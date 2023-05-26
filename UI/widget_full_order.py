from PyQt6.QtWidgets import *


class WidgetFullOrder(QWidget):
    """Предоставляет всю информацию о лоте и позволяет проводить с ним манипуляции"""
    def __init__(self):
        super().__init__()
        layout_full_order = QVBoxLayout()
        label = QLabel('Тут будет вся информация о лоте')
        layout_full_order.addWidget(label)

        self.setLayout(layout_full_order)


if __name__ == '__main__':
    app = QApplication([])
    window = WidgetFullOrder()
    window.show()
    app.exec()
