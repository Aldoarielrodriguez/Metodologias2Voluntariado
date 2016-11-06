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

varBasicoPredefinido2=CodigoUsuarioEntitys.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido2)

varBasicoPredefinido3=CodigoUsuarioEntitys.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido3)

varBasicoPredefinido4=CodigoUsuarioEntitys.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido4)

varBasicoPredefinido5=CodigoUsuarioEntitys.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido5)

varBasicoPredefinido6=CodigoUsuarioEntitys.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido6)

varBasicoPredefinido7=CodigoUsuarioEntitys.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido7)


varCondicion=CodigoUsuarioEntitys.Condicion(pilas)
contexto.agregarCodigo(varCondicion)

varCondicion2=CodigoUsuarioEntitys.Condicion(pilas)
contexto.agregarCodigo(varCondicion2)


varCondicionalSi=CodigoUsuarioEntitys.CondicionalSi(pilas)
contexto.agregarCodigo(varCondicionalSi)

varCondicionalSi2=CodigoUsuarioEntitys.CondicionalSi(pilas)
contexto.agregarCodigo(varCondicionalSi2)

varRepetir=CodigoUsuarioEntitys.Repetir(pilas)
contexto.agregarCodigo(varCondicionalSi)





varIniciarPrograma.incrustar(varBasicoPredefinido)
varIniciarPrograma.incrustar(varBasicoPredefinido2)
varIniciarPrograma.incrustar(varRepetir)
varRepetir.incrustar(varCondicionalSi)
varCondicionalSi.incrustar(varCondicion)
varCondicionalSi.incrustar(varBasicoPredefinido3)
varCondicionalSi.incrustar(varBasicoPredefinido4)
varRepetir.incrustar(varCondicionalSi2)
varCondicionalSi2.incrustar(varCondicion2)
varCondicionalSi2.incrustar(varBasicoPredefinido5)
varIniciarPrograma.incrustar(varBasicoPredefinido6)
varIniciarPrograma.incrustar(varBasicoPredefinido7)

pilas.fondos.Fondo('images/background.jpg')
pilas.ejecutar()
