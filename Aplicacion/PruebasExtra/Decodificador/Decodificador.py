import pilasengine

class Colectivo():
    def __init__(self):
        self.encendido=False
    def encender(self):
        print("Soy el colectivo y me acabo de encender")
        self.encendido=True
    def avanzar(self):
        print("Soy el colectivo y avance una cuadra")
    def isEncendido(self):
        return self.encendido
    def subirPasajeros(self):
        print("Estoy subiendo pasajeros")
class CodigoUsuario():
    def __init__(self):
        pass

    def ejecutar(self):
        pass

bondi=Colectivo()


class IniciarPrograma():
    def __init__(self):
        self.macro=[]
    def ejecutar(self):
        print("Se acaba de iniciar Programa")
        for cod in self.macro:
            cod.ejecutar()

class BasicoPredefinido():
    def __init__(self):
        self.codigo="pass"
        self.macro=[]
    def ejecutar(self):
        exec(self.codigo)
    def setCodigo(self, codigo):
        self.codigo = codigo

class Condicion():
    def __init__(self):
        self.macro=[]
        self.condicion=""
    def ejecutar(self):
        pass
    def setCondicion(self, condicion):
        self.condicion=condicion


class CondicionalSi():
    def __init__(self):
        self.macro=[]
        self.condicion=""
    def setCondicion(self, condicion):
        self.condicion=condicion
    def ejecutar(self):
        cond=False
        exec("cond="+self.condicion.condicion)
        if(cond):
            for cod in self.macro:
                cod.ejecutar()


        

class Repetir():
    def __init__(self):
        self.cantidad=0
        self.macro=[]
    def ejecutar(self):
        for time in range(0,self.cantidad):
            for cod in self.macro:
                cod.ejecutar()
    def setCantidad(self,cant):
        self.cantidad=cant


iniciarPrograma=IniciarPrograma()

bondiArrancar=BasicoPredefinido()
bondiArrancar.setCodigo("bondi.encender()")

bondiAvanzar=BasicoPredefinido()
bondiAvanzar.setCodigo("bondi.avanzar()")

bondiDoblar=BasicoPredefinido()
bondiDoblar.setCodigo("bondi.doblar()")
bondiSubirPasajeros=BasicoPredefinido()
bondiSubirPasajeros.setCodigo("bondi.subirPasajeros()")

condicionalSi=CondicionalSi()

condicion=Condicion()
condicion.setCondicion("bondi.isEncendido()")
condicionalSi.setCondicion(condicion)
condicionalSi.macro.append(bondiSubirPasajeros)

repetir=Repetir()
repetir.setCantidad(4)
repetir.macro.append(bondiAvanzar)

iniciarPrograma.macro.append(bondiArrancar)
iniciarPrograma.macro.append(repetir)
iniciarPrograma.macro.append(condicionalSi)

iniciarPrograma.ejecutar()
