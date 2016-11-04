import pilasengine

class CodigoUsuario(pilasengine.actores.Actor):
    def iniciar(self):
        pass
    def esIncrustable(self,codigosAceptados, codigoIngresado):
        for cadaCodigo in codigosAceptados:
            if(cadaCodigo==codigoIngresado):
                return True
        return False



class IniciarPrograma(CodigoUsuario):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/IniciarProgramaPilas.png")
        self.desplazamientoVertical=28
        self.desplazamientoHorizontal=20
        self.centro=("izquierda","arriba")
        self.__macro=[]
    def incrustar(self, codigo):
        if(self.esIncrustable(["BasicoPredefinido","CondicionalSi","Repetir"], type(codigo).__name__)):
            self.__macro.append(codigo)
            return True
        #codigo.devolverAlOrigen()
    def actualizar(self):
        contadorDeDesplazamiento=1
        for codigo in self.__macro:
            codigo.y=self.y-self.desplazamientoVertical*contadorDeDesplazamiento
            codigo.x=self.x+self.desplazamientoHorizontal
            contadorDeDesplazamiento+=1
    def devolverAlOrigen(self):
        self.x=200
        self.y=200
        

class BasicoPredefinido(CodigoUsuario):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/BasicoPredefinido.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=-29
        self.centro=("izquierda","arriba")
        self.__macro=[]
    def incrustar(self, codigo):
        self.__macro.append(codigo)
    def actualizar(self):
        contadorDeDesplazamiento=1
        for codigo in self.__macro:
            codigo.y=self.y-self.desplazamientoVertical*contadorDeDesplazamiento
            codigo.x=self.x+self.desplazamientoHorizontal
            contadorDeDesplazamiento+=1

class CondicionalSi(CodigoUsuario):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/CondicionalSi.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=-29
        self.centro=("izquierda","arriba")
        self.__macro=[]
    def incrustar(self, codigo):
        self.__macro.append(codigo)
    def actualizar(self):
        contadorDeDesplazamiento=1
        for codigo in self.__macro:
            codigo.y=self.y-self.desplazamientoVertical*contadorDeDesplazamiento
            codigo.x=self.x+self.desplazamientoHorizontal
            contadorDeDesplazamiento+=1

class DefinirMetodo(CodigoUsuario):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/DefinirMetodo.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=-29
        self.centro=("izquierda","arriba")
        self.__macro=[]
    def incrustar(self, codigo):
        self.__macro.append(codigo)
    def actualizar(self):
        contadorDeDesplazamiento=1
        for codigo in self.__macro:
            codigo.y=self.y-self.desplazamientoVertical*contadorDeDesplazamiento
            codigo.x=self.x+self.desplazamientoHorizontal
            contadorDeDesplazamiento+=1
    def devolverAlOrigen(self):
        self.x=200
        self.y=200

class Condicion(CodigoUsuario):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/Condicion.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=-29
        self.centro=("izquierda","arriba")
        self.__macro=[]
    def incrustar(self, codigo):
        self.__macro.append(codigo)
    def actualizar(self):
        contadorDeDesplazamiento=1
        for codigo in self.__macro:
            codigo.y=self.y-self.desplazamientoVertical*contadorDeDesplazamiento
            codigo.x=self.x+self.desplazamientoHorizontal
            contadorDeDesplazamiento+=1
    def devolverAlOrigen(self):
        self.x=200
        self.y=200

class Repetir(CodigoUsuario):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/Repetir.png")
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=-29
        self.centro=("izquierda","arriba")
        self.__macro=[]
    def incrustar(self, codigo):
        self.__macro.append(codigo)
    def actualizar(self):
        contadorDeDesplazamiento=1
        for codigo in self.__macro:
            codigo.y=self.y-self.desplazamientoVertical*contadorDeDesplazamiento
            codigo.x=self.x+self.desplazamientoHorizontal
            contadorDeDesplazamiento+=1
