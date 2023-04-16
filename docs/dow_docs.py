from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import fake_useragent
import os
import time
import lxml
import pickle

url = "https://torgi.gov.ru/new/public/lots/lot/22000010210000000915_1/(lotInfo:docs)?fromRec=false#lotInfoSection-docs"
# user agent
user = fake_useragent.UserAgent().random
# объект опций
options = webdriver.ChromeOptions()
options.add_argument(f'"user-agent": {user}')

# Загрузка файлов в назначенное место
download_dir = '/Users/bender/PycharmProjects/auction_manager/docs/'
options.add_experimental_option('prefs', {
    'download.default_directory': download_dir,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

# работа в фоновом режиме
options.add_argument("headless")
# Отключения режима webdriver
# options.add_argument("--disable-blink-features=AutomationControlled")


# драйвер хрома и передаваемые в него аргументы
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:

    driver.get(url)

    time.sleep(5)

    website_docs = driver.find_elements(By.CLASS_NAME, 'attachments-list__item__buttons__left-col')
    for dow_doc in website_docs:
        dow_doc.click()
    time.sleep(10)
    print('Документы скачены')
    downloaded_files = os.listdir(download_dir)
    print(downloaded_files)


except Exception as ex:

    print(ex)
finally:
    driver.close()
    driver.quit()
