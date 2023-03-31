from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    """Пример создания структуры с классам. Сперва создается основное окно, а потом
    дополнительные кнопки на нем, текстбоксыы и остальное """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Main Window')

        self.button = QPushButton('Open Dialog', self)
        self.button.move(50, 50)
        self.button.clicked.connect(self.openDialog)

    def openDialog(self):
        dialog = Dialog(self)
        dialog.exec_()

class Dialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle('Dialog')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()