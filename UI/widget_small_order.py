from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class WidgetsSmallOrder(QWidget):
    """Предоставляет краткую информацию о лоте и позволяет проводить с ним манипуляции"""
    def __init__(self):
        super().__init__()
        # Инициализируем label
        self.label_application_form = QLabel("Электронный аукцион")
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

        # Располагаем label по сетке
        layout_small_order = QGridLayout()
        layout_small_order.addWidget(self.label_application_form, 0, 0, 1, 1)
        layout_small_order.addWidget(self.label_subject_of_bidding, 1, 0, 3, 1)
        layout_small_order.addWidget(self.label_land_area_name, 4, 0, 1, 1)
        layout_small_order.addWidget(self.label_land_area, 5, 0, 1, 1)
        layout_small_order.addWidget(self.label_e_platform_name, 6, 0, 1, 1)
        layout_small_order.addWidget(self.label_e_platform, 7, 0, 1, 1)

        layout_small_order.addWidget(self.label_status, 0, 1, 1, 1)
        layout_small_order.addWidget(self.label_trade_type, 1, 1, 1, 1)
        layout_small_order.addWidget(self.label_initial_price_name, 2, 1, 1, 1)
        layout_small_order.addWidget(self.label_initial_price, 3, 1, 1, 1)
        layout_small_order.addWidget(self.label_cadastral_number_name, 4, 1, 1, 1)
        layout_small_order.addWidget(self.label_cadastral_number, 5, 1, 1, 1)
        layout_small_order.addWidget(self.label_closing_date_name, 6, 1, 1, 1)
        layout_small_order.addWidget(self.label_closing_date, 7, 1, 1, 1)

        self.setLayout(layout_small_order)

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

        # Задаём размеры Label
        font_7 = QFont()
        font_7.setPointSize(7)
        font_9 = QFont()
        font_9.setPointSize(9)

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
        print(f'Вы нажали на SmallWidget {e.button()}')


class WidgetFullOrder(WidgetsSmallOrder):
    """Предоставляет всю информацию о лоте и позволяет проводить с ним манипуляции"""
    def __init__(self):
        super().__init__()
        pass


if __name__ == '__main__':
    app = QApplication([])
    window = WidgetFullOrder()
    window.show()
    app.exec()




