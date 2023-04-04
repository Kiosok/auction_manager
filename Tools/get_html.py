from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_html(name_html, url):
    """Создаем html файл по ссылке"""

    # объект опций
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)"
                         "Chrome/108.0.0.0 Safari/537.36")
    # Отключения режима webdriver
    options.add_argument("--disable-blink-features=AutomationControlled")
    # работа в фоновом режиме
    options.add_argument("--headless")

    # драйвер хрома и передаваемые в него аргументы
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    try:

        driver.get(url)

        # получаем html страницу и парсим ее
        html = driver.page_source
        with open(f'{name_html}.html', 'w', encoding='utf-8') as file:
            file.write(html)

        print(f'Файл {name_html}.html создан.')

    except Exception as ex:

        print(ex)
    finally:
        driver.close()
        driver.quit()


get_html('my_lot', 'https://torgi.gov.ru/new/public/lots/lot/22000010620000000068_3/(lotInfo:info)?fromRec=false')