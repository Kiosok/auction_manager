import os
import time

import fake_useragent
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoaderDocs:
    """Загрузчик документов. Принимает ссылку на документы и номер лота"""
    def __init__(self, url, number_lot):
        self.url = url
        self.download_dir = "/Users/bender/PycharmProjects/auction_manager/docs/" + str(number_lot)
        self.user = fake_useragent.UserAgent().random
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'"user-agent": {self.user}')
        self.options.add_experimental_option('prefs', {
            'download.default_directory': self.download_dir,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': True
        })
        self.options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=self.options)

    def download_elements(self):
        """Скачивает документы в нужную папку."""
        try:
            self.driver.get(self.url)

            # Поиск элементов файлов с помощью CSS_SELECTOR и клик по ним, чтобы скачать
            website_docs = self.driver.find_elements(By.CSS_SELECTOR, ".word-break-caption")
            for dow_doc in website_docs:
                time.sleep(1)
                dow_doc.click()
                time.sleep(1)

            downloaded_files = os.listdir(self.download_dir)

            return downloaded_files
        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()
            self.driver.quit()


# Пример использования класса
downloader = LoaderDocs(
    "https://torgi.gov.ru/new/public/lots/lot/22000024510000000007_1/(lotInfo:docs)?fromRec=false#lotInfoSection-docs",
    "lot 655556№2")
downloaded_files = downloader.download_elements()
print(len(downloaded_files))
