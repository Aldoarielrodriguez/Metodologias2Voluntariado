import pilasengine
import CodigoUsuario
import time



pilas = pilasengine.iniciar(1024,860)

def engancharCodigos(cod, cod2):
    if(type(cod).__name__=="Condicion"):
        if(type(cod2).__name__!="CondicionalSi"):
            return False
    if(type(cod).__name__=="CondicionalSi"):
        if(type(cod2).__name__=="Condicion"):
            cod.incrustar(cod2)

    if(type(cod).__name__=="CondicionalSi" and type(cod2).__name__=="Condicion"):
            cod.incrustar(cod2)
            return True
    #Ambos son el mismo
    if(cod.x==cod2.x and cod.y==cod2.y):
        return False
    #En si, son distintos
    elif(cod.x!=cod2.x or cod.y!=cod2.y):
        for x in cod.getMacro():
            if(x.x==cod2.x and x.y==cod2.y):
                return False
        if(str(cod2.owner)=="None"):
            cod.incrustar(cod2)



  
        
contexto=CodigoUsuario.Contexto()

varIniciarPrograma=CodigoUsuario.IniciarPrograma(pilas)
contexto.agregarCodigo(varIniciarPrograma)

varBasicoPredefinido=CodigoUsuario.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido)

varBasicoPredefinido2=CodigoUsuario.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido2)

varBasicoPredefinido3=CodigoUsuario.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido3)

varBasicoPredefinido4=CodigoUsuario.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido4)

varBasicoPredefinido5=CodigoUsuario.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido5)

varBasicoPredefinido6=CodigoUsuario.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido6)

varBasicoPredefinido7=CodigoUsuario.BasicoPredefinido(pilas)
contexto.agregarCodigo(varBasicoPredefinido7)


varCondicion=CodigoUsuario.Condicion(pilas)
contexto.agregarCodigo(varCondicion)

varCondicion2=CodigoUsuario.Condicion(pilas)
contexto.agregarCodigo(varCondicion2)


varCondicionalSi=CodigoUsuario.CondicionalSi(pilas)
contexto.agregarCodigo(varCondicionalSi)

varCondicionalSi2=CodigoUsuario.CondicionalSi(pilas)
contexto.agregarCodigo(varCondicionalSi2)

varRepetir=CodigoUsuario.Repetir(pilas)
contexto.agregarCodigo(varRepetir)


pilas.colisiones.agregar(contexto.getTodosLosCodigos(), contexto.getTodosLosCodigos(),engancharCodigos)

pilas.fondos.Fondo('images/background.jpg')
pilas.ejecutar()
