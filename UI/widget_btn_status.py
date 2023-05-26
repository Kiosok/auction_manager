from PyQt6.QtWidgets import *


class BtnS(QWidget):
    """Кнопки статусов"""
    def __init__(self):
        super().__init__()
        btn_new = QPushButton('Новые')
        btn_on_approval = QPushButton('На согласовании')
        btn_in_the_work = QPushButton('В работе')
        btn_finished = QPushButton('Завершенные')
        btn_not_participating = QPushButton('Не участвуем')
        btn_archive = QPushButton('Архив')

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_new)
        btn_layout.addWidget(btn_on_approval)
        btn_layout.addWidget(btn_in_the_work)
        btn_layout.addWidget(btn_finished)
        btn_layout.addWidget(btn_not_participating)
        btn_layout.addWidget(btn_archive)

        self.setLayout(btn_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = BtnS()
    window.show()
    app.exec()