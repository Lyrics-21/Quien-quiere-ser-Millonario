if not primera_opcion:
dibujar_figura("rect", VENTANA, ROJO, lista_posicion_correcta, 0, 1, width_opciones, height_opciones, 4, 0)
else:
dibujar_figura("rect", VENTANA, GRIS, lista_posicion_correcta, 0, 1, width_opciones, height_opciones, 4, 0)
if not segunda_opcion:
dibujar_figura("rect", VENTANA, ROJO, lista_posicion_incorrecta, 0, 1, width_opciones, height_opciones, 4, 0)
else:
dibujar_figura("rect", VENTANA, GRIS, lista_posicion_incorrecta, 0, 1, width_opciones, height_opciones, 4, 0)
if not tercera_opcion:
dibujar_figura("rect", VENTANA, ROJO, lista_posicion_incorrecta, 2, 3, width_opciones, height_opciones, 4, 0)
else:
dibujar_figura("rect", VENTANA, GRIS, lista_posicion_incorrecta, 2, 3, width_opciones, height_opciones, 4, 0)
if not cuarta_opcion:
dibujar_figura("rect", VENTANA, ROJO, lista_posicion_incorrecta, 4, 5, width_opciones, height_opciones, 4, 0)
else:
dibujar_figura("rect", VENTANA, GRIS, lista_posicion_incorrecta, 4, 5, width_opciones, height_opciones, 4, 0)

opciones = [
    (lista_posicion_correcta, GRIS),
    (lista_posicion_incorrecta, ROJO),
    (lista_posicion_incorrecta, ROJO),
    (lista_posicion_incorrecta, ROJO)
]

for i, (opcion, color) in enumerate(opciones):
    indices = (i * 2, i * 2 + 1)
    if not primera_vuelta:
        dibujar_figura("rect", VENTANA, color, opcion, indices[0], indices[1], width_opciones, height_opciones, 4, 0)