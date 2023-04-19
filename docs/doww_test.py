from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import fake_useragent
import os
import time
import lxml
import pickle

url = "https://torgi.gov.ru/new/public/lots/lot/22000024510000000007_1/(lotInfo:docs)?fromRec=false#lotInfoSection-docs"
# user agent
user = fake_useragent.UserAgent().random
# объект опций
options = webdriver.ChromeOptions()
options.add_argument(f'"user-agent": {user}')

# Загрузка файлов в назначенное место
download_dir = '/Users/bender/PycharmProjects/auction_manager/docs/Bur'
options.add_experimental_option('prefs', {
    'download.default_directory': download_dir,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

# работа в фоновом режиме
#options.add_argument("--headless=new")
# Отключения режима webdriver
# options.add_argument("--disable-blink-features=AutomationControlled")


# драйвер хрома и передаваемые в него аргументы
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:

    driver.get(url)

    time.sleep(5)

    website_docs = driver.find_elements(By.CSS_SELECTOR, "body > app-root > app-layout > main > app-work-area > div > div > ng-sidebar-container > div > div:nth-child(1) > app-public-shell > div > div > app-lot-item > div > div > div:nth-child(3) > div.work-space > div > div.tab-form-content > app-lot-docs > div > div:nth-child(4) > app-hashed-attachments-list > div > div:nth-child(1) > div > div.file-name-with-info > div.attachments-list__item__buttons__left-col > app-button.attachments-list__item__buttons__name.align-label-left.display-flex.text-button-no-center.word-break-caption")
    print(website_docs)

    # Find all elements with a class of "example-selector"
    # объеденить с изначальным поиском элементов чтобы они страховали друг друга
    website_docs = driver.find_elements(By.CSS_SELECTOR, ".word-break-caption")
    for dow_doc in website_docs:
        time.sleep(1)
        dow_doc.click()
        time.sleep(1)


    time.sleep(3)
    print('Документы скачены')
    downloaded_files = os.listdir(download_dir)
    print(downloaded_files)


except Exception as ex:

    print(ex)
finally:
    driver.close()
    driver.quit()
