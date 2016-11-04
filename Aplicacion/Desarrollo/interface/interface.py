# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:39:38 2016

@author: joanteran
"""
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
import processing.entity
import Application
import processing.centralProcessor
import webbrowser


main_form_class = uic.loadUiType("Main.ui")[0]
confirm_form_class = uic.loadUiType("Main.ui")[0]
class UserInterface(QtGui.QMainWindow, main_form_class):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(UserInterface, cls).__new__(cls, *args, **kwargs)
        return cls._instance 
    def __init__(self, parent=None):
       QtGui.QMainWindow.__init__(self, parent)
       self.__archivoActual=processing.entity.Archivo()
       self.procesador = processing.centralProcessor.CentralProcessor(self)
       self.actionsPerform = GUIActions(self, self.procesador)
       self.setupUi(self)
       self.pausarBtn.clicked.connect(self.actionsPerform.pausarActionPerform)
       self.pararBtn.clicked.connect(self.actionsPerform.pararActionPerform)
       self.ejecutarBtn.clicked.connect(self.actionsPerform.ejecutarActionPerform)
       self.reiniciarBtn.clicked.connect(self.actionsPerform.reiniciarActionPerform)
       #
       """self.actionNuevo.triggered.connect(self.actionsPerform.nuevoActionPerform)
       self.actionAbrir.triggered.connect(self.actionsPerform.abrirActionPerform)
       self.actionGuardar.triggered.connect(self.actionsPerform.guardarActionPerform)
       self.actionGuardarComo.triggered.connect(self.actionsPerform.guardarComoActionPerform)
       #
       self.actionCortar.triggered.connect(self.actionsPerform.cortarActionPerform)
       self.actionCopiar.triggered.connect(self.actionsPerform.copiarActionPerform)
       self.actionPegar.triggered.connect(self.actionsPerform.pegarActionPerform)
       self.actionDeshacer.triggered.connect(self.actionsPerform.deshacerActionPerform)
       self.actionRehacer.triggered.connect(self.actionsPerform.rehacerActionPerform)
       self.actionLimpiarAreaDeCodigo.triggered.connect(self.actionsPerform.limpiarAreaDeCodigoActionPerform)"""
       #
       self.actionEjecutar.triggered.connect(self.actionsPerform.ejecutarActionPerform)
       self.actionPausar.triggered.connect(self.actionsPerform.pausarActionPerform)
       self.actionReiniciar.triggered.connect(self.actionsPerform.reiniciarActionPerform)
       self.actionParar.triggered.connect(self.actionsPerform.pararActionPerform)
       self.actionEjecutarLento.triggered.connect(self.actionsPerform.ejecutarLentoActionPerform)
       self.actionEjecutarRapido.triggered.connect(self.actionsPerform.ejecutarRapidoActionPerform)
       #
       self.actionManual.triggered.connect(self.actionsPerform.manualActionPerform)
       self.actionWww.triggered.connect(self.actionsPerform.wwwActionPerform)
       self.actionSalir.triggered.connect(self.actionsPerform.salirActionPerform)
       self.actionSalir2.triggered.connect(self.actionsPerform.salirActionPerform)
       #
       #self.codeArea.textChanged.connect(self.actionsPerform.codeAreaChangedValue)
       """self.actionExportarComoHtml.triggered.connect(self.actionsPerform.exportarComoHtml)
       self.actionImportarHtml.triggered.connect(self.actionsPerform.importarHtml)"""
    
        
    def getArchivoActual(self):
        return self.__archivoActual
    def setArchivoActual(self, f):
        self.__archivoActual = f
  
  


        
class GUIActions():
    def __init__(self, userInterface, procesador):
        self.userInterface = userInterface
        self.guiToolKit = GUIToolKit(userInterface, self)
        self.__mainFile=None
        self.procesador = procesador
        
    def pausarActionPerform(self):
        self.procesador.pausarPrograma()
    def pararActionPerform(self):
        self.procesador.pararPrograma()
    def reiniciarActionPerform(self):
        self.procesador.reiniciarPrograma()
    def ejecutarActionPerform(self):
        self.procesador.ejecutarPrograma()
    """def nuevoActionPerform(self):
        self.guiToolKit.confirmarArchivoSinGuardar()
        self.guiToolKit.generarArchivoNuevo()
    def abrirActionPerform(self):
        self.guiToolKit.confirmarArchivoSinGuardar()
        self.guiToolKit.cargarArchivoEnPrograma(self.guiToolKit.obtenerURLDeArchivoPorVentanaParaAbrir())
    def guardarActionPerform(self):
        if (self.userInterface.getArchivoActual().getPathAbsoluto()==None):
            self.guardarComoActionPerform()
            return True
        else:
            self.guiToolKit.guardarArchivo(self.userInterface.getArchivoActual().getPathAbsoluto())
        
    def guardarComoActionPerform(self):
        ruta = self.guiToolKit.obtenerURLDeArchivoPorVentanaParaGuardar()
        if ruta:
            self.guiToolKit.guardarArchivo(str(ruta))
        
    def cortarActionPerform(self):
        pass
        #self.userInterface.codeArea.cut()
        
    def copiarActionPerform(self):
        pass
        #self.userInterface.codeArea.copy()
    def pegarActionPerform(self):
        pass
        #self.userInterface.codeArea.paste()
    def deshacerActionPerform(self):
        pass
        #self.userInterface.codeArea.undo()
    def rehacerActionPerform(self):
        pass
        #self.userInterface.codeArea.redo()
    def limpiarAreaDeCodigoActionPerform(self):
        pass
        #if(self.guiToolKit.confirmarSiNoPorVentana("¿Seguro desea borrar todo el codigo?")):
        #        self.userInterface.codeArea.clear()
    """    
    def manualActionPerform(self):
        print("Abriendo Menu")
    def wwwActionPerform(self):
        url = Application.Application().getOficialURL()
        webbrowser.open_new(url)
    def salirActionPerform(self):
        self.guiToolKit.confirmarArchivoSinGuardar()        
        exit()
    def ejecutarLentoActionPerform(self):
        self.procesador.ejecutarLento()
    def ejecutarRapidoActionPerform(self):
        self.procesador.ejecutarRapido()
    def exportarComoHtml(self):
        ruta = self.guiToolKit.obtenerURLDeArchivoPorVentanaParaGuardar(extension="html")
        if ruta:
            self.guiToolKit.guardarArchivo(str(ruta),extension="html")
    def importarHtml(self):
        self.guiToolKit.confirmarArchivoSinGuardar()
        self.guiToolKit.cargarArchivoEnPrograma(self.guiToolKit.obtenerURLDeArchivoPorVentanaParaAbrir("html"))
        
        
    def codeAreaChangedValue(self):
        self.guiToolKit.marcarArchivoComoEscrito(True)
        
        
class GUIToolKit():
    def __init__(self, userInterface, guiactions):
        self.userInterface= userInterface
        self.guiActions = guiactions
        self.archivoModificado = False
        
    def generarArchivoNuevo(self):
        """
        Genera un archivo nuevo para Archivo->Nuevo o Ctrl+n
        """
        self.userInterface.setArchivoActual(processing.entity.Archivo())
        #self.userInterface.codeArea.setText("")
        self.userInterface.lblFileName.setText("URL: ")
        self.marcarArchivoComoEscrito(False)
    
    def obtenerURLDeArchivoPorVentanaParaGuardar(self, extension=None):
        """Selecciona una ruta para el guardado de archivos;
        Si no especificamos extension, buscara predeterminada del software;
        Podremos buscar de otra extension, especificandola por parametro;
        """
        if(extension==None):
            extension = Application.Application().getExtensionDeArchivos()
            
        ruta = QFileDialog.getSaveFileName(self.userInterface, "Guardar Archivo",
                                           "",
                                           "Archivos (*."+extension+")",
                                           options=QFileDialog.DontUseNativeDialog)        
        
        return ruta
        
    def obtenerURLDeArchivoPorVentanaParaAbrir(self, extension=None):
        """Selecciona una ruta para la apuretura de archivos;
        Si no especificamos extension, buscara predeterminada del software;
        Podremos buscar de otra extension, especificandola por parametro;
        """
        if(extension==None):
            extension = Application.Application().getExtensionDeArchivos()
            
        url = QFileDialog.getOpenFileName(self.userInterface, "Abrir Archivo",
                                   "",
                                   "Archivos (*."+extension+")",
                                   options=QFileDialog.DontUseNativeDialog)
        return url
     
    def guardarArchivo(self, ruta, extension=None):
        """Se guardara el archivo segun la url obtenida por obtenerURLDeArchivoPorVentanaParaGuardar()
        Si no especificamos extension, buscara predeterminada del software;
        Podremos buscar de otra extension, especificandola por parametro;
        """
        texto=""
        if(extension==None):
            extension=Application.Application().getExtensionDeArchivos()
            
        if not ruta.endswith("."+extension):
            ruta += ('.'+extension)
        #if(extension=="html"):
        #    texto=self.userInterface.codeArea.toHtml()
        #else:
        #    texto = self.userInterface.codeArea.toPlainText()
            
        with open(ruta, 'w') as archivo:
            archivo.write(texto)
        self.marcarArchivoComoEscrito(False)
        self.__actualizarArchivoPostCarga(ruta)
    
    def cargarArchivoEnPrograma(self, url):
        """Se cargara en programa el archivo segun la url obtenida por obtenerURLDeArchivoPorVentanaParaAbrir()
         Si no especificamos extension, buscara predeterminada del software;
        Podremos buscar de otra extension, especificandola por parametro;        
        """
        if not url:
            return False
        if url:
            url= unicode(url)
        
        with open((url), 'r') as archivo:
            contenido = archivo.read()
        
        #self.userInterface.codeArea.setText(contenido)

        self.__actualizarArchivoPostCarga(url)
        
        
        
            
    def confirmarSiNoPorVentana(self, mensaje):
        """ Confirmacion de si o no (True, False) por medio de ventana. """
        reply = QtGui.QMessageBox.question(self.userInterface, 'Confirmacion!',
            mensaje, QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        
        if reply == QtGui.QMessageBox.Yes:
            return True
        else:
            return False
            
    def confirmarArchivoSinGuardar(self):
        """Confirmara si el archivo actual esta sin guardar, en tal caso, sugerira guardarlo."""
        if(self.userInterface.getArchivoActual().isModified()):
            if(self.confirmarSiNoPorVentana("Desea guardar los cambios en el archivo actual?")):
                self.guiActions.guardarActionPerform()
        
        
        
    def __actualizarArchivoPostCarga(self,url):
        """Actualiza la interfaz grafica y el "Archivo" de la aplicacion."""
        self.userInterface.lblFileName.setText("URL: "+url)
        self.userInterface.setArchivoActual(processing.entity.Archivo(path=url,name=self._extraerNombreDeArchivoDesdeURL(url)))
        
        
    def _extraerNombreDeArchivoDesdeURL(self, url):
        """Se pasa la url completa, y extrae el nombre"""
        nombreDeArchivo = url.split("/")
        nombreDeArchivo = nombreDeArchivo[len(nombreDeArchivo)-1]
        return nombreDeArchivo
        
    def marcarArchivoComoEscrito(self, boolean):
        """Setea el archivo actual como escrito o no segun parametro."""
        texto=str(self.userInterface.lblFileName.text())
        if(not texto.startswith("URL")):
            texto="URL:"
        
        texto = self.setAsteriscoFinal(texto, boolean)
        
        self.userInterface.lblFileName.setText(texto)
        self.userInterface.getArchivoActual().setModified(boolean)
        
            
                
    def setAsteriscoFinal(self, string, boolean):
        """Setea o saca el * final de un string segun parametro."""
        if(boolean):
            if(not string.endswith("*")):
                string +="*"
        elif(not boolean):
            if(string.endswith("*")):
                string = string.replace("*","")
        return string
        
