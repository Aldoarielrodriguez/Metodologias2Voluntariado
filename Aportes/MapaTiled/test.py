import pilasengine

pilas = pilasengine.iniciar()

mapa = pilas.actores.MapaTiled('test.tmx')

# Genera un personaje en movimiento.
maton = pilas.actores.Maton()


pilas.avisar("Use el teclado para mover al personaje.")

maton.aprender("moversecomocoche")

# Mantiene en ejecución el juego.
pilas.ejecutar()
