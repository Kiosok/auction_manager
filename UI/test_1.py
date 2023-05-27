from PyQt6.QtWidgets import *
from widget_btn_status import BtnS
from test_2 import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

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

        small_order = WidgetsSmallOrder()

        vbox.addWidget(small_order)

        widget_small_orders.setLayout(vbox)

        scroll_main_left.setWidget(widget_small_orders)


        """Правая часть приложения"""
        # Кнопки статусов и скрол панель для просмотра развернутого лота
        self.widget_main_right = QWidget()
        self.layout_main_right = QVBoxLayout()
        # Размещение Full Виджета
        self.full_order = FullWidget()
        self.full_order.-*


        """Нижний слой связывающий обе части"""
        widget_main = QWidget()
        self.layout_main = QHBoxLayout()
        self.layout_main.addWidget(widget_main_left)

        widget_main.setLayout(self.layout_main)


        self.setCentralWidget(widget_main)

    def add_full_order(self, e):


        self.layout_main_right.addWidget(self.full_order)
        self.widget_main_right.setLayout(self.layout_main_right)
        self.layout_main.addWidget(self.widget_main_right)




if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
