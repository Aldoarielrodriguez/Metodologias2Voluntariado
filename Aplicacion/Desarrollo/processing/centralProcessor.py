# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:39:38 2016

@author: joanteran
"""


class CentralProcessor():
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CentralProcessor, cls).__new__(cls, *args, **kwargs)
        return cls._instance 
    def __init__(self, userInterface):
        print("Creando Procesador")
        self.userInterface = userInterface
    def pausarPrograma(self):
        print("pausar Programa")
    def pararPrograma(self):
        print("Parar Programa")
    def ejecutarPrograma(self):
        print("ejecutar Programa")
    def reiniciarPrograma(self):
        print("reiniciar Programa")
    def ejecutarLento(self):
        print("Ejecutando lento")
    def ejecutarRapido(self):
        print("Ejecutando Rapido")