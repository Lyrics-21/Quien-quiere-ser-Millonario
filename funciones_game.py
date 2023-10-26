import random
import pygame

def dibujar_figura(figura : str, pantalla : str, color : str, lista : list, posicion : int, segunda_posicion : int, width : int, height : int, borde : int, radio : int):
    if figura == "rect":
        pygame.draw.rect(pantalla, color, (lista[posicion], lista[segunda_posicion], width, height), borde)
    elif figura == "circle":
        pygame.draw.circle(pantalla, color, (posicion, segunda_posicion), radio, borde)
        
def click_cursor(evento, x, y, width, height):
    pos_x = evento.pos[0]
    pos_y = evento.pos[1]
    if pos_x >= x and pos_x <= (x + width) and pos_y >= y and pos_y <= (y + height):
        return False
    return True

def cursor_en_circulo(evento, x_circulo, y_circulo, radio):
    pos_x_cursor, pos_y_cursor = evento.pos
    distancia_al_centro = ((pos_x_cursor - x_circulo)**2 + (pos_y_cursor - y_circulo)**2)**0.5
    return distancia_al_centro <= radio

def generar_porcentajes():
    lista_destino = [0, 0, 0, 0]
    for _ in range(100):
        numero = random.choices([0, 1, 2, 3], weights=[50, 10, 20, 10])[0]#el cero a lo ultimo es para agarrar el primer numero de la lista que devuelve random
        lista_destino[numero] += 1#si no tuviera ese [0] no podria usar numero como key, ya que es de tipo lista
    return lista_destino

def mostrar_publico(lista, num_random):
    lista_comodin = []
    contador = 0
    respuestas_incorrectas = lista[num_random]["Respuestas_incorrectas"]
    respuesta_correcta = lista[num_random]["Respuesta_correcta"]
    respuestas_incorrectas.remove(respuesta_correcta)# Remueve la respuesta correcta
    respuestas_incorrectas.insert(0, respuesta_correcta)# Inserta la respuesta correcta en la posición 0
    lista_porcentajes = generar_porcentajes()
    for _ in lista_porcentajes:
        lista_comodin.append(f'{respuestas_incorrectas[contador]} - {lista_porcentajes [contador]}%')
        contador += 1
    return lista_comodin

def retornar_preguntas(lista: list, valor_premio:int):
    lista_valor_premio = []
    for pregunta in lista:
        premio = pregunta["premio"]
        if premio == valor_premio:
            lista_valor_premio.append(pregunta)
    return lista_valor_premio

def mostrar_preguntas(lista: list):
    contador = 1
    num_random = random.randint(0, len(lista)-1)
    pregunta = lista[num_random]["Pregunta"]
    respuestas = lista[num_random]["Respuestas_incorrectas"]
    print(f"{pregunta}")
    for i in respuestas:
        print(f"{contador} - {i}")
        contador += 1
    return num_random


        

        
            
