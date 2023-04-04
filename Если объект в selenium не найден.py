from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)"
                     "Chrome/108.0.0.0 Safari/537.36")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://ya.ru/")

try:
    element = driver.find_element('id', "nonexistent-element")
    # do something with the element
except NoSuchElementException:
    # element not found, continue to next statement
    pass

# continue with the next statement
print("Next statement")