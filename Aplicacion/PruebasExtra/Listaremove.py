
class MiClase():
    def __init__(self, contenido):
        self.contenido=contenido


clase1=MiClase("asd")
clase2=MiClase("aasdasdsd")
clase3=MiClase("aqweqwesd")
clase4=MiClase("axcvxcvsd")
clase5=MiClase("aghgfsd")
clase6=MiClase("asqweqwed")

lista=[]
lista.append(clase1)
lista.append(clase2)
lista.append(clase3)
lista.append(clase4)
lista.append(clase5)
lista.append(clase6)

print("Lista completa: ")
print lista

claseExtra=MiClase("asd")
lista.remove(clase1)
print("Lista Incompleta")
print lista
