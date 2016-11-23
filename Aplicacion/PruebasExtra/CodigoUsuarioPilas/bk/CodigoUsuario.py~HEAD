import pilasengine

class Contexto():
    def __init__(self):
        self.__coordenadasIniciarPrograma=[-250,200]
        self.__depositoDeCodigo=DepositoDeCodigo()
        self.iniciarPrograma=None
    def agregarCodigo(self,codigo):
        if(type(codigo).__name__=="IniciarPrograma"):
            codigo.x=self.__coordenadasIniciarPrograma[0]
            codigo.y=self.__coordenadasIniciarPrograma[1]
            self.iniciarPrograma=codigo
        else:
            self.__depositoDeCodigo.agregarCodigo(codigo)
    def getTodosLosCodigos(self):
        lista=self.__depositoDeCodigo.getCodigos()
        lista.append(self.iniciarPrograma)
        return lista

        
        
class DepositoDeCodigo():
    def __init__(self):
        self.__y=400
        self.__x=300
        self.__codigos=[]
        self.__tamanioDeSalto=50
    def agregarCodigo(self,codigo):
        codigo.x=self.__x
        codigo.y=self.__y-(len(self.__codigos)*self.__tamanioDeSalto)
        self.__codigos.append(codigo)
    def getCodigos(self):
        return self.__codigos



class CodigoUsuario(pilasengine.actores.Actor):
    def iniciar(self):
        self.macro=[]
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
    def getMacro(self):
        return self.macro




class IniciarPrograma(CodigoUsuario):
    def iniciar(self):
        self.owner=None
        self.imagen=self.pilas.imagenes.cargar("images/IniciarProgramaPilas.png")
        self.desplazamientoVertical=28
        self.desplazamientoHorizontal=20
        self.centro=("izquierda","arriba")
        self.macro=[]
        self.colisiono=False
    def incrustar(self, codigo):
        if(self.esIncrustable(["BasicoPredefinido","CondicionalSi","Repetir"], type(codigo).__name__)):
            for x in self.macro:
                if(codigo.x==x.x and codigo.y==x.y):
                    return False
            if(codigo.x==self.x and codigo.y==self.y):
                return False
            self.macro.append(codigo)
            codigo.owner=self
            return True
        return False
    def actualizar(self):
        contadorDeDesplazamiento=1
        for codigo in self.macro:
            codigo.y=self.y-self.desplazamientoVertical*contadorDeDesplazamiento
            codigo.x=self.x+self.desplazamientoHorizontal
            codigo.z=self.z-1
            contadorDeDesplazamiento+=1+codigo.getCantidadContenida()

        

class BasicoPredefinido(CodigoUsuario):
    def iniciar(self):
        self.owner=None
        self.imagen=self.pilas.imagenes.cargar("images/BasicoPredefinido.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=30
        self.centro=("izquierda","arriba")
        self.macro=[]
        self.aprender(self.pilas.habilidades.Arrastrable)
        self.colisiono=False
    def incrustar(self, codigo):
        return False
    def actualizar(self):
        pass
    def getCantidadContenida(self):
        return 0
        
class CondicionalSi(CodigoUsuario):
    def iniciar(self):
        self.owner=None
        self.imagen=self.pilas.imagenes.cargar("images/CondicionalSi.png")
        self.desplazamientoVertical=36
        self.desplazamientoHorizontal=20
        self.centro=("izquierda","arriba")
        self.macro=[]
        self.__condicion=None
        self.aprender(self.pilas.habilidades.Arrastrable)
    def incrustar(self, codigo):
        if(type(codigo).__name__=="Condicion"):
            self.__condicion=codigo
            return True
        if(self.esIncrustable(["BasicoPredefinido","CondicionalSi"], type(codigo).__name__)):
            for x in self.macro:
                if(codigo.x==x.x and codigo.y==x.y):
                    return False
            if(codigo.x==self.x and codigo.y==self.y):
                return False
            self.macro.append(codigo)
            return True
        return False
    def actualizar(self):
        contadorDeDesplazamiento=1
        for codigo in self.macro:
            codigo.y=self.y-self.desplazamientoVertical*contadorDeDesplazamiento
            codigo.x=self.x+self.desplazamientoHorizontal
            codigo.z=self.z-1
            contadorDeDesplazamiento+=1+codigo.getCantidadContenida()
        if(str(self.__condicion)!="None"):
            self.__condicion.y=self.y-5
            self.__condicion.x=self.x+30
            self.__condicion.z=self.z-1
    def getMacro(self):
        return self.macro



class Condicion(CodigoUsuario):
    def iniciar(self):
        self.owner=None
        self.imagen=self.pilas.imagenes.cargar("images/Condicion.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=-29
        self.centro=("izquierda","arriba")
        self.aprender(self.pilas.habilidades.Arrastrable)
    def incrustar(self, codigo):
        pass
    def actualizar(self):
        pass
    def getMacro(self):
        return []

class Repetir(CodigoUsuario):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/Repetir.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=22
        self.centro=("izquierda","arriba")
        self.macro=[]
        self.aprender(self.pilas.habilidades.Arrastrable)
        self.owner=None
    def incrustar(self, codigo):
        if(self.esIncrustable(["BasicoPredefinido","CondicionalSi","Repetir"], type(codigo).__name__)):
            for x in self.macro:
                if(codigo.x==x.x and codigo.y==x.y):
                    return False
            if(codigo.x==self.x and codigo.y==self.y):
                return False
            if(str(codigo.owner)!="None"):
                return False
            codigo.owner=self
            self.macro.append(codigo)
            return True
        return False
    def actualizar(self):
        contadorDeDesplazamiento=1
        for codigo in self.macro:
            codigo.y=self.y-self.desplazamientoVertical*contadorDeDesplazamiento
            codigo.x=self.x+self.desplazamientoHorizontal
            codigo.z=self.z-1
            contadorDeDesplazamiento+=1+codigo.getCantidadContenida()

