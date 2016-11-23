#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Convierte temperaturas
# www.pythondiario.com
 
import sys
from PyQt4 import QtCore, QtGui, uic
import pilasengine


def iniciar_pilas(contenedor,tamanio=[640,640]):
	pilas = pilasengine.iniciar(tamanio[0],tamanio[1])
	pilas.definir_iniciado_desde_asistente(True)
	scope = {'pilas': pilas,'self': None, 'colores': pilasengine.colores,'pilasengine': pilasengine}
	contenedor.addWidget(scope['pilas'].widget)
	return pilas

 
