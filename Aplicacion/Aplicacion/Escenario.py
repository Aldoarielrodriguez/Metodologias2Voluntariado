import pilasengine


class Vehiculo(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/Bus.png")
        self.escala=0.4

class Persona(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/Persona2.png")
        self.escala=0.4

class SenialBus(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar("images/senialBus.png")
        self.escala=0.4

class Parada(pilasengine.actores.Actor):
    def iniciar(self):
        self.imgHorizontal=self.pilas.imagenes.cargar("images/paradaHorizontal.png")
        self.imgVertical=self.pilas.imagenes.cargar("images/paradaVertical.png")
        self.imagen=self.imgHorizontal
    def setToLeft(self):
        self.imagen=self.imgVertical
    def setToRight(self):
        self.imagen=self.imgVertical
    def setToUp(self):
        self.imagen=self.imgHorizontal
    def setToDown(self):
        self.imagen=self.imgHorizontal

