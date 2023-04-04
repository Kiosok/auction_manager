from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# Здесь будем парсить сам лот

with open('torgi.html', 'r', encoding='utf-8') as file:
    html = file.read()

suop = BeautifulSoup(html, 'lxml')
all_lot = suop.find_all('app-lot-list-item')

for lot in all_lot:
    print(lot.find(class_='lotLink').get('href'))