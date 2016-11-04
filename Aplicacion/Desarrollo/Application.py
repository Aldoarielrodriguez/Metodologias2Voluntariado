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
        self.__appName="Aplicacion epa"
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
        self.escenarioPilas = enginepilas.iniciar_pilas(self.interface.codeAreaPilas)
        self.areaDeCodigoPilas=enginepilas.iniciar_pilas(self.interface.escenarioPilas)
        #Se inicia el Decodificador
        self.decoder = decoder.Decoder()
        #Instanciando entorno de desarrollo
        self.developmentenvironment = developmentenvironment.EnviromentDev()
        #Se inicia la aplicacion.
        self.app.exec_()
        
        
