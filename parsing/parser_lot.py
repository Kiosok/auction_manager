from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def parser_link_lot(url):
    """Парсим все данные со страницы."""

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)
        # Wait for the page to fully load
        driver.implicitly_wait(10)
        time.sleep(3.3)
        html = driver.page_source
        # Do something with the HTML

        print(html)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    # Все данные с главной шапки
    dict_lot = {}

    def search_text(class_tag, name_teg=''):
        text_class = suop.find(class_=f'{class_tag}')
        if text_class is None:
            text_class = suop.find(class_=f'lotBiddForm')

        text_class = text_class.text.strip()
        if 'Добавить в избранное' in text_class:
            text_class = text_class.replace(' Добавить в избранное', '')

        """Добавление в словарь"""
        return {name_teg: text_class}

    def search_name_value(class_name, class_value):
        keys = []
        values = []

        div_keys = suop.find_all(class_=f'{class_name}')
        for i in div_keys:
            keys.append(i.text.strip())

        div_values = suop.find_all(class_=f'{class_value}')
        for f in div_values:
            values.append(f.text.strip())

        dict_text = {k: v for k, v in zip(keys, values)}

        return dict_text

    def replace_value_is_key(my_dict):
        """Удаляет из ключа текст значения"""
        for key, value in my_dict.items():
            if value in key:
                new_key = key.replace(value, '').strip()
                my_dict[new_key] = my_dict.pop(key).strip()
        return my_dict

    suop = BeautifulSoup(html, 'lxml')

    # Отдельные элименты
    lotbiddform = search_text('lotBiddForm with-small-bottom-gap', 'Форма заявки')
    status = search_text('status', 'Статус')

    # Шапка
    dict_lot_handler = search_name_value('lotAttributeName', 'lotAttributeValue')

    # Все данные с информация о лоте
    dict_lot_information = search_name_value('attr_title', 'attr_value')

    # Характеристики лота
    lot_characteristics = replace_value_is_key(search_name_value('char', 'lotAttributeDetail no-padding-bottom'))

    # Объединение в единый словарь
    dict_lot.update(dict_lot_handler)
    dict_lot.update(dict_lot_information)
    dict_lot.update(lot_characteristics)
    dict_lot.update(lotbiddform)
    dict_lot.update(status)
    dict_lot.update({'link_lot': url})
    dict_lot.update({'condition': 'Новые'})
    print(dict_lot)
    return dict_lot

# Попробовал всё связать
from links_to_lots import GovScraper

scraper = GovScraper()
links = scraper.scrape_links()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

for link in links:
    dict_lot = parser_link_lot(link)
    from lot import lot

    obj_lot = lot.Lot(dict_lot)

    engine = create_engine('sqlite:///lots.db')
    Session = sessionmaker(bind=engine)
    from lot import lot

    Base = lot.Base

    Base.metadata.create_all(engine)  # create tables
    session = Session()
    session.merge(obj_lot)
    session.commit()
