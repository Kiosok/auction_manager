from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import time
import pickle


def authentication():
    """Вход на сайт через login and password и выгрузка куки."""

    url = "https://torgi.gov.ru/new/public"

    # объект опций
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)"
                         "Chrome/108.0.0.0 Safari/537.36")

    # Получаем строку, содержащую путь к рабочей директории:
    dir_path = Path.cwd()
    # Объединяем полученную строку с недостающими частями пути
    path = str(Path(dir_path, 'chromdriver.exe'))
    # выведем значение переменной path:
    print(path)

    # драйвер хрома и передаваемые в него аргументы
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    try:

        driver.get(url)

        time.sleep(1)

        bidding = driver.find_element(by='xpath', value='//*[@id="dropdownManual"]/button')
        bidding.click()
        category = driver.find_element(by='xpath', value='/html/body/app-root/app-layout/main/app-work-area/div/div'
                                                         '/ng-sidebar-container/div/div[1]/app-public-shell/div/div/'
                                                         'app-public-main/div[1]/app-main-header/div/div/div/div[2]/'
                                                         'app-main-header-nav-bar/div/app-dropdown/div/div/'
                                                         'app-categories/div[1]/div[2]/div[3]/div[2]/a/span')
        category.click()
        location = driver.find_element(by='xpath', value='/html/body/app-root/app-layout/main/app-work-area/div/div'
                                                         '/ng-sidebar-container/div/div['
                                                         '1]/app-public-shell/div/div/app-lot-list/div[2]/div['
                                                         '1]/app-lot-filter/form/div[4]/app-form-item/div/div['
                                                         '2]/app-select/ng-select/div/div/div[2]')
        location.click()
        kemerovo_region = driver.find_element(by='xpath', value='//*[@id="item-70"]/div/span/span')
        kemerovo_region.click()

        show_more = driver.find_element(by='xpath', value='/html/body/app-root/app-layout/main/app-work-area/div/div'
                                                          '/ng-sidebar-container/div/div['
                                                          '1]/app-public-shell/div/div/app-lot-list/div[2]/div['
                                                          '2]/div/app-button/button/span[2]')
        show_more.click()
        show_more.click()

        time.sleep(15)

    except Exception as ex:

        print(ex)
    finally:
        driver.close()
        driver.quit()


authentication()
