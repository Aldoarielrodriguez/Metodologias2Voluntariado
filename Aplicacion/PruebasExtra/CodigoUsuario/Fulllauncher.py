import pilasengine
import CodigoUsuarioEntitys
pilas = pilasengine.iniciar()

a =  CodigoUsuarioEntitys.IniciarPrograma(pilas)
b = CodigoUsuarioEntitys.BasicoPredefinido(pilas)
c = CodigoUsuarioEntitys.CondicionalSi(pilas)
d = CodigoUsuarioEntitys.DefinirMetodo(pilas)
e = CodigoUsuarioEntitys.Condicion(pilas)
f = CodigoUsuarioEntitys.Repetir(pilas)

a.aprender(pilas.habilidades.Arrastrable)
b.aprender(pilas.habilidades.Arrastrable)
c.aprender(pilas.habilidades.Arrastrable)
d.aprender(pilas.habilidades.Arrastrable)
e.aprender(pilas.habilidades.Arrastrable)
f.aprender(pilas.habilidades.Arrastrable)

pilas.fondos.FondoMozaico('images/background.jpg')
pilas.ejecutar()
