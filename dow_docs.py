import os
import time
import fake_useragent
from selenium import webdriver
from selenium.webdriver.common.by import By


class Loader:

    def __init__(self, lot):
        self.url = lot.link_doc
        self.download_dir = "/Users/bender/PycharmProjects/auction_manager/docs/" + str(lot.lot_number)
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

    def download_files(self):
        """Загрузить файлы"""
        try:
            self.driver.get(self.url)
            website_docs = self.driver.find_elements(By.CLASS_NAME, 'attachments-list__item__buttons__left-col')
            for dow_doc in website_docs:
                dow_doc.click()
            time.sleep(5)
            downloaded_files = os.listdir(self.download_dir)

            return downloaded_files
        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()
            self.driver.quit()


# Пример использования класса
# downloader = ElementDownloader(
#     "https://torgi.gov.ru/new/public/lots/lot/22000024510000000007_1/(lotInfo:docs)?fromRec=false#lotInfoSection-docs",
#     "lot 655556№2")
# downloaded_files = downloader.download_elements()
# print(len(downloaded_files))
