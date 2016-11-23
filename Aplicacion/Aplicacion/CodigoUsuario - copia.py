import pilasengine

 
class Contexto():
    def __init__(self):
        self.__coordenadasIniciarPrograma=[-300,250]
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
    def engancharCodigos(self, cod, cod2):
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
            
           
        
        
class DepositoDeCodigo():
    def __init__(self):
        self.__y=300
        self.__x=200
        self.__codigos=[]
        self.__tamanioDeSalto=50
    def agregarCodigo(self,codigo):
        codigo.x=self.__x
        codigo.y=self.__y-(len(self.__codigos)*self.__tamanioDeSalto)
        self.__codigos.append(codigo)
    def getCodigos(self):
        return self.__codigos



class CodigoUsuario(pilasengine.actores.Actor):
    def iniciar(self,img="images/Repetir.png"):
        self.owner=None
        self.macro=[]
        self.centro=("izquierda","arriba")
        self.imagen= self.pilas.imagenes.cargar(img)
        self.desplazamientoVertical=30
        self.desplazamientoHorizontal=30
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
        CodigoUsuario.iniciar(self)
        self.imagen=self.pilas.imagenes.cargar("images/IniciarProgramaPilas.png")
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
    def ejecutar(self):
        print("Se acaba de iniciar Programa")
        for cod in self.macro:
            cod.ejecutar()

        

class BasicoPredefinido(CodigoUsuario):
    def iniciar(self):
        CodigoUsuario.iniciar(self)
        self.imagen=self.pilas.imagenes.cargar("images/BasicoPredefinido.png")
        self.aprender(self.pilas.habilidades.Arrastrable)
        self.colisiono=False
        self.codigo="pass"

    def incrustar(self, codigo):
        return False
    def actualizar(self):
        pass
    def getCantidadContenida(self):
        return 0
    def ejecutar(self):
        exec(self.codigo)
    def setCodigo(self, codigo):
        self.codigo = codigo
        
class CondicionalSi(CodigoUsuario):
    def iniciar(self):
        CodigoUsuario.iniciar(self)
        self.imagen=self.pilas.imagenes.cargar("images/CondicionalSi.png")
        self.__condicion=None
        self.aprender(self.pilas.habilidades.Arrastrable)
        self.condicion=""
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
    def setCondicion(self, condicion):
        self.condicion=condicion
    def ejecutar(self):
        cond=False
        exec("cond="+self.condicion.condicion)
        if(cond):
            for cod in self.macro:
                cod.ejecutar()



class Condicion(CodigoUsuario):
    def iniciar(self):
        CodigoUsuario.iniciar(self)
        self.imagen=self.pilas.imagenes.cargar("images/Condicion.png")
        self.aprender(self.pilas.habilidades.Arrastrable)
        self.condicion=""
    def incrustar(self, codigo):
        pass
    def actualizar(self):
        pass
    def getMacro(self):
        return []
    def ejecutar(self):
        pass
    def setCondicion(self, condicion):
        self.condicion=condicion

class Repetir(CodigoUsuario):
    def iniciar(self):
        CodigoUsuario.iniciar(self,img="images/Repetir.png")
        self.aprender(self.pilas.habilidades.Arrastrable)
        self.cantidad=0
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
    def ejecutar(self):
        for time in range(0,self.cantidad):
            for cod in self.macro:
                cod.ejecutar()
    def setCantidad(self,cant):
        self.cantidad=cant

