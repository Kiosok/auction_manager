from PyQt6.QtWidgets import *
from widget_btn_status import BtnS
from widget_order import WidgetFullOrder
from widget_order import WidgetSmallOrder

from smoll_ui import Ui_Form


class MainWindow(QMainWindow):
    """Главное окно"""

    def __init__(self):

        super().__init__()
        # Размер начального окна
        self.setMinimumSize(900, 900)

        """Левая часть приложения"""
        # Скрол панель и её расположение.
        scroll_main_left = QScrollArea()
        layout_main_left = QVBoxLayout()
        layout_main_left.addWidget(scroll_main_left)
        widget_main_left = QWidget()
        widget_main_left.setLayout(layout_main_left)
        # Вложение в скрол панель
        widget_small_orders = QWidget()
        vbox = QVBoxLayout()

        small_order = WidgetSmallOrder()
        small_order_1 = WidgetSmallOrder()
        small_order_2 = WidgetSmallOrder()

        vbox.addWidget(small_order)
        vbox.addWidget(small_order_1)
        vbox.addWidget(small_order_2)

        widget_small_orders.setLayout(vbox)

        scroll_main_left.setWidget(widget_small_orders)

        """Правая часть приложения"""
        # Скрол панель и её расположение.
        scroll_main_rigt = QScrollArea()
        layout_main_rigt = QVBoxLayout()
        layout_main_rigt.addWidget(scroll_main_rigt)
        widget_main_rigt = QWidget()
        widget_main_rigt.setLayout(layout_main_rigt)
        # Вложение в скрол панель
        widget_full_orders = QWidget()
        # Задаю минимальный размер выджета
        widget_full_orders.setMinimumSize(600, 600)

        self.vbox_r = QVBoxLayout()
        btn_status = BtnS()
        btn_status.setMaximumHeight(44)
        self.vbox_r.addWidget(btn_status)
        widget_full_orders.setLayout(self.vbox_r)
        scroll_main_rigt.setWidget(widget_full_orders)

        """Нижний слой связывающий обе части"""
        widget_main = QWidget()
        layout_main = QHBoxLayout()
        layout_main.addWidget(widget_main_left)
        layout_main.addWidget(widget_main_rigt)
        widget_main.setLayout(layout_main)

        self.setCentralWidget(widget_main)

        # Сигнал с widget order. Иполняется после клика по нему.
        small_order.signal_mouse.connect(lambda :self.add_full_widget())
        small_order_1.signal_mouse.connect(lambda: self.add_full_widget())

    def add_full_widget(self):

        print('Виджет добален')
        full_order = WidgetFullOrder()
        self.vbox_r.addWidget(full_order)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
