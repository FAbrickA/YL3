# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 440)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 121, 31))
        self.label.setObjectName("label")
        self.line_edit_sort = QtWidgets.QLineEdit(Dialog)
        self.line_edit_sort.setGeometry(QtCore.QRect(150, 50, 311, 31))
        self.line_edit_sort.setObjectName("line_edit_sort")
        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setGeometry(QtCore.QRect(0, 9, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_title.setFont(font)
        self.label_title.setText("")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.label_2.setObjectName("label_2")
        self.line_edit_roast = QtWidgets.QLineEdit(Dialog)
        self.line_edit_roast.setGeometry(QtCore.QRect(150, 100, 311, 31))
        self.line_edit_roast.setObjectName("line_edit_roast")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 190, 481, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.text_edit_description = QtWidgets.QTextEdit(Dialog)
        self.text_edit_description.setGeometry(QtCore.QRect(20, 220, 441, 141))
        self.text_edit_description.setObjectName("text_edit_description")
        self.checkbox_ground = QtWidgets.QCheckBox(Dialog)
        self.checkbox_ground.setGeometry(QtCore.QRect(20, 150, 81, 21))
        self.checkbox_ground.setObjectName("checkbox_ground")
        self.spin_price = QtWidgets.QSpinBox(Dialog)
        self.spin_price.setGeometry(QtCore.QRect(190, 150, 91, 21))
        self.spin_price.setMaximum(999999)
        self.spin_price.setObjectName("spin_price")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(140, 150, 41, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(310, 150, 51, 21))
        self.label_5.setObjectName("label_5")
        self.spin_size = QtWidgets.QSpinBox(Dialog)
        self.spin_size.setGeometry(QtCore.QRect(370, 150, 91, 21))
        self.spin_size.setMaximum(9999999)
        self.spin_size.setObjectName("spin_size")
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setGeometry(QtCore.QRect(50, 390, 151, 31))
        self.button_ok.setObjectName("button_ok")
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        self.button_cancel.setGeometry(QtCore.QRect(270, 390, 151, 31))
        self.button_cancel.setObjectName("button_cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Сорт"))
        self.label_2.setText(_translate("Dialog", "Обжарка"))
        self.label_3.setText(_translate("Dialog", "Описание"))
        self.checkbox_ground.setText(_translate("Dialog", "Молотый"))
        self.label_4.setText(_translate("Dialog", "Цена"))
        self.label_5.setText(_translate("Dialog", "Размер"))
        self.button_ok.setText(_translate("Dialog", "Ок"))
        self.button_cancel.setText(_translate("Dialog", "Отмена"))
