#!/usr/bin/env python
import os

class Paciente:
	def __init__(self, idNum, nombre, habitacion, diagnostico, alergias, comentario, preAlta, gravedad):
		self.id = idNum
		self.nombre = nombre
		self.habitacion = habitacion
		self.diagnostico = diagnostico
		self.alergias = alergias
		self.comentario = comentario
		self.preAlta = preAlta
		self.gravedad = gravedad
		#self.datosTemperatura = [35,34,32,33,35]
		#self.horasTemperatura = ['13:30\n02/06/20', '17:30\n02/06/20', '20:00\n02/06/20', '08:00\n03/06/20', '12:00\n03/06/20']
		#self.datosOximetria = [100, 95, 98, 94, 97]
		#self.horasOximetria = ['13:30\n02/06/20', '17:30\n02/06/20', '20:00\n02/06/20', '08:00\n03/06/20', '12:00\n03/06/20']
		self.datosTemperatura = list()
		self.horasTemperatura = list()
		self.datosOximetria = list()
		self.horasOximetria = list()

		self.nombreArchivo = str(idNum) + '-' + nombre + '-' + habitacion + '.txt'

	def imprimir(self):
		print("  Nombre: " + self.nombre)
		print("  Habitacion: " + str(self.habitacion))
		print("  Comentario: " + self.comentario)

	def modificarString_quitaEnter(self, stringHoras):
		nuevoString = ''
		longi = len(stringHoras)

		for i in range(0, longi):
			if stringHoras[i] != '\n':
				nuevoString = nuevoString + stringHoras[i]
			else:
				nuevoString = nuevoString + ' '

		return nuevoString

	def modificarString_agregaEnter(self, stringHoras):
		nuevoString = ''
		longi = len(stringHoras)

		for i in range(0, longi):
			if stringHoras[i] != ' ':
				nuevoString = nuevoString + stringHoras[i]
			else:
				nuevoString = nuevoString + '\n'

		return nuevoString

	def actualizarNombreArchivo(self):
		os.rename(self.nombreArchivo,str(self.id) + '-' + self.nombre + '-' + self.habitacion + '.txt')
		self.nombreArchivo = str(self.id) + '-' + self.nombre + '-' + self.habitacion + '.txt'

#if __name__ == "__main__":

	#unPaciente = Paciente(1, "Jona", "501", "xd", "alergias", "comentario", "No", "Grave")

	#pruebaString = '13:30\n02/06/20'

	#resultado = unPaciente.modificarString_quitaEnter(pruebaString)

	#print("pruebaString: " + pruebaString)
	#print("resultado: " + resultado)

	#nuevoRes = unPaciente.modificarString_agregaEnter(resultado)
	#print("nuevoRes: " + nuevoRes)
