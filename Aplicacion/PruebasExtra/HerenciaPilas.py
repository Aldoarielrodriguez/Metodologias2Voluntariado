import pilasengine

pilas = pilasengine.iniciar()

class Padre(pilasengine.actores.Actor):
    def iniciar(self):
        self.asd=4
        self.qwe="qweVariable"


class Hijo(Padre):
    def iniciar(self):
        Padre.iniciar(self)
        pass
epa=Hijo(pilas)


def info():
    print(epa.asd)
    print(epa.qwe)

pilas.ejecutar()
