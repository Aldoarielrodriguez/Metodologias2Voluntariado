#exec("print(\"Hola Mundo\")")
#print("Hola Mundo")
#print("########################")
#string="lista=\"abcde\"\nfor x in lista:\n    print(x)"
#exec(string)


def decodificar(objeto):
    exec(objeto.getContenido())


class Codigo():
    def __init__(self, contenido):
        self.__contenido=contenido
    def getContenido(self):
        return self.__contenido

class Colectivo():
    def __init__(self):
        pass
    def arrancar(self):
        self.setON()
    def setON(self):
        self.luces=ON

colectivo = Colectivo()
codigo = Codigo("colectivo.arrancar()")
decodificar(codigo)
