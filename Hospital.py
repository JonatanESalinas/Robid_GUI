#!/usr/bin/env python
import csv
from Paciente import Paciente
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem

class Hospital:
    def __init__(self):
        self.myArrayPacientes = list()
        self.arrayRecorridos = list()
        self.nombreArchivoHospital = 'base_de_datos_Hospital.txt'

    def eliminarUnPaciente(self, posicion):
        del self.myArrayPacientes[posicion]

    def leerBaseDeDatosHospital(self, archivoHospital, miVentana):
        try:
            with open(archivoHospital) as miArchivo_csv:
                lector_csv = csv.reader(miArchivo_csv, delimiter='|')
                contadorLinea = 0
                for renglon in lector_csv:
                    if contadorLinea == 0:
                        contadorLinea += 1
                    else:
                        nombrePaciente = renglon[0]
                        habitacion = renglon[1]
                        gravedad = renglon[2]
                        preAlta = renglon[3]
                        diagnostico = renglon[4]
                        alergias = renglon[5]
                        comentario = renglon[6]

                        nuevoPaciente = Paciente(1, nombrePaciente, habitacion, diagnostico, alergias, comentario, preAlta, gravedad)
                        self.myArrayPacientes.append(nuevoPaciente)
                        
                        renglonPos = miVentana.tablaPacientes.rowCount()
                        miVentana.tablaPacientes.insertRow(renglonPos)
                        miVentana.tablaPacientes.setItem(renglonPos , 0, QTableWidgetItem(nombrePaciente))
                        miVentana.tablaPacientes.setItem(renglonPos , 1, QTableWidgetItem(habitacion))
                        miVentana.tablaPacientes.setItem(renglonPos , 2, QTableWidgetItem(gravedad))
                        miVentana.tablaPacientes.setItem(renglonPos , 3, QTableWidgetItem(preAlta))
                        contadorLinea += 1

                print("Ya acabe de cargar los datos de los pacientes.")
        except FileNotFoundError:
            print("No encontre el archivo...")

    def guardarBaseDeDatosHospital(self):
        try:
            with open(self.nombreArchivoHospital, mode='w', newline='') as miArchivo_csv:
                escritor_csv = csv.writer(miArchivo_csv, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                escritor_csv.writerow(['Nombre', 'Habitacion', 'Gravedad', 'PreAlta', 'Diagnostico', 'Alergias', 'Comentarios', 'nombreArchivo'])

                length = len(self.myArrayPacientes)

                for i in range(length):
                    escritor_csv.writerow([self.myArrayPacientes[i].nombre, self.myArrayPacientes[i].habitacion, self.myArrayPacientes[i].gravedad, self.myArrayPacientes[i].preAlta, self.myArrayPacientes[i].diagnostico, self.myArrayPacientes[i].alergias, self.myArrayPacientes[i].comentario, self.myArrayPacientes[i].nombreArchivo])

            print("Termine de escribir el archivo teoricamente")
        except:
            print("Algo salio mal")

    def guardarDatos_TempOxi_Pacientes(self):
        try:
            length = len(self.myArrayPacientes)
            
            for i in range(length):

                with open(self.myArrayPacientes[i].nombreArchivo, mode='w', newline='') as myDataFile_csv:
                    escritor_csv = csv.writer(myDataFile_csv, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    escritor_csv.writerow(['Tipo Medicion', 'Hora/Dia', 'Valor'])

                    cantidadDatosTemp = len(self.myArrayPacientes[i].datosTemperatura)

                    for y in range(cantidadDatosTemp):
                        horaSinEnter = self.myArrayPacientes[i].modificarString_quitaEnter(self.myArrayPacientes[i].horasTemperatura[y])
                        escritor_csv.writerow(['Temperatura', horaSinEnter, self.myArrayPacientes[i].datosTemperatura[y]])

                    cantidadDatosOxi = len(self.myArrayPacientes[i].datosOximetria)

                    for y in range(cantidadDatosOxi):
                        horaSinEnter = self.myArrayPacientes[i].modificarString_quitaEnter(self.myArrayPacientes[i].horasOximetria[y])
                        escritor_csv.writerow(['Oximetria', horaSinEnter, self.myArrayPacientes[i].datosOximetria[y]])                        

            print("Termine de escribir los archivos de datos de los pacientes")            
        except:
            print("Hubo un error")

    def cargarDatos_TempOxi_Pacientes(self):
        try:
            length = len(self.myArrayPacientes)
            
            for i in range(length):
                with open(self.myArrayPacientes[i].nombreArchivo) as myDataFile_csv:
                    lector_csv = csv.reader(myDataFile_csv, delimiter='|')
                    contadorLinea = 0
                    #print("nombreArchivo: " + self.myArrayPacientes[i].nombreArchivo)
                    for renglon in lector_csv:
                        if contadorLinea == 0:
                            contadorLinea += 1
                        else:
                            tipoMedicion = renglon[0]
                            horaFecha = self.myArrayPacientes[i].modificarString_agregaEnter(renglon[1])
                            valorDato = int(renglon[2])
                            
                            if tipoMedicion == "Temperatura":
                                self.myArrayPacientes[i].horasTemperatura.append(horaFecha)
                                self.myArrayPacientes[i].datosTemperatura.append(valorDato)
                            else:
                                self.myArrayPacientes[i].horasOximetria.append(horaFecha)
                                self.myArrayPacientes[i].datosOximetria.append(valorDato)
                            
                            contadorLinea += 1
            
            print("Ya acabe de cargar los datos oxi temp de los pacientes.")
        except FileNotFoundError:
            print("No encontre el archivo de un paciente...")   

    def verificaHabitacion(self, habSeleccionada):
        length = len(self.myArrayPacientes)
        for i in range(length):
            if(self.myArrayPacientes[i].habitacion==habSeleccionada):
                return True

        return False

if __name__ == "__main__":
    unHospital = Hospital()
    print("Alo")
##agradecimientos: Dinosoft Flat icons