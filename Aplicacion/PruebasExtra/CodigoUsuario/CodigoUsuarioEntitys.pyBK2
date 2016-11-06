import pilasengine

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




class IniciarPrograma(CodigoUsuario):
    def iniciar(self):
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
    def actualizar(self):
        contadorDeDesplazamiento=1
        for codigo in self.macro:
            codigo.y=self.y-self.desplazamientoVertical*contadorDeDesplazamiento
            codigo.x=self.x+self.desplazamientoHorizontal
            codigo.z=self.z-1
            contadorDeDesplazamiento+=1+codigo.getCantidadContenida()
        

class BasicoPredefinido(CodigoUsuario):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/BasicoPredefinido.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=30
        self.centro=("izquierda","arriba")
        self.macro=[]
    def incrustar(self, codigo):
        return False
    def actualizar(self):
        pass
    def getCantidadContenida(self):
        return 0
        
class CondicionalSi(CodigoUsuario):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/CondicionalSi.png")
        self.desplazamientoVertical=36
        self.desplazamientoHorizontal=20
        self.centro=("izquierda","arriba")
        self.macro=[]
        self.__condicion=None
    def incrustar(self, codigo):
        if(self.esIncrustable(["BasicoPredefinido","CondicionalSi","Repetir"], type(codigo).__name__)):
            self.macro.append(codigo)
            return True
        print(type(codigo).__name__)
        if(str(type(codigo).__name__)=="Condicion"):
            self.__condicion=codigo
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


class Condicion(CodigoUsuario):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/Condicion.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=-29
        self.centro=("izquierda","arriba")
    def incrustar(self, codigo):
        return False
    def actualizar(self):
        pass

class Repetir(CodigoUsuario):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/Repetir.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=22
        self.centro=("izquierda","arriba")
        self.macro=[]
    def incrustar(self, codigo):
        if(self.esIncrustable(["BasicoPredefinido","CondicionalSi","Repetir"], type(codigo).__name__)):
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

