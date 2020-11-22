#!/usr/bin/env python3.7
'''
    Para correr toda la interfaz:
        python interfaceBot.py
    Para cambiar de .ui a .py:
        pyuic5 nombreArchivo.ui -o nombreArchivo.py
    Para generar el archivo Imag_rc.py:
        pyrcc5 Imag.qrc -o Imag_rc.py

EDIT: Es necesario tener la developer version de PyQtGraph, se instala con:
pip install git+https://github.com/pyqtgraph/pyqtgraph.git
Debido a que pyqtgraph no funciona con Python 3.8

'''

import sys
import os
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from Pacientes_Ventana import *
from AgregaPaciente_Ventana import *
from EditarPaciente_Ventana import *
from habOcupada_ventana import *
from confirmElimin_ventana import *
from Paciente import Paciente
from Hospital import Hospital
from Recorrido import Recorrido
import datetime

ultimoSeleccionado = -1

class Ui_confirmElimin_ventana(QtWidgets.QMainWindow,Ui_confirmElimin_ventana):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.aceptar_confirmElim.clicked.connect(self.siElimina)
        self.cancelar_confirmElim.clicked.connect(self.noElimina)

    def siElimina(self):
        global ultimoSeleccionado
        ventanaPacientes.tablaPacientes.removeRow(ultimoSeleccionado)
        miHospital.eliminarUnPaciente(ultimoSeleccionado)
        ventanaPacientes.limpiaPantalla_DatosPaciente()
        ventanaPacientes.limpiaGraficas()
        ultimoSeleccionado = -1
        self.close()

    def noElimina(self):
        self.close()

class Ui_habOcupada_ventana(QtWidgets.QMainWindow,Ui_habOcupada_ventana):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.aceptarBoton_ocup.clicked.connect(self.cerrar)

    def cerrar(self):
        self.close()

class Ui_AgregaPac_ventana(QtWidgets.QMainWindow,Ui_AgregaPac_ventana):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.Aceptar_bot_agrPac.clicked.connect(self.aceptaDatos)
        self.Cancelar_bot_AgrPac.clicked.connect(self.cancelaDatos)

    def aceptaDatos(self):

        if(miHospital.verificaHabitacion(self.comboBox_Habitacion.currentText())):
            self.ventana_yaOcupada = Ui_habOcupada_ventana()
            self.ventana_yaOcupada.show()
        else:
            global nombrePaciente
            nombrePaciente = self.cajaNombre.toPlainText()
            print("Mi nombre es: " + nombrePaciente)
            habitacion = self.comboBox_Habitacion.currentText()
            print("Mi habitacion es: " + habitacion)
            diagnostico = self.cajaDiagnostico.toPlainText()
            print("Mi diagnostico es: " + diagnostico)
            alergias = self.cajaAlergias.toPlainText()
            print("Mis alergias: " + alergias)
            comentario = self.cajaComentario.toPlainText()
            print("Mi comentario es: " + comentario)
            preAlta = self.comboBox_preAlta.currentText()
            print("Mi preAlta es: " + preAlta)
            gravedad = self.checaBotonGravedad()
            print("Mi gravedad es: " + gravedad)
            print("--------------------")

            nuevoPaciente = Paciente(1, nombrePaciente, habitacion, diagnostico, alergias, comentario, preAlta, gravedad)
            miHospital.myArrayPacientes.append(nuevoPaciente)
            
            renglonPos = ventanaPacientes.tablaPacientes.rowCount()
            ventanaPacientes.tablaPacientes.insertRow(renglonPos)
            ventanaPacientes.tablaPacientes.setItem(renglonPos , 0, QtWidgets.QTableWidgetItem(nombrePaciente))
            ventanaPacientes.tablaPacientes.setItem(renglonPos , 1, QtWidgets.QTableWidgetItem(habitacion))
            ventanaPacientes.tablaPacientes.setItem(renglonPos , 2, QtWidgets.QTableWidgetItem(gravedad))
            ventanaPacientes.tablaPacientes.setItem(renglonPos , 3, QtWidgets.QTableWidgetItem(preAlta))

            self.close()


    def cancelaDatos(self):
        self.close()

    def checaBotonGravedad(self):
        if(self.radioButton_estable.isChecked()):
            return self.radioButton_estable.text()
        elif(self.radioButton_grave.isChecked()):
            return self.radioButton_grave.text()
        else:
            return self.radioButton_critico.text()


class Ui_EditarPac_ventana(QtWidgets.QMainWindow,Ui_EditarPac_ventana):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.cajaNombre.setText(miHospital.myArrayPacientes[ultimoSeleccionado].nombre)
        unIndexHab = self.comboBox_Habitacion.findText(miHospital.myArrayPacientes[ultimoSeleccionado].habitacion)
        self.comboBox_Habitacion.setCurrentIndex(unIndexHab)
        self.cajaDiagnostico.setText(miHospital.myArrayPacientes[ultimoSeleccionado].diagnostico)
        self.cajaAlergias.setText(miHospital.myArrayPacientes[ultimoSeleccionado].alergias)
        self.cajaComentario.setText(miHospital.myArrayPacientes[ultimoSeleccionado].comentario)
        self.rellenaRadioButton(miHospital.myArrayPacientes[ultimoSeleccionado].gravedad)
        unIndexPre = self.comboBox_preAlta.findText(miHospital.myArrayPacientes[ultimoSeleccionado].preAlta)
        self.comboBox_preAlta.setCurrentIndex(unIndexPre)

        print("Equis de")
        self.Aceptar_bot_agrPac.clicked.connect(self.revisaDisponibilidadHabitacion)
        self.Cancelar_bot_AgrPac.clicked.connect(self.cancelaDatos)

    def revisaDisponibilidadHabitacion(self):
        if(miHospital.verificaHabitacion(self.comboBox_Habitacion.currentText())):
            if(self.comboBox_Habitacion.currentText()==miHospital.myArrayPacientes[ultimoSeleccionado].habitacion):                
                self.aceptaDatosEditar()
            else:
                self.ventana_yaOcupada = Ui_habOcupada_ventana()
                self.ventana_yaOcupada.show()
        else:
            self.aceptaDatosEditar()
            miHospital.myArrayPacientes[ultimoSeleccionado].actualizarNombreArchivo()
        
        print("---Teoricamente el paciente fue editado---")

    def aceptaDatosEditar(self):
        global nombrePaciente
        nombrePaciente = self.cajaNombre.toPlainText()
        miHospital.myArrayPacientes[ultimoSeleccionado].nombre = nombrePaciente
        habitacion = self.comboBox_Habitacion.currentText()
        miHospital.myArrayPacientes[ultimoSeleccionado].habitacion = habitacion
        diagnostico = self.cajaDiagnostico.toPlainText()
        miHospital.myArrayPacientes[ultimoSeleccionado].diagnostico = diagnostico
        alergias = self.cajaAlergias.toPlainText()
        miHospital.myArrayPacientes[ultimoSeleccionado].alergias = alergias
        comentario = self.cajaComentario.toPlainText()
        miHospital.myArrayPacientes[ultimoSeleccionado].comentario = comentario
        preAlta = self.comboBox_preAlta.currentText()
        miHospital.myArrayPacientes[ultimoSeleccionado].preAlta = preAlta
        gravedad = self.checaBotonGravedad()
        miHospital.myArrayPacientes[ultimoSeleccionado].gravedad = gravedad            

        ventanaPacientes.tablaPacientes.setItem(ultimoSeleccionado , 0, QtWidgets.QTableWidgetItem(nombrePaciente))
        ventanaPacientes.tablaPacientes.setItem(ultimoSeleccionado , 1, QtWidgets.QTableWidgetItem(habitacion))
        ventanaPacientes.tablaPacientes.setItem(ultimoSeleccionado , 2, QtWidgets.QTableWidgetItem(gravedad))
        ventanaPacientes.tablaPacientes.setItem(ultimoSeleccionado , 3, QtWidgets.QTableWidgetItem(preAlta))
        ventanaPacientes.muestraDatos_Paciente(ultimoSeleccionado)
        self.close()

    def cancelaDatos(self):
        self.close()

    def checaBotonGravedad(self):
        if(self.radioButton_estable.isChecked()):
            return self.radioButton_estable.text()
        elif(self.radioButton_grave.isChecked()):
            return self.radioButton_grave.text()
        else:
            return self.radioButton_critico.text()

    def rellenaRadioButton(self, nivelGravedad):
        if(nivelGravedad=="Estable"):
            self.radioButton_estable.setChecked(True)
        elif(nivelGravedad=="Grave"):
            self.radioButton_grave.setChecked(True)
        else:
            self.radioButton_critico.setChecked(True)      


class Ui_PacientesVentana(QtWidgets.QMainWindow,Ui_PacientesVentana, QDialog):   #QDialog?
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.AgregPac_Boton.clicked.connect(self.AgregaPaciente)
        self.tablaPacientes.itemClicked.connect(self.item_click)
        self.EliminaPac_boton.clicked.connect(self.EliminaPaciente)
        self.EditarPac_boton.clicked.connect(self.editarPaciente)

        self.etiqueta_diagnostico.setReadOnly(True)
        self.etiqueta_alergias.setReadOnly(True)
        self.etiqueta_comentarios.setReadOnly(True)
        
        self.formatoGraficas()

    def EliminaPaciente(self):
        if(ultimoSeleccionado!= -1):
            print("Voy a eliminar al paciente en: " + str(ultimoSeleccionado))
            self.ventanaConfirmacion = Ui_confirmElimin_ventana()
            self.ventanaConfirmacion.show()

    def AgregaPaciente(self):
        self.ventana_AgregaPaciente = Ui_AgregaPac_ventana()
        self.ventana_AgregaPaciente.show()

    def item_click(self,item):
        global ultimoSeleccionado
        ultimoSeleccionado = item.row()
        print("Pruebaxd, elemento: " + str(item.row()))
        self.muestraDatos_Paciente(item.row())
        self.graficaTemperatura()
        self.graficaOxigeno()

    def muestraDatos_Paciente(self, renglon):
        self.etiqueta_nombre.setText("   " + miHospital.myArrayPacientes[renglon].nombre)
        self.etiqueta_habitacion.setText(miHospital.myArrayPacientes[renglon].habitacion)
        self.etiqueta_gravedad.setText(miHospital.myArrayPacientes[renglon].gravedad)
        self.etiqueta_preAlta.setText(miHospital.myArrayPacientes[renglon].preAlta)
        self.etiqueta_diagnostico.setReadOnly(True)
        self.etiqueta_diagnostico.setText(miHospital.myArrayPacientes[renglon].diagnostico)
        self.etiqueta_alergias.setReadOnly(True)
        self.etiqueta_alergias.setText(miHospital.myArrayPacientes[renglon].alergias)
        self.etiqueta_comentarios.setReadOnly(True)
        self.etiqueta_comentarios.setText(miHospital.myArrayPacientes[renglon].comentario)

    def limpiaPantalla_DatosPaciente(self):
        self.etiqueta_nombre.setText(" ")
        self.etiqueta_habitacion.setText(" ")
        self.etiqueta_gravedad.setText(" ")
        self.etiqueta_preAlta.setText(" ")
        self.etiqueta_diagnostico.setReadOnly(True)
        self.etiqueta_diagnostico.setText(" ")
        self.etiqueta_alergias.setReadOnly(True)
        self.etiqueta_alergias.setText(" ")
        self.etiqueta_comentarios.setReadOnly(True)
        self.etiqueta_comentarios.setText(" ")
        
    def graficaPrueba(self):
        L = [1,2,3,4,5]
        self.grafica_temperatura.plot(L)
        self.grafica_oximetria.plot(L)

    def graficaTemperatura(self):
        #global ultimoSeleccionado
        xdict = dict(enumerate(miHospital.myArrayPacientes[ultimoSeleccionado].horasTemperatura))
        stringaxis = pg.AxisItem(orientation='bottom')
        stringaxis.setTicks([xdict.items()])

        #TODO ESTE BLOQUE SE VA A MODIFICAR A LOS PARAMETROS FINALES DE LA GRAFICA (POSICION, TAMANIO FINALES)
        self.grafica_temperatura = PlotWidget(self.scrollAreaWidgetContents, axisItems={'bottom': stringaxis})
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafica_temperatura.sizePolicy().hasHeightForWidth())
        self.grafica_temperatura.setSizePolicy(sizePolicy)
        self.grafica_temperatura.setMinimumSize(QtCore.QSize(100, 150))
        self.grafica_temperatura.setObjectName("grafica_temperatura")
        self.gridLayout.addWidget(self.grafica_temperatura, 12, 0, 1, 5)
        #####################

        self.grafica_temperatura.setLabel('left', 'Temperatura', units='°C')
        self.grafica_temperatura.setLabel('bottom', 'Hora y dia', units='Hr/d')

        curve = self.grafica_temperatura.plot(list(xdict.keys()), miHospital.myArrayPacientes[ultimoSeleccionado].datosTemperatura, pen='b', symbol='x') #esto lo agregue

    def graficaOxigeno(self):
        #global ultimoSeleccionado
        zdict = dict(enumerate(miHospital.myArrayPacientes[ultimoSeleccionado].horasOximetria))
        stringaxis2 = pg.AxisItem(orientation='bottom')
        stringaxis2.setTicks([zdict.items()])

        #TODO ESTE BLOQUE SE VA A MODIFICAR A LOS PARAMETROS FINALES DE LA GRAFICA (POSICION, TAMANIO FINALES)
        self.grafica_oximetria = PlotWidget(self.scrollAreaWidgetContents, axisItems={'bottom': stringaxis2})
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafica_oximetria.sizePolicy().hasHeightForWidth())
        self.grafica_oximetria.setSizePolicy(sizePolicy)
        self.grafica_oximetria.setMinimumSize(QtCore.QSize(100, 150))
        self.grafica_oximetria.setObjectName("grafica_oximetria")
        self.gridLayout.addWidget(self.grafica_oximetria, 15, 0, 1, 5)
        #####################
        
        self.grafica_oximetria.setLabel('left', 'Saturacion de oxigeno', units='SpO2')
        self.grafica_oximetria.setLabel('bottom', 'Hora y dia', units='Hr/d')

        curve2 = self.grafica_oximetria.plot(list(zdict.keys()), miHospital.myArrayPacientes[ultimoSeleccionado].datosOximetria, pen='r', symbol='o')

    def formatoGraficas(self):
        self.grafica_temperatura.setLabel('left', 'Temperatura', units='°C')
        self.grafica_temperatura.setLabel('bottom', 'Hora y dia', units='Hr/d')
        self.grafica_oximetria.setLabel('left', 'Saturacion de oxigeno', units='SpO2')
        self.grafica_oximetria.setLabel('bottom', 'Hora y dia', units='Hr/d')

    def limpiaGraficas(self):
        self.grafica_temperatura = PlotWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafica_temperatura.sizePolicy().hasHeightForWidth())
        self.grafica_temperatura.setSizePolicy(sizePolicy)
        self.grafica_temperatura.setMinimumSize(QtCore.QSize(100, 150))
        self.grafica_temperatura.setObjectName("grafica_temperatura")
        self.gridLayout.addWidget(self.grafica_temperatura, 12, 0, 1, 5)

        self.grafica_oximetria = PlotWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafica_oximetria.sizePolicy().hasHeightForWidth())
        self.grafica_oximetria.setSizePolicy(sizePolicy)
        self.grafica_oximetria.setMinimumSize(QtCore.QSize(100, 150))
        self.grafica_oximetria.setObjectName("grafica_oximetria")
        self.gridLayout.addWidget(self.grafica_oximetria, 15, 0, 1, 5)

        self.formatoGraficas()

    def editarPaciente(self):
        if(ultimoSeleccionado!= -1):
            self.ventana_EditarPaciente = Ui_EditarPac_ventana()
            self.ventana_EditarPaciente.show()
          

def on_message(client, userdata, msg):
    #FUNCION QUE SE EJECUTE CUANDO SE RECIBA UN NUEVO DATO POR ALGUN TOPICO
    x = datetime.datetime.now()

    horaYdia = str(x.hour)+":"+str(x.minute)+"\n"+str(x.day)+"/"+str(x.month)+"/"+str(x.year)
    print(horaYdia)

if __name__ == "__main__":

    miHospital = Hospital()

    appi = QtWidgets.QApplication([])
    ventanaPacientes = Ui_PacientesVentana()

    miHospital.leerBaseDeDatosHospital(miHospital.nombreArchivoHospital, ventanaPacientes)
    miHospital.cargarDatos_TempOxi_Pacientes()
    
    ventanaPacientes.show()
    appi.exec_()

    miHospital.guardarBaseDeDatosHospital()
    miHospital.guardarDatos_TempOxi_Pacientes()

    print("Hola")