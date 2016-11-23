import pilasengine
import CodigoUsuario
pilas = pilasengine.iniciar()

contexto=CodigoUsuario.Contexto(pilas=pilas)

varIniciarPrograma=CodigoUsuario.IniciarPrograma(pilas, contexto=contexto)
varBasicoPredefinido=CodigoUsuario.BasicoPredefinido(pilas, contexto=contexto)
varBasicoPredefinido2=CodigoUsuario.BasicoPredefinido(pilas, contexto=contexto)

"""
varBasicoPredefinido3=CodigoUsuario.BasicoPredefinido(pilas, contexto=contexto)
varBasicoPredefinido4=CodigoUsuario.BasicoPredefinido(pilas, contexto=contexto)
varBasicoPredefinido5=CodigoUsuario.BasicoPredefinido(pilas, contexto=contexto)
varBasicoPredefinido6=CodigoUsuario.BasicoPredefinido(pilas, contexto=contexto)
varBasicoPredefinido7=CodigoUsuario.BasicoPredefinido(pilas, contexto=contexto)
varCondicion=CodigoUsuario.Condicion(pilas, contexto=contexto)
varCondicion2=CodigoUsuario.Condicion(pilas, contexto=contexto)
varCondicionalSi=CodigoUsuario.CondicionalSi(pilas, contexto=contexto)
varCondicionalSi2=CodigoUsuario.CondicionalSi(pilas, contexto=contexto)
varRepetir=CodigoUsuario.Repetir(pilas, contexto=contexto)
"""


"""
varIniciarPrograma.incrustar(varBasicoPredefinido)
varIniciarPrograma.incrustar(varBasicoPredefinido2)
varIniciarPrograma.incrustar(varRepetir)
varRepetir.incrustar(varCondicionalSi)
varCondicionalSi.incrustar(varCondicion)
varCondicionalSi.incrustar(varBasicoPredefinido3)
varCondicionalSi.incrustar(varBasicoPredefinido4)
varRepetir.incrustar(varCondicionalSi2)
varCondicionalSi2.incrustar(varCondicion2)
varCondicionalSi2.incrustar(varBasicoPredefinido5)
varIniciarPrograma.incrustar(varBasicoPredefinido6)
varIniciarPrograma.incrustar(varBasicoPredefinido7)
"""


pilas.fondos.Fondo('images/background.jpg')
pilas.ejecutar()
