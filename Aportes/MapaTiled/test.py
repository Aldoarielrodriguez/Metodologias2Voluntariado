import pilasengine

pilas = pilasengine.iniciar()

mapa = pilas.actores.MapaTiled("test.tmx")

pilas.ejecutar()
