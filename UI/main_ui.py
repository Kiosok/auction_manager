from PyQt6.QtWidgets import *
from widget_btn_status import BtnS
from widget_order import WidgetFullOrder
from widget_order import WidgetOrder


class MainWindow(QMainWindow):
    """Главное окно"""

    def __init__(self):

        super().__init__()
        # Размер начального окна
        self.setMinimumSize(900, 300)

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

        # Создание виджетов
        import json
        with open('dict_lot.json', 'r') as file:
            dict_lot = json.load(file)
            for lot in dict_lot:
                small_order = WidgetOrder(lot)
                vbox.addWidget(small_order)

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
        # Задаю минимальный размер виджета
        widget_full_orders.setMinimumSize(600, 800)
        # в self.vbox можно вложить любой виджет что нужен в правом скроле
        self.vbox_r = QVBoxLayout()
        widget_full_orders.setLayout(self.vbox_r)
        scroll_main_rigt.setWidget(widget_full_orders)

        """Нижний слой связывающий обе части"""
        btn_status = BtnS()

        widget_main = QWidget()
        layout_main = QGridLayout()
        layout_main.addWidget(btn_status, 1, 0, 1, 2)
        layout_main.addWidget(widget_main_left)
        layout_main.addWidget(widget_main_rigt)
        widget_main.setLayout(layout_main)

        self.setCentralWidget(widget_main)

        # Сигнал с widget order. Исполняется после клика по нему.
        small_order.signal_mouse.connect(lambda: self.add_full_widget())

    def clear_layout(self, layout):
        """Очистка layout от всех виджетов """
        while layout.count():
            widget = layout.takeAt(0).widget()
            widget.deleteLater()

    def add_full_widget(self):
        self.clear_layout(self.vbox_r)

        print('Виджет добавлен')
        full_order = WidgetFullOrder()
        self.vbox_r.addWidget(full_order)



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
