import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Click me', self)
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print('Button clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())