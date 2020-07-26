#!/usr/bin/env python

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
		self.datosTemperatura = [35,34,32,33,35]
		self.horasTemperatura = ['13:30\n02/06/20', '17:30\n02/06/20', '20:00\n02/06/20', '08:00\n03/06/20', '12:00\n03/06/20']
		self.datosOximetria = [100, 95, 98, 94, 97]
		self.horasOximetria = ['13:30\n02/06/20', '17:30\n02/06/20', '20:00\n02/06/20', '08:00\n03/06/20', '12:00\n03/06/20']

		self.nombreArchivo = str(idNum) + "-" + nombre + "-" + habitacion + ".txt"

	def imprimir():
		print("  Nombre: " + self.nombre)
		print("  Habitacion: " + str(self.habitacion))
		print("  Comentario: " + self.comentario)