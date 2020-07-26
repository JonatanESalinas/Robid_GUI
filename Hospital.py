#!/usr/bin/env python

class Hospital:
	def __init__(self):
		self.myArrayPacientes = list()
		self.arrayRecorridos = list()

	def eliminarUnPaciente(self, posicion):
		del self.myArrayPacientes[posicion]