from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class WidgetsSmallOrder(QWidget):
    """Предоставляет краткую информацию о лоте и позволяет проводить с ним манипуляции"""
    def __init__(self):
        super().__init__()
        # Инициализируем label для вывода данных.
        label_application_form = QLabel("Электронный аукцион")


        # Располагаем label по сетке
        self.layout_small_order = QGridLayout()
        self.layout_small_order.addWidget(label_application_form, 0, 0, 1, 1)

        self.setLayout(self.layout_small_order)

        # Форматируем label, шрифт/размер
        label_application_form.setStyleSheet("color: rgb(60, 54, 255); background-color: rgba(255, 255, 255, 0);")

        # Задаём размеры Label
        font_7 = QFont()
        font_7.setPointSize(7)

        label_application_form.setFont(font_7)

    def mouseReleaseEvent(self, e):

        print(f'Вы нажали на SmallWidget {e.button()}')


class FullWidget(WidgetsSmallOrder):
    def __init__(self):
        super().__init__()






if __name__ == '__main__':
    app = QApplication([])
    window = WidgetsSmallOrder()
    window.show()
    app.exec()




