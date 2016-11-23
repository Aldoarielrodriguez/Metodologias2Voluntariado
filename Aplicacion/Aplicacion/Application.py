# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:39:38 2016

@author: joanteran
"""
import interface.interface as interface
import sys
import enginepilas.enginepilas as enginepilas
import processing.decoder as decoder
import processing.developmentenvironment as developmentenvironment
import CodigoUsuario
import Escenario
from PyQt4 import QtCore, QtGui, uic


class Application(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Application, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    def __init__(self):
        self.__extensionDeArchivos = "py"
        self.__oficialUrl = "www.google.com.ar"
        self.__appName="Trabajo Final Metodologias de Programacion 2"
    def getAppName(self):
        return self.__appName
    def getExtensionDeArchivos(self):
        return self.__extensionDeArchivos
    def getOficialURL(self):
        return self.__oficialUrl
    def launch(self):
        #Se instancia el QApplication
        self.app = QtGui.QApplication(sys.argv)
        #Se instancia e inicia nuestra Interface Grafica
        self.interface =  interface.UserInterface()
        self.interface.show()
        #Se inicia el motor pilas y se le pasa la interface por parametro, para que lo incruste.
        self.escenarioPilas = enginepilas.iniciar_pilas(self.interface.escenarioPilas,[800,800])
        self.areaDeCodigoPilas=enginepilas.iniciar_pilas(self.interface.codeAreaPilas,[800,640])
        self.iniciarAreaDeCodigo()
        self.iniciarEscenario()
        #Se inicia el Decodificador
        self.decoder = decoder.Decoder()
        #Instanciando entorno de desarrollo
        self.developmentenvironment = developmentenvironment.EnviromentDev()
        #Se inicia la aplicacion.
        self.app.exec_()
    def iniciarAreaDeCodigo(self):
        self.iniciarEjemplo()
    def iniciarEjemplo(self):
        contexto=CodigoUsuario.Contexto()

        self.areaDeCodigoPilas.colisiones.agregar(contexto.getTodosLosCodigos(), contexto.getTodosLosCodigos(),contexto.engancharCodigos)
        self.areaDeCodigoPilas.fondos.Fondo('images/background.jpg')
    def iniciarEscenario(self):
        mapa = self.escenarioPilas.actores.MapaTiled("mapas/test.tmx")
        colectivo=Escenario.Vehiculo(self.escenarioPilas)
        persona=Escenario.Persona(self.escenarioPilas)
        persona.x=200
        senialDeTransito=Escenario.SenialBus(self.escenarioPilas)
        senialDeTransito.y=200
        paradaIzq=Escenario.Parada(self.escenarioPilas)
        paradaIzq.x=-100
        paradaIzq.setToLeft()
        paradaDer=Escenario.Parada(self.escenarioPilas)
        paradaDer.x=100
        paradaDer.setToRight()
        paradaArr=Escenario.Parada(self.escenarioPilas)
        paradaArr.y=100
        paradaArr.setToUp()
        paradaAba=Escenario.Parada(self.escenarioPilas)
        paradaAba.y=-100
        paradaAba.setToDown()

