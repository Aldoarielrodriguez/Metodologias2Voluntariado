import pilasengine
import CodigoUsuarioEntitys
pilas = pilasengine.iniciar()

class Contexto():
    def __init__(self):
        self.__coordenadasIniciarPrograma=[-250,200]
        self.__depositoDeCodigo=DepositoDeCodigo()
    def agregarCodigo(self,codigo):
        if(type(codigo).__name__=="IniciarPrograma"):
            codigo.x=self.__coordenadasIniciarPrograma[0]
            codigo.y=self.__coordenadasIniciarPrograma[1]
        else:
            self.__depositoDeCodigo.agregarCodigo(codigo)

        
        
class DepositoDeCodigo():
    def __init__(self):
        self.__y=200
        self.__x=200
        self.__codigos=[]
        self.__tamanioDeSalto=50
    def agregarCodigo(self,codigo):
        codigo.x=self.__x
        codigo.y=self.__y-(len(self.__codigos)*self.__tamanioDeSalto)
        self.__codigos.append(codigo)
        
        
contexto=Contexto()

varIniciarPrograma=CodigoUsuarioEntitys.IniciarPrograma(pilas)
contexto.agregarCodigo(varIniciarPrograma)

varBasicoPredefinido=CodigoUsuarioEntitys.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido)

varDefinirMetodo=CodigoUsuarioEntitys.DefinirMetodo(pilas)
contexto.agregarCodigo(varDefinirMetodo)

varCondicion=CodigoUsuarioEntitys.Condicion(pilas)
contexto.agregarCodigo(varCondicion)

varCondicionalSi=CodigoUsuarioEntitys.CondicionalSi(pilas)
contexto.agregarCodigo(varCondicionalSi)

varRepetir=CodigoUsuarioEntitys.Repetir(pilas)
contexto.agregarCodigo(varCondicionalSi)

varIniciarPrograma2=CodigoUsuarioEntitys.IniciarPrograma(pilas)
contexto.agregarCodigo(varIniciarPrograma2)

#varCodigoUsuario=CodigoUsuarioEntitys.CodigoUsuario(pilas)
#contexto.agregarCodigo(varCodigoUsuario)

"""
Iniciar programa:
Debe soportar:
    BasicoPredefinido
    CondicionalSi
    Repetir
NO debe soportar:
    IniciarPrograma
    CodigoUsuario
    DefinirMetodo
    Condicion
"""

varIniciarPrograma.incrustar(varBasicoPredefinido)
varIniciarPrograma.incrustar(varCondicionalSi)
varIniciarPrograma.incrustar(varRepetir)
varIniciarPrograma.incrustar(varIniciarPrograma2)
#varIniciarPrograma.incrustar(varCodigoUsuario)
varIniciarPrograma.incrustar(varDefinirMetodo)
varIniciarPrograma.incrustar(varCondicion)

pilas.fondos.Fondo('images/background.jpg')
pilas.ejecutar()
