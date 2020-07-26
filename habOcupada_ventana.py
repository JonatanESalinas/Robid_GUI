# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'habOcupada_ventana.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_habOcupada_ventana(object):
    def setupUi(self, habOcupada_ventana):
        habOcupada_ventana.setObjectName("habOcupada_ventana")
        habOcupada_ventana.resize(312, 165)
        self.aceptarBoton_ocup = QtWidgets.QPushButton(habOcupada_ventana)
        self.aceptarBoton_ocup.setGeometry(QtCore.QRect(110, 120, 75, 23))
        self.aceptarBoton_ocup.setObjectName("aceptarBoton_ocup")
        self.label = QtWidgets.QLabel(habOcupada_ventana)
        self.label.setGeometry(QtCore.QRect(20, 20, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(habOcupada_ventana)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(habOcupada_ventana)
        QtCore.QMetaObject.connectSlotsByName(habOcupada_ventana)

    def retranslateUi(self, habOcupada_ventana):
        _translate = QtCore.QCoreApplication.translate
        habOcupada_ventana.setWindowTitle(_translate("habOcupada_ventana", "Advertencia"))
        self.aceptarBoton_ocup.setText(_translate("habOcupada_ventana", "Aceptar"))
        self.label.setText(_translate("habOcupada_ventana", "Esta habitación ya está ocupada."))
        self.label_2.setText(_translate("habOcupada_ventana", "Por favor, elige otra."))
