from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import fake_useragent

import time
import lxml
import pickle

url = "https://torgi.gov.ru/new/public"
name = '+79516109285'
password = 'Kotik008/'
# user agent
user = fake_useragent.UserAgent().random
# объект опций
options = webdriver.ChromeOptions()
options.add_argument(f'"user-agent": {user}')

# работа в фоновом режиме
# options.add_argument("headless")
# Отключения режима webdriver
# options.add_argument("--disable-blink-features=AutomationControlled")

# драйвер хрома и передаваемые в него аргументы
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:

    driver.get(url)
    driver.implicitly_wait(10)

    login_gov = driver.find_element(By.XPATH,
                                     "/html/body/app-root/app-layout/main/app-work-area/div/div/ng-sidebar"
                                     "-container/div/div[1]/app-public-shell/div/div/app-public-main/div["
                                     "1]/app-main-header/div/div/div/div[3]/app-login/app-button/button/span[2]")
    login_gov.click()

    login_gos = driver.find_element(By.ID, 'login')
    login_gos.send_keys(name)
    password_gos = driver.find_element(By.ID, 'password')
    password_gos.send_keys(password)

    verify = driver.find_element(By.XPATH, '/html/body/esia-root/div/esia-login/div/div[1]/form/div[4]/button')
    verify.click()

    one_click = driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/app-organization-select-modal/div['
                                              '2]/div[1]/div/div[4]/app-big-radio-button[2]/label/span')
    one_click.click()
    two_click = driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/app-organization-select-modal/div['
                                              '3]/app-button[2]/button/span[2]')
    two_click.click()
    free_click = driver.find_element(By.XPATH,
                                     "/html/body/ngb-modal-window/div/div/app-organization-select-modal/div[2]/div["
                                     "2]/div/ul/li/div")
    free_click.click()
    four_click = driver.find_element(By.XPATH,
                                     "/html/body/ngb-modal-window/div/div/app-organization-select-modal/div["
                                     "3]/app-button[2]/button/span[2]")
    four_click.click()

    print('Нажал')
    time.sleep(39)

except Exception as ex:

    print(ex)
finally:
    driver.close()
    driver.quit()
