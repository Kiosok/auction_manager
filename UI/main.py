from PyQt6.QtWidgets import *
from widget_btn_status import BtnS
from widget_full_order import WidgetFullOrder
from widget_small_order import WidgetsSmallOrder

from smoll_ui import Ui_Form


class MainWindow(QMainWindow):
    """Главное окно"""

    def __init__(self):
        super().__init__()

        """Левая часть приложения """
        # Скрол панель и её расположение.
        scroll_main_left = QScrollArea()
        layout_main_left = QVBoxLayout()
        layout_main_left.addWidget(scroll_main_left)
        widget_main_left = QWidget()
        widget_main_left.setLayout(layout_main_left)
        # Вложение в скрол панель
        widget_small_orders = QWidget()
        vbox = QVBoxLayout()

        small_order = WidgetsSmallOrder()
        small_order_1 = WidgetsSmallOrder()
        small_order_2 = WidgetsSmallOrder()

        vbox.addWidget(small_order)
        vbox.addWidget(small_order_1)
        vbox.addWidget(small_order_2)

        widget_small_orders.setLayout(vbox)

        scroll_main_left.setWidget(widget_small_orders)


        """Правая часть приложения"""
        # Кнопки статусов и скрол панель для просмотра развернутого лота
        widget_main_right = QWidget()
        layout_main_right = QVBoxLayout()
        btn_status = BtnS()
        full_order = WidgetFullOrder()
        layout_main_right.addWidget(btn_status)
        layout_main_right.addWidget(full_order)
        widget_main_right.setLayout(layout_main_right)

        """Нижний слой связывающий обе части"""
        widget_main = QWidget()
        layout_main = QHBoxLayout()
        layout_main.addWidget(widget_main_left)
        layout_main.addWidget(widget_main_right)
        widget_main.setLayout(layout_main)


        self.setCentralWidget(widget_main)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
