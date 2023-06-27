from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from pprint import pprint


class GovScraper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)

        s = Service(executable_path='path_to_chromedriver')
        self.driver = webdriver.Chrome(service=s, options=options)

        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            'source': '''
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
          '''
        })

        name = '+79516109285'
        password = 'Kotik008/lol'

    def scrape_links(self):
        try:
            self.driver.get('https://torgi.gov.ru/new/public')
            self.driver.implicitly_wait(10)

            bidding = self.driver.find_element(by='xpath', value='//*[@id="dropdownManual"]/button')
            bidding.click()
            category = self.driver.find_element(By.XPATH, value='/html/body/app-root/app-layout/main/app-work-area/div/div/div['
                                                           '1]/app-public-shell/div/div/app-public-main/div['
                                                           '1]/app-main-header/div/div/div/div['
                                                           '2]/app-main-header-nav-bar/div/app-dropdown/div/div/app'
                                                           '-categories/div[1]/div[2]/div[3]/div[2]/a')
            category.click()
            location = self.driver.find_element(by='xpath', value='/html/body/app-root/app-layout/main/app-work-area/div/div/div['
                                                             '1]/app-public-shell/div/div/app-lot-list/div[2]/div['
                                                             '1]/app-lot-filter/form/div[4]/app-form-item/div/div['
                                                             '2]/app-select/ng-select')
            location.click()
            kemerovo_region = self.driver.find_element(by='xpath', value='//*[@id="item-70"]/div/span')
            kemerovo_region.click()

            show_more = self.driver.find_element(by='xpath',
                                                 value='/html/body/app-root/app-layout/main/app-work-area/div/div/div['
                                                       '1]/app-public-shell/div/div/app-lot-list/div[2]/div[2]/div/app-button')
            show_more.click()
            show_more.click()

            # получаем html страницу и парсим ее
            html = self.driver.page_source
            suop = BeautifulSoup(html, 'lxml')
            all_lot = suop.find_all('app-lot-list-item')

            list_link = []

            for lot in all_lot:
                list_link.append('https://torgi.gov.ru' + lot.find(class_='lotLink').get('href'))

            return list_link

        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()
            self.driver.quit()

scrapy = GovScraper()
pprint(scrapy.scrape_links())