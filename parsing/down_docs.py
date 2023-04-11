from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import lxml
import pickle

url = "https://torgi.gov.ru/new/public/lots/lot/22000010620000000068_3/(lotInfo:docs)?fromRec=false#lotInfoSection-docs"

# объект опций
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)"
                     "Chrome/108.0.0.0 Safari/537.36")
# работа в фоновом режиме
#options.add_argument("headless")
# Отключения режима webdriver
# options.add_argument("--disable-blink-features=AutomationControlled")

# Загрузка файлов в назначенное место
options.add_experimental_option('prefs', {
    'download.default_directory': '/Users/bender/PycharmProjects/auction_manager/docs/',
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': False
})



# драйвер хрома и передаваемые в него аргументы
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:

    driver.get(url)

    time.sleep(3)


    website_docs = driver.find_elements(By.CLASS_NAME, 'attachments-list__item__buttons__left-col')
    for dow_doc in website_docs:
        dow_doc.click()

    print('Нажал')
    time.sleep(1)


    # получаем html страницу и парсим ее
    html = driver.page_source
    suop = BeautifulSoup(html, 'lxml')
    all_lot = suop.find_all('app-lot-list-item')

    list_link = []

    for lot in all_lot:
        list_link.append('https://torgi.gov.ru' + lot.find(class_='lotLink').get('href'))

    # принтует все ссылки на текущие лоты
    print(list_link)


    time.sleep(15)

except Exception as ex:

    print(ex)
finally:
    driver.close()
    driver.quit()
