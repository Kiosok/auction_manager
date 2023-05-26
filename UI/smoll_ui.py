# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Smoll_Widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(447, 177)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_initial_price_name = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_initial_price_name.setFont(font)
        self.label_initial_price_name.setStyleSheet("color: rgb(108, 108, 108);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_initial_price_name.setObjectName("label_initial_price_name")
        self.gridLayout.addWidget(self.label_initial_price_name, 2, 5, 1, 1)
        self.label_trade_type = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_trade_type.setFont(font)
        self.label_trade_type.setStyleSheet("color: rgb(108, 108, 108);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_trade_type.setObjectName("label_trade_type")
        self.gridLayout.addWidget(self.label_trade_type, 1, 5, 1, 1)
        self.label_land_area_name = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_land_area_name.setFont(font)
        self.label_land_area_name.setStyleSheet("color: rgb(108, 108, 108);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_land_area_name.setObjectName("label_land_area_name")
        self.gridLayout.addWidget(self.label_land_area_name, 4, 0, 1, 1)
        self.label_land_area = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_land_area.setFont(font)
        self.label_land_area.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_land_area.setObjectName("label_land_area")
        self.gridLayout.addWidget(self.label_land_area, 5, 0, 1, 1)
        self.label_e_platform_name = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_e_platform_name.setFont(font)
        self.label_e_platform_name.setStyleSheet("color: rgb(108, 108, 108);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_e_platform_name.setObjectName("label_e_platform_name")
        self.gridLayout.addWidget(self.label_e_platform_name, 6, 0, 1, 1)
        self.label_e_platform = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_e_platform.setFont(font)
        self.label_e_platform.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_e_platform.setObjectName("label_e_platform")
        self.gridLayout.addWidget(self.label_e_platform, 7, 0, 1, 1)
        self.label_application_form = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_application_form.setFont(font)
        self.label_application_form.setStyleSheet("color: rgb(108, 108, 108);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_application_form.setObjectName("label_application_form")
        self.gridLayout.addWidget(self.label_application_form, 0, 0, 1, 1)
        self.label_subject_of_bidding = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_subject_of_bidding.setFont(font)
        self.label_subject_of_bidding.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_subject_of_bidding.setObjectName("label_subject_of_bidding")
        self.gridLayout.addWidget(self.label_subject_of_bidding, 1, 0, 3, 1)
        self.label_initial_price = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_initial_price.setFont(font)
        self.label_initial_price.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_initial_price.setObjectName("label_initial_price")
        self.gridLayout.addWidget(self.label_initial_price, 3, 5, 1, 1)
        self.label_closing_date = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_closing_date.setFont(font)
        self.label_closing_date.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_closing_date.setObjectName("label_closing_date")
        self.gridLayout.addWidget(self.label_closing_date, 7, 5, 1, 1)
        self.label_closing_date_name = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_closing_date_name.setFont(font)
        self.label_closing_date_name.setStyleSheet("color: rgb(108, 108, 108);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_closing_date_name.setObjectName("label_closing_date_name")
        self.gridLayout.addWidget(self.label_closing_date_name, 6, 5, 1, 1)
        self.label_cadastral_number_name = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_cadastral_number_name.setFont(font)
        self.label_cadastral_number_name.setStyleSheet("color: rgb(108, 108, 108);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_cadastral_number_name.setObjectName("label_cadastral_number_name")
        self.gridLayout.addWidget(self.label_cadastral_number_name, 4, 5, 1, 1)
        self.label_cadastral_number = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_cadastral_number.setFont(font)
        self.label_cadastral_number.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_cadastral_number.setObjectName("label_cadastral_number")
        self.gridLayout.addWidget(self.label_cadastral_number, 5, 5, 1, 1)
        self.label_status = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(60, 54, 255);")
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 0, 5, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_initial_price_name.setText(_translate("Form", "Начальная цена"))
        self.label_trade_type.setText(_translate("Form", "Аренда и продажа земельных участков"))
        self.label_land_area_name.setText(_translate("Form", "Площадь земельного участка:"))
        self.label_land_area.setText(_translate("Form", "3 465 005 кв.м."))
        self.label_e_platform_name.setText(_translate("Form", "Электронная площадка"))
        self.label_e_platform.setText(_translate("Form", "РТС-тендер"))
        self.label_application_form.setText(_translate("Form", "Электронный аукцион"))
        self.label_subject_of_bidding.setText(_translate("Form", "Земельный участок в кадастровым \n"
"номером 42:07:0110001:385, \n"
"площадью 3465005 кв.м."))
        self.label_initial_price.setText(_translate("Form", "255 717, 37 Р"))
        self.label_closing_date.setText(_translate("Form", "08.06.2023 17:00 (MCK+4)"))
        self.label_closing_date_name.setText(_translate("Form", "Дата и время окончания подачи заявок"))
        self.label_cadastral_number_name.setText(_translate("Form", "Кадастровый номер земельного участка:"))
        self.label_cadastral_number.setText(_translate("Form", "42:07:0110001:385"))
        self.label_status.setText(_translate("Form", "Прием заявок"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())