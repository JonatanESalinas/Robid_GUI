# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmElimin_ventana.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_confirmElimin_ventana(object):
    def setupUi(self, confirmElimin_ventana):
        confirmElimin_ventana.setObjectName("confirmElimin_ventana")
        confirmElimin_ventana.resize(392, 132)
        self.aceptar_confirmElim = QtWidgets.QPushButton(confirmElimin_ventana)
        self.aceptar_confirmElim.setGeometry(QtCore.QRect(200, 90, 75, 23))
        self.aceptar_confirmElim.setObjectName("aceptar_confirmElim")
        self.cancelar_confirmElim = QtWidgets.QPushButton(confirmElimin_ventana)
        self.cancelar_confirmElim.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.cancelar_confirmElim.setObjectName("cancelar_confirmElim")
        self.label = QtWidgets.QLabel(confirmElimin_ventana)
        self.label.setGeometry(QtCore.QRect(40, 20, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(confirmElimin_ventana)
        QtCore.QMetaObject.connectSlotsByName(confirmElimin_ventana)

    def retranslateUi(self, confirmElimin_ventana):
        _translate = QtCore.QCoreApplication.translate
        confirmElimin_ventana.setWindowTitle(_translate("confirmElimin_ventana", "Confirmación de eliminar paciente"))
        self.aceptar_confirmElim.setText(_translate("confirmElimin_ventana", "Aceptar"))
        self.cancelar_confirmElim.setText(_translate("confirmElimin_ventana", "Cancelar"))
        self.label.setText(_translate("confirmElimin_ventana", "¿Confirma que desea eliminar a este paciente?"))
