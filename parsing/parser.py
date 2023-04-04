from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# Здесь будем парсить сам лот
with open('my_lot.html', 'r', encoding='utf-8') as file:
    html_1 = file.read()
with open('my_lot_public.html', 'r', encoding='utf-8') as file_2:
    html_2 = file_2.read()


def search_text(class_tag):
    text_class = suop.find(class_=f'{class_tag}').text.strip()
    return text_class


# меняем местами чтобы понимать что на обоих страницах работает
html =  html_1 + html_2

suop = BeautifulSoup(html, 'lxml')

header_title = search_text('header_title')
status = search_text('status').replace(' Добавить в избранное', '')
lotbiddform = search_text('lotBiddForm with-small-bottom-gap')
alert_content = search_text('alert-content')
lot_number = search_text('lotAttributeValue')
initial_price = search_text('prices__row__price-cell lotPrice')
auction_step = suop.find_all(class_='prices__row__price-cell lotPrice')[1].text.strip()
type_of_lease = suop.find_all(class_='lotAttributeValue')[1].text.strip()

print(lot_number)


# all_lot = suop.find_all('app-lot-list-item')
#
# for lot in all_lot:
#     print(lot.find(class_='lotLink').get('href'))