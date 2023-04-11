from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# Здесь будем парсить сам лот
with open('my_lot.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Все данные с главной шапки
dict_lot = {}


def search_text(class_tag, name_teg=''):
    text_class = suop.find(class_=f'{class_tag}').text.strip()
    if 'Добавить в избранное' in text_class:
        text_class = text_class.replace(' Добавить в избранное', '')

    """Добавление в словарь"""
    return {name_teg:text_class}


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


# меняем местами чтобы понимать что на обоих страницах работает
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
dict_lot.update({'link_lot': 'link', 'link_doc': 'link'})
print(dict_lot)

# Ссылка на документы
"""Изменить в предыдущем документе создания ссылок на доки файлов.
Или впринципе создать отдельный метод на скачивание'Класс'. 
Который будет брать ссылку из класса лота приобразовывать её и скачивать"""
# https://torgi.gov.ru/new/public/lots/lot/22000010620000000068_3/(lotInfo:docs)?fromRec=false#lotInfoSection-docs
# https://torgi.gov.ru/new/public/lots/lot/22000010620000000068_3/(lotInfo:info)?fromRec=false#lotInfoSection-info