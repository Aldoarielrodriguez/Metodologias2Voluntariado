class Archivo():
    def __init__(self, path=None, name=None):
        self.__pathAbsoluto = path
        self.__name = name
        self.__isModified = False
    def getPathAbsoluto(self):
        return self.__pathAbsoluto
    def getName(self):
        return self.__name
    def isModified(self):
        return self.__isModified
    def setPathAbsoluto(self, path):
        self.__pathAbsoluto= path
    def setName(self, name):
        self.__name = name
    def setModified(self, boolean):
        self.__isModified = boolean
        