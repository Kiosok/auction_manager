import os
import sys
from PyQt6.QtWidgets import *
from pprint import pprint

# Прописываем адрес к папке
sys.path.append(rf"G:\Documents\Python\game\auction_manager\UI")
# На уровень выше
sys.path.append(os.path.join(os.getcwd(), '..'))

from UI.main_ui import MainWindow


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()



