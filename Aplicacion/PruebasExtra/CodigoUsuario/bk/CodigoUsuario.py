import pilasengine

def engancharCodigos(cod, cod2):
    cod.incrustar(cod2)

def clickEnCodigo(codigo):
    codigo.eliminar()


"""/////////////////    Entidades"""
class CodigoUsuario(pilasengine.actores.Actor):
    def iniciar(self):
        pass
    def esIncrustable(self,codigosAceptados, codigoIngresado):
        for cadaCodigo in codigosAceptados:
            if(cadaCodigo==codigoIngresado):
                return True
        return False
    def getCantidadContenida(self):
        cant=0
        if(str(self.macro)!=None):
            for x in self.macro:
                cant+=x.getCantidadContenida()
            cant+=len(self.macro)
        return cant
    def actualizar(self):
         self.actualizarGeneral()

    def actualizarGeneral(self):
        contadorDeDesplazamiento=1
        for codigo in self.macro:
            codigo.y=self.y-self.desplazamientoVertical*contadorDeDesplazamiento
            codigo.x=self.x+self.desplazamientoHorizontal
            codigo.z=self.z-1
            contadorDeDesplazamiento+=1+codigo.getCantidadContenida()
    def actualizarConCondicion(self):
        if(str(self.condicion)!="None"):
            self.condicion.y=self.y-5
            self.condicion.x=self.x+30
            self.condicion.z=self.z-1






class IniciarPrograma(CodigoUsuario):
    def iniciar(self, contexto):
        contexto.agregarCodigo(self)
        self.imagen=self.pilas.imagenes.cargar("images/IniciarProgramaPilas.png")
        self.desplazamientoVertical=28
        self.desplazamientoHorizontal=20
        self.centro=("izquierda","arriba")
        self.macro=[]
    def incrustar(self, codigo):
        if(self.esIncrustable(["BasicoPredefinido","CondicionalSi","Repetir"], type(codigo).__name__)):
            self.macro.append(codigo)
            return True
        return False

        

class BasicoPredefinido(CodigoUsuario):
    def iniciar(self, contexto):
        contexto.agregarCodigo(self)
        self.imagen=self.pilas.imagenes.cargar("images/BasicoPredefinido.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=30
        self.centro=("izquierda","arriba")
        self.macro=[]
        self.aprender(self.pilas.habilidades.Arrastrable)
    def incrustar(self, codigo):
        return False
    def actualizar(self):
        pass
    def getCantidadContenida(self):
        return 0
        
class CondicionalSi(CodigoUsuario):
    def iniciar(self, contexto):
        contexto.agregarCodigo(self)
        self.imagen=self.pilas.imagenes.cargar("images/CondicionalSi.png")
        self.desplazamientoVertical=36
        self.desplazamientoHorizontal=20
        self.centro=("izquierda","arriba")
        self.macro=[]
        self.condicion=None
        self.aprender(self.pilas.habilidades.Arrastrable)
    def incrustar(self, codigo):
        if(self.esIncrustable(["BasicoPredefinido","CondicionalSi","Repetir"], type(codigo).__name__)):
            self.macro.append(codigo)
            return True
        print(type(codigo).__name__)
        if(str(type(codigo).__name__)=="Condicion"):
            self.condicion=codigo
            return True
            
        return False
    def actualizar(self):
        self.actualizarGeneral()
        self.actualizarConCondicion()



class Condicion(CodigoUsuario):
    def iniciar(self, contexto):
        contexto.agregarCodigo(self)
        self.imagen=self.pilas.imagenes.cargar("images/Condicion.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=-29
        self.centro=("izquierda","arriba")
        self.aprender(self.pilas.habilidades.Arrastrable)
    def incrustar(self, codigo):
        return False
    def actualizar(self):
        pass

class Repetir(CodigoUsuario):
    def iniciar(self, contexto):
        contexto.agregarCodigo(self)
        self.imagen=self.pilas.imagenes.cargar("images/Repetir.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=22
        self.centro=("izquierda","arriba")
        self.macro=[]
        self.aprender(self.pilas.habilidades.Arrastrable)
    def incrustar(self, codigo):
        if(self.esIncrustable(["BasicoPredefinido","CondicionalSi","Repetir"], type(codigo).__name__)):
            self.macro.append(codigo)
            return True
        return False
    def actualizar(self):
        self.actualizarGeneral()



"""/////////////////         Contextuales"""
class Contexto():
    def __init__(self, pilas):
        self.pilas=pilas
        self.__coordenadasIniciarPrograma=[-250,200]
        self.__depositoDeCodigo=DepositoDeCodigo()
        self.__todosLosCodigos=[]
        self.pilas.colisiones.agregar(self.__todosLosCodigos, self.__todosLosCodigos,engancharCodigos)
    def agregarCodigo(self,codigo):
        if(type(codigo).__name__=="IniciarPrograma"):
            codigo.x=self.__coordenadasIniciarPrograma[0]
            codigo.y=self.__coordenadasIniciarPrograma[1]
        else:
            self.__depositoDeCodigo.agregarCodigo(codigo)
        self.__todosLosCodigos.append(codigo)
        codigo.cuando_hace_click=clickEnCodigo

        
        
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
        
