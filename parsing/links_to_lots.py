from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


class GovScraper:
    def __init__(self):
        self.url = "https://torgi.gov.ru/new/public"
        self.options = Options()
        self.options.add_argument("user-agent=Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)"
                     "Chrome/108.0.0.0 Safari/537.36")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=self.options)

    def scrape_links(self):
        try:
            self.driver.get(self.url)

            time.sleep(1)

            bidding = self.driver.find_element(by='xpath', value='//*[@id="dropdownManual"]/button')
            bidding.click()
            category = self.driver.find_element(by='xpath', value='/html/body/app-root/app-layout/main/app-work-area/div/div'
                                                             '/ng-sidebar-container/div/div[1]/app-public-shell/div/div/'
                                                             'app-public-main/div[1]/app-main-header/div/div/div/div[2]/'
                                                             'app-main-header-nav-bar/div/app-dropdown/div/div/'
                                                             'app-categories/div[1]/div[2]/div[3]/div[2]/a/span')
            category.click()
            location = self.driver.find_element(by='xpath', value='/html/body/app-root/app-layout/main/app-work-area/div/div'
                                                             '/ng-sidebar-container/div/div['
                                                             '1]/app-public-shell/div/div/app-lot-list/div[2]/div['
                                                             '1]/app-lot-filter/form/div[4]/app-form-item/div/div['
                                                             '2]/app-select/ng-select/div/div/div[2]')
            location.click()
            kemerovo_region = self.driver.find_element(by='xpath', value='//*[@id="item-70"]/div/span/span')
            kemerovo_region.click()

            show_more = self.driver.find_element(by='xpath',
                                            value='/html/body/app-root/app-layout/main/app-work-area/div/div'
                                                  '/ng-sidebar-container/div/div['
                                                  '1]/app-public-shell/div/div/app-lot-list/div[2]/div['
                                                  '2]/div/app-button/button/span[2]')
            show_more.click()
            show_more.click()

            # получаем html страницу и парсим ее
            html = self.driver.page_source
            suop = BeautifulSoup(html, 'lxml')
            all_lot = suop.find_all('app-lot-list-item')

            list_link = []

            for lot in all_lot:
                list_link.append('https://torgi.gov.ru' + lot.find(class_='lotLink').get('href'))

            print(list_link)

            return list_link

        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()
            self.driver.quit()