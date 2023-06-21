from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication


class Signal(QWidget):
    my_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        label = QLabel('Нажми и получишь результат')
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        self.setLayout(vbox)




    def mouseReleaseEvent(self, e):
        print('Test one')
        self.my_signal.emit()


if __name__ == '__main__':
    app = QApplication([])
    window = Signal()
    window.show()
    app.exec()
