from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import pyqtSignal


class WidgetOrder(QWidget):
    """Предоставляет краткую информацию о лоте и позволяет проводить с ним манипуляции"""
    signal_mouse = pyqtSignal()

    def __init__(self, dict_lot):

        super().__init__()
        # Инициализируем label для вывода small widget.

        lot_number = dict_lot.get('lot_number', 'None')
        trade_type = dict_lot.get('trade_type', 'None')
        e_platform = dict_lot.get('e_platform', 'None')
        subject_property_location = dict_lot.get('subject_property_location', 'None')
        start_date = dict_lot.get('start_date', 'None')
        closing_date = dict_lot.get('closing_date', 'None')
        date_of_bidding = dict_lot.get('date_of_bidding', 'None')
        subject_of_bidding = dict_lot.get('subject_of_bidding', 'None')
        lot_description = dict_lot.get('lot_description', 'None')
        property_location = dict_lot.get('property_location', 'None')
        object_category = dict_lot.get('object_category', 'None')
        form_of_ownership = dict_lot.get('form_of_ownership', 'None')
        term_of_agreement = dict_lot.get('term_of_agreement', 'None')
        type_of_contract = dict_lot.get('type_of_contract', 'None')
        lease_term = dict_lot.get('lease_term', 'None')
        initial_price = dict_lot.get('initial_price', 'None')
        auction_step = dict_lot.get('auction_step', 'None')
        deposit_amount = dict_lot.get('deposit_amount', 'None')
        recipient = dict_lot.get('recipient', 'None')
        purpose_of_payment = dict_lot.get('purpose_of_payment', 'None')
        cadastral_number = dict_lot.get('cadastral_number', 'None')
        land_area = dict_lot.get('land_area', 'None')
        type_of_use = dict_lot.get('type_of_use', 'None')
        application_form = dict_lot.get('application_form', 'None')
        status = dict_lot.get('status', 'None')

        condition = dict_lot.get('condition', 'Новые')
        link_lot = dict_lot.get('link_lot', 'None')

        # Переменные small widget

        self.application_form = QLabel(application_form)
        # Номер лота
        self.subject_of_bidding = QLabel(lot_number)
        self.label_land_area_name = QLabel("Площадь земельного участка:")
        self.land_area = QLabel(land_area)
        self.label_e_platform_name = QLabel("Электронная площадка")
        self.e_platform = QLabel(e_platform)

        self.status = QLabel(status)
        self.trade_type = QLabel(trade_type)
        self.label_initial_price_name = QLabel("Начальная цена")
        self.initial_price = QLabel(initial_price)
        self.label_cadastral_number_name = QLabel("Кадастровый номер земельного участка:")
        self.cadastral_number = QLabel(cadastral_number)
        self.label_closing_date_name = QLabel("Дата и время окончания подачи заявок")
        self.closing_date = QLabel(closing_date)

        # Переменные full widget

        # Временный ограничитель длины строки
        import textwrap
        wrapped = textwrap.wrap(lot_description, width=80)
        lot_description = '\n'.join(wrapped)
        self.lot_description = QLabel(lot_description)

        self.lot_number = QLabel(lot_number)
        self.subject_property_location = QLabel(subject_property_location)
        self.property_location = QLabel(property_location)
        self.start_date = QLabel(start_date)
        self.date_of_bidding = QLabel(date_of_bidding)
        self.object_category = QLabel(object_category)
        self.form_of_ownership = QLabel(form_of_ownership)
        self.term_of_agreement = QLabel(term_of_agreement)
        self.type_of_contract = QLabel(type_of_contract)
        self.lease_term = QLabel(lease_term)
        self.auction_step = QLabel(auction_step)
        self.deposit_amount = QLabel(deposit_amount)
        self.recipient = QLabel(recipient)
        self.purpose_of_payment = QLabel(purpose_of_payment)
        self.type_of_use = QLabel(type_of_use)

        self.link_lot = QLabel(link_lot)
        self.condition = QLabel(condition)

        # Располагаем label по сетке
        self.layout_small_order = QGridLayout()
        self.layout_small_order.addWidget(self.application_form, 0, 0, 1, 1)
        self.layout_small_order.addWidget(self.subject_of_bidding, 1, 0, 3, 1)
        self.layout_small_order.addWidget(self.label_land_area_name, 4, 0, 1, 1)
        self.layout_small_order.addWidget(self.land_area, 5, 0, 1, 1)
        self.layout_small_order.addWidget(self.label_e_platform_name, 6, 0, 1, 1)
        self.layout_small_order.addWidget(self.e_platform, 7, 0, 1, 1)

        self.layout_small_order.addWidget(self.status, 0, 1, 1, 1)
        self.layout_small_order.addWidget(self.trade_type, 1, 1, 1, 1)
        self.layout_small_order.addWidget(self.label_initial_price_name, 2, 1, 1, 1)
        self.layout_small_order.addWidget(self.initial_price, 3, 1, 1, 1)
        self.layout_small_order.addWidget(self.label_cadastral_number_name, 4, 1, 1, 1)
        self.layout_small_order.addWidget(self.cadastral_number, 5, 1, 1, 1)
        self.layout_small_order.addWidget(self.label_closing_date_name, 6, 1, 1, 1)
        self.layout_small_order.addWidget(self.closing_date, 7, 1, 1, 1)

        self.setLayout(self.layout_small_order)

        # Форматируем label, шрифт/размер
        self.application_form.setStyleSheet("color: rgb(60, 54, 255); background-color: rgba(255, 255, 255, 0);")
        self.subject_of_bidding.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_land_area_name.setStyleSheet("color: rgb(108, 108, 108); background-color: rgba(255, 255, 255, 0);")
        self.land_area.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_e_platform_name.setStyleSheet("color: rgb(108, 108, 108); background-color: rgba(255, 255, 255, 0);")
        self.e_platform.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.status.setStyleSheet("background-color: rgba(255, 255, 255, 0); color: rgb(60, 54, 255);")
        self.trade_type.setStyleSheet("color: rgb(108, 108, 108); background-color: rgba(255, 255, 255, 0);")
        self.label_initial_price_name.setStyleSheet("color: rgb(108,108,108); background-color: rgba(255,255,255,0);")
        self.initial_price.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_cadastral_number_name.setStyleSheet("color: rgb(108,108,108);background-color: rgba(255,255,255,0);")
        self.cadastral_number.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_closing_date_name.setStyleSheet("color: rgb(108,108,108); background-color: rgba(255,255,255,0);")
        self.closing_date.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

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

        self.application_form.setFont(font_7)
        self.subject_of_bidding.setFont(font_9)
        self.label_land_area_name.setFont(font_7)
        self.land_area.setFont(font_9)
        self.label_e_platform_name.setFont(font_7)
        self.e_platform.setFont(font_9)

        self.status.setFont(font_7)
        self.trade_type.setFont(font_7)
        self.label_initial_price_name.setFont(font_7)
        self.initial_price.setFont(font_9)
        self.label_cadastral_number_name.setFont(font_7)
        self.cadastral_number.setFont(font_9)
        self.label_closing_date_name.setFont(font_7)
        self.closing_date.setFont(font_9)

    def mouseReleaseEvent(self, e):
        self.signal_mouse.emit()

        print(f'Вы нажали на SmallWidget {e.button()}')


class WidgetFullOrder(WidgetOrder):
    """Предоставляет всю информацию о лоте и позволяет проводить с ним манипуляции"""
    def __init__(self, dict_lot):
        super().__init__(dict_lot)
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
    import json
    with open('dict_lot.json', 'r') as file:
        dict_lot = json.load(file)

    app = QApplication([])
    window = WidgetFullOrder(dict_lot[5])
    print(dict_lot[1])
    window.show()
    app.exec()




