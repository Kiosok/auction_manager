from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import pyqtSignal


class WidgetOrder(QWidget):
    """Предоставляет краткую информацию о лоте и позволяет проводить с ним манипуляции"""
    signal_mouse = pyqtSignal()

    def __init__(self):

        super().__init__()
        # Инициализируем label для вывода small widget.
        self.label_application_form = QLabel('Электронная площадка')
        self.label_subject_of_bidding = QLabel("Земельный участок кадастр\nномер 42:07:0110001:385,\nплощадью 3465005 кв.м.")
        self.label_land_area_name = QLabel("Площадь земельного участка:")
        self.label_land_area = QLabel("3 465 005 кв.м.")
        self.label_e_platform_name = QLabel("Электронная площадка")
        self.label_e_platform = QLabel("РТС-тендер")

        self.label_status = QLabel("Прием заявок")
        self.label_trade_type = QLabel("Аренда и продажа земельных участков")
        self.label_initial_price_name = QLabel("Начальная цена")
        self.label_initial_price = QLabel("255 717, 37 Р")
        self.label_cadastral_number_name = QLabel("Кадастровый номер земельного участка:")
        self.label_cadastral_number = QLabel("42:07:0110001:385")
        self.label_closing_date_name = QLabel("Дата и время окончания подачи заявок")
        self.label_closing_date = QLabel("08.06.2023 17:00 (MCK+4)")

        # Переменные full widget
        self.lot_description = QLabel('земельный участок  в кадастровом квартале 42:09:2603001')

        self.lot_number = QLabel('Извещение, лот')
        self.subject_property_location = QLabel('Ханты-Мансийский автономный округ')
        self.property_location = QLabel('АО Ханты-Мансийский Автономный округ - Югра, г.о. Нягань, г. Нягань, ул Сибирская, дом 40 к. 1')
        self.start_date = QLabel('Дата и время начала подачи заявок')
        self.date_of_bidding = QLabel('10.08.2023 14:00 (МСК+2)')
        self.object_category = QLabel('Автобусы')
        self.form_of_ownership = QLabel('Муниципальная собственность')
        self.term_of_agreement = QLabel('в течение 5 рабочих дней с даты проведения продажи')
        self.type_of_contract = QLabel('договор аренды земельного участка')
        self.lease_term = QLabel('Срок аренды')
        self.auction_step = QLabel('10 974,93 ₽ (3,00 %)')
        self.deposit_amount = QLabel('Размер задатка')
        self.recipient = QLabel('Получатель')
        self.purpose_of_payment = QLabel('Назначение платежа')
        self.type_of_use = QLabel('Обеспечение сельскохозяйственного производства')

        self.link_lot = QLabel('https://torgi.gov.ru/new/public/lots/lot/22000010620000000167_1/(lotInfo:info)?fromRec=false')
        self.condition = QLabel('Новые')

        # Располагаем label по сетке
        self.layout_small_order = QGridLayout()
        self.layout_small_order.addWidget(self.label_application_form, 0, 0, 1, 1)
        self.layout_small_order.addWidget(self.label_subject_of_bidding, 1, 0, 3, 1)
        self.layout_small_order.addWidget(self.label_land_area_name, 4, 0, 1, 1)
        self.layout_small_order.addWidget(self.label_land_area, 5, 0, 1, 1)
        self.layout_small_order.addWidget(self.label_e_platform_name, 6, 0, 1, 1)
        self.layout_small_order.addWidget(self.label_e_platform, 7, 0, 1, 1)

        self.layout_small_order.addWidget(self.label_status, 0, 1, 1, 1)
        self.layout_small_order.addWidget(self.label_trade_type, 1, 1, 1, 1)
        self.layout_small_order.addWidget(self.label_initial_price_name, 2, 1, 1, 1)
        self.layout_small_order.addWidget(self.label_initial_price, 3, 1, 1, 1)
        self.layout_small_order.addWidget(self.label_cadastral_number_name, 4, 1, 1, 1)
        self.layout_small_order.addWidget(self.label_cadastral_number, 5, 1, 1, 1)
        self.layout_small_order.addWidget(self.label_closing_date_name, 6, 1, 1, 1)
        self.layout_small_order.addWidget(self.label_closing_date, 7, 1, 1, 1)

        self.setLayout(self.layout_small_order)

        # Форматируем label, шрифт/размер
        self.label_application_form.setStyleSheet("color: rgb(60, 54, 255); background-color: rgba(255, 255, 255, 0);")
        self.label_subject_of_bidding.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_land_area_name.setStyleSheet("color: rgb(108, 108, 108); background-color: rgba(255, 255, 255, 0);")
        self.label_land_area.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_e_platform_name.setStyleSheet("color: rgb(108, 108, 108); background-color: rgba(255, 255, 255, 0);")
        self.label_e_platform.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.label_status.setStyleSheet("background-color: rgba(255, 255, 255, 0); color: rgb(60, 54, 255);")
        self.label_trade_type.setStyleSheet("color: rgb(108, 108, 108); background-color: rgba(255, 255, 255, 0);")
        self.label_initial_price_name.setStyleSheet("color: rgb(108,108,108); background-color: rgba(255,255,255,0);")
        self.label_initial_price.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_cadastral_number_name.setStyleSheet("color: rgb(108,108,108);background-color: rgba(255,255,255,0);")
        self.label_cadastral_number.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_closing_date_name.setStyleSheet("color: rgb(108,108,108); background-color: rgba(255,255,255,0);")
        self.label_closing_date.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        # Размеры для шрифтов
        font_7 = QFont()
        font_7.setPointSize(7)
        font_9 = QFont()
        font_9.setPointSize(9)
        self.font_14 = QFont()
        self.font_14.setBold(True)
        self.font_14.setPointSize(10)
        self.font_12 = QFont()
        self.font_12.setPointSize(12)

        self.label_application_form.setFont(font_7)
        self.label_subject_of_bidding.setFont(font_9)
        self.label_land_area_name.setFont(font_7)
        self.label_land_area.setFont(font_9)
        self.label_e_platform_name.setFont(font_7)
        self.label_e_platform.setFont(font_9)

        self.label_status.setFont(font_7)
        self.label_trade_type.setFont(font_7)
        self.label_initial_price_name.setFont(font_7)
        self.label_initial_price.setFont(font_9)
        self.label_cadastral_number_name.setFont(font_7)
        self.label_cadastral_number.setFont(font_9)
        self.label_closing_date_name.setFont(font_7)
        self.label_closing_date.setFont(font_9)

    def mouseReleaseEvent(self, e):
        self.signal_mouse.emit()

        print(f'Вы нажали на SmallWidget {e.button()}')


class WidgetFullOrder(WidgetOrder):
    """Предоставляет всю информацию о лоте и позволяет проводить с ним манипуляции"""
    def __init__(self):
        super().__init__()
        # Выбор статуса ордера
        set_status = QComboBox()
        set_status.addItems(['Новые', 'На согласование', 'В работе', 'Завершенные', 'Не участвуем', 'Архив'])
        print(set_status.currentIndex())
        self.layout_small_order.addWidget(set_status, 8, 0, 1, 2)

        # Документы
        marker_doc = QLabel("Место для документов")
        marker_doc.setStyleSheet("background-color: rgb(185, 236, 87);")

        self.layout_small_order.addWidget(marker_doc, 9, 0, 1, 1)

        # Карта
        marker_map = QLabel("              Карта")
        marker_map.setStyleSheet("background-color: rgb(175, 55, 75);")

        self.layout_small_order.addWidget(marker_map, 9, 1, 1, 1)

        # Сведения о лоте надпись
        name_information_lot = QLabel('Сведенья о лоте')
        name_information_lot.setFont(self.font_14)
        self.layout_small_order.addWidget(name_information_lot, 12, 0, 1, 2)

        # Предмет торгов
        name_lot_description = QLabel('Предмет торгов (наименование лота)')
        name_lot_description.setFont(self.font_14)
        self.layout_small_order.addWidget(name_lot_description, 13, 0, 1, 2)
        self.layout_small_order.addWidget(self.lot_description, 14, 0, 1, 2)

        # Субъект местонахождения имущества
        name_subject_property_location = QLabel('Субъект местонахождения имущества')
        name_subject_property_location.setFont(self.font_14)
        self.layout_small_order.addWidget(name_subject_property_location, 15, 0, 1, 2)
        self.layout_small_order.addWidget(self.subject_property_location, 16, 0, 1, 2)

        # Местонахождение имущества
        name_property_location = QLabel('Местонахождение имущества')
        name_property_location.setFont(self.font_14)
        self.layout_small_order.addWidget(name_property_location, 17, 0, 1, 2)
        self.layout_small_order.addWidget(self.property_location, 18, 0, 1, 2)

        # Категория объекта
        name_object_category = QLabel('Категория объекта')
        name_object_category.setFont(self.font_14)
        self.layout_small_order.addWidget(name_object_category, 19, 0, 1, 2)
        self.layout_small_order.addWidget(self.object_category, 20, 0, 1, 2)

        # Форма собственности
        name_form_of_ownership = QLabel('Форма собственности')
        name_form_of_ownership.setFont(self.font_14)
        self.layout_small_order.addWidget(name_form_of_ownership, 21, 0, 1, 2)
        self.layout_small_order.addWidget(self.form_of_ownership, 22, 0, 1, 2)

        # Дата проведения торгов
        name_date_of_bidding = QLabel('Дата проведения торгов')
        name_date_of_bidding.setFont(self.font_14)
        self.layout_small_order.addWidget(name_date_of_bidding, 23, 0, 1, 2)
        self.layout_small_order.addWidget(self.date_of_bidding, 24, 0, 1, 2)

        # Срок заключения договора
        name_term_of_agreement = QLabel('Срок заключения договора')
        name_term_of_agreement.setFont(self.font_14)
        self.layout_small_order.addWidget(name_term_of_agreement, 25, 0, 1, 2)
        self.layout_small_order.addWidget(self.term_of_agreement, 26, 0, 1, 2)

        # Вид договора
        name_type_of_contract = QLabel('Вид договора')
        name_type_of_contract.setFont(self.font_14)
        self.layout_small_order.addWidget(name_type_of_contract, 27, 0, 1, 2)
        self.layout_small_order.addWidget(self.type_of_contract, 28, 0, 1, 2)

        # Шаг аукциона
        name_auction_step = QLabel('Шаг аукциона')
        name_auction_step.setFont(self.font_14)
        self.layout_small_order.addWidget(name_auction_step, 29, 0, 1, 2)
        self.layout_small_order.addWidget(self.auction_step, 30, 0, 1, 2)

        # Размер задатка
        name_deposit_amount = QLabel('Размер задатка')
        name_deposit_amount.setFont(self.font_14)
        self.layout_small_order.addWidget(name_deposit_amount, 31, 0, 1, 2)
        self.layout_small_order.addWidget(self.deposit_amount, 32, 0, 1, 2)

        # Характеристики лота
        label_features_lot = QLabel('Характеристики лота')
        label_features_lot.setFont(self.font_14)

        # Вид разрешённого использования земельного участка
        name_type_of_contract = QLabel('Вид разрешённого использования земельного участка')
        self.layout_small_order.addWidget(name_type_of_contract, 33, 0, 1, 2)
        self.layout_small_order.addWidget(self.type_of_contract, 34, 0, 1, 2)

        self.layout_small_order.addWidget(label_features_lot, 35, 0, 1, 2)

        # ссылка на офф. сайт
        name_link = QLabel(f'<a href="{self.link_lot.text()}">Ссылка на офф. сайт</a>')
        name_link.setOpenExternalLinks(True)
        self.layout_small_order.addWidget(name_link)


if __name__ == '__main__':
    app = QApplication([])
    window = WidgetFullOrder()
    window.show()
    app.exec()




