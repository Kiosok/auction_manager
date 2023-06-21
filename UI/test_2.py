from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyWidget(QWidget):
    my_signal = pyqtSignal()

    def __init__(self):
        super().__init__()


        button = QPushButton('Click me', self)
        button.clicked.connect(self.on_button_clicked)

        vbox = QVBoxLayout()
        vbox.addWidget(button)
        self.setLayout(vbox)

    def on_button_clicked(self):
        self.my_signal.emit()


if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.my_signal.connect(lambda: print('Signal received'))
    widget.show()
    app.exec()