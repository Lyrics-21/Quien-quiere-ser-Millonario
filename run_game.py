import pygame
import random
import sys
from lista_preguntas_game import lista_preguntas
from recursos.colores import *
from funciones_game import retornar_preguntas
from funciones_game import dibujar_figura
from funciones_game import click_cursor
from funciones_game import cursor_en_circulo
from funciones_game import mostrar_publico

pygame.init()

pygame.mixer.init()
##############################################################################

click_sound = pygame.mixer.Sound("EXAMEN/recursos/sounds/Sound_click.mp3")
next_level_sound = pygame.mixer.Sound("EXAMEN/recursos/sounds/next_level.mp3") # Sonidos
end_game_sound = pygame.mixer.Sound("EXAMEN/recursos/sounds/gtav.mp3")

##############################################################################

pygame.display.set_caption("¿QUIEN QUIERE SER MILLONARIO?") #Titulo de ventana
icono = pygame.image.load("EXAMEN/recursos/javier-milei-reivindico-la-libertad-personal-vender-organosss.png") # Icono
pygame.display.set_icon(icono)
titulo = pygame.image.load("EXAMEN/recursos/Sin título-1.png") # Titulo
titulo = pygame.transform.scale(titulo, (800, 700))

###############################################################################

background_image = pygame.image.load("EXAMEN/recursos/FONDO.png")
background_image = pygame.transform.scale(background_image, (1000, 900))
background_image_byn = pygame.image.load("EXAMEN/recursos/FONDObyn.png")
background_image_byn = pygame.transform.scale(background_image_byn, (1000, 900))

imagen_play = pygame.image.load("EXAMEN/recursos/PLAY.png")
imagen_play = pygame.transform.scale(imagen_play, (800, 700))

imagen_quit = pygame.image.load("EXAMEN/recursos/QUIT.png")
imagen_quit = pygame.transform.scale(imagen_quit, (800, 700))
#IMAGENES A USAR
imagen_continuar = pygame.image.load("EXAMEN/recursos/continuar.png") 
imagen_continuar = pygame.transform.scale(imagen_continuar, (700, 600))

imagen_correcto = pygame.image.load("EXAMEN/recursos/CORRECTP.png")
imagen_correcto = pygame.transform.scale(imagen_correcto, (800, 700))

imagen_siguiente_pregunta = pygame.image.load("EXAMEN/recursos/SIGUIENTE.png")
imagen_siguiente_pregunta = pygame.transform.scale(imagen_siguiente_pregunta, (500, 400))

imagen_incorrecto = pygame.image.load("EXAMEN/recursos/INCORRECTO.png")
imagen_incorrecto = pygame.transform.scale(imagen_incorrecto, (800, 700))

#####################################################################################

fuente = pygame.font.SysFont("impact",50)
fuente_grande =  pygame.font.SysFont("impact",30) # Fuentes de texto a usar
fuente_chica =  pygame.font.SysFont("impact",25)

###################################################

VENTANA = pygame.display.set_mode((1000, 900)) #Pixeles
VENTANA.blit(background_image, (0, 0)) # Mostrar pantalla principal

####################################################

clock = pygame.time.Clock()

####################
# Posiciones de los rectangulos para Play y Quit
x_si = 200
y_si_no = 440
x_no = 550
width = 260
height = 100
color_si = GRIS
color_no = GRIS
# Posicioines del titulo
x_titulo = 103
y_titulo = 65
width_titulo = 795
height_titulo = 125

#######################
# Opciones
width_opciones = 300
height_opciones = 80
contador_opciones = 1

# Boton de siguiente pregunta
x_continuar = 340
y_continuar = 370
width_continuar = 320
height_continuar = 80

#####################
# Comodines
color_publico = GRIS
color_llamada = GRIS
color_mitad = GRIS


y_comodin = 670
x_publico = 100
x_llamada = 230
x_mitad = 360

x_estadisticas = 500
y_estadisticas = 610
with_estadisticas = 350
height_estadisticas = 212

x_mostrar_estadisticas = 515

uso_publico = True
uso_llamada = True
uso_mitad = True

##################

flag = True # Bandera del while principal
bandera = True # Bandera del menu
bandera_incorrecto = True # Bandera para el caso de que la opcion sea incorrecta
bandera_correcto = True # Bandera para el caso de que la opcion sea correcta
click_si_no = True # bandera para el click del menu

##########################################

premios = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
contador = 0
mostrar = True # Bandera para mostrar las preguntas y las opciones
lista_posicion_correcta = []
lista_posicion_incorrecta = []
mostrar_correcto = True 
primera_vuelta = False
lista_porcentajes_respuestas = []
score_total = 0

#################

while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == pygame.MOUSEBUTTONUP:
                if click_si_no:
                    bandera_incorrecto = click_cursor(evento, x_no, y_si_no, width, height) # Devuelve False si hace click en QUIT, de lo contrario TRUE
                    bandera_correcto = click_cursor(evento, x_si, y_si_no, width, height) # Devuelve False si hace click en PLAY, de lo contrario TRUE
                    if not bandera_incorrecto or not bandera_correcto: # Si alguno de los dos es FALSE entra
                        click_sound.play()
                        VENTANA.blit(background_image, (0, 0)) # Con esto borra todo lo que hay en pantalla
                        bandera = False # con esto logro que se deje de blitear el Menu
        if evento.type == pygame.MOUSEMOTION: # con este if logro cambiar el color de las opciones del menu si el cursor para por las mismas
            si = click_cursor(evento, x_si, y_si_no, width, height)
            no = click_cursor(evento, x_no, y_si_no, width, height)
            if not si:
                color_si = ROJO
            elif not no:
                color_no = ROJO
        if bandera: # Muestra el Menu
            pygame.draw.rect(VENTANA, color_si, (x_si, y_si_no, width, height))
            pygame.draw.rect(VENTANA, color_no, (x_no, y_si_no, width, height))
            pygame.draw.rect(VENTANA, GRIS, (x_titulo, y_titulo, width_titulo, height_titulo))
            VENTANA.blit(titulo,(100, -145))
            VENTANA.blit(imagen_play, (-67, 218))
            VENTANA.blit(imagen_quit, (282, 218))
            color_si = GRIS
            color_no = GRIS
            
        elif bandera_incorrecto == False: # Este if solo entra si la opcion elegida fue incorrecta
            # Devuelvo toas las variables necesarias a su estado de inicio
            bandera_correcto = True
            click_si_no = False
            uso_publico = True
            uso_llamada = True
            uso_mitad = True
            color_publico = GRIS
            color_llamada = GRIS
            color_mitad = GRIS
            # Muestra cajas de texto ya sea Quit Continuar o El score total
            pygame.draw.rect(VENTANA, GRIS, (x_titulo, y_titulo, width_titulo, height_titulo))
            pygame.draw.rect(VENTANA, GRIS, (x_si, y_si_no, width, height))
            pygame.draw.rect(VENTANA, GRIS, (x_no, y_si_no, width, height))
            pygame.draw.rect(VENTANA, GRIS, (x_no, y_si_no, width, height))
            VENTANA.blit(imagen_incorrecto,(100, -145))
            VENTANA.blit(imagen_quit, (282, 218))
            VENTANA.blit(imagen_continuar, (-18, 258))
            texto_score_total = fuente.render((f"Score  :  {score_total} $"),True, BLANCO, GRIS)
            VENTANA.blit(texto_score_total, (364, 285))

            if evento.type == pygame.MOUSEMOTION: # Esto cambiar el color de las opciones del menu si el cursor para por las mismas
                boton_continuar = click_cursor(evento, x_si, y_si_no, width, height)
                boton_salir = click_cursor(evento, x_no, y_si_no, width, height)
                if not boton_continuar:
                    pygame.draw.rect(VENTANA, ROJO, (x_si, y_si_no, width, height), 4)
                else:
                    pygame.draw.rect(VENTANA, GRIS, (x_si, y_si_no, width, height), 4)
                if not boton_salir:
                    pygame.draw.rect(VENTANA, ROJO, (x_no, y_si_no, width, height), 4)
                else:
                    pygame.draw.rect(VENTANA, GRIS, (x_no, y_si_no, width, height), 4)

            if evento.type == pygame.MOUSEBUTTONUP: # Dentro de este if valido si hice click en la opcion en Conttinuar o Quit
                click_continuar = click_cursor(evento, x_si, y_si_no, width, height)
                click_salir = click_cursor(evento, x_no, y_si_no, width, height)
                if not click_continuar: # en el caso de que presione Continuar, procedo a resetear todas laas variables a su estado inicial
                    end_game_sound.stop()
                    click_sound.play()
                    VENTANA.blit(background_image, (0, 0))
                    lista_posicion_correcta.clear() # Borro las posocion de la opcion correcta
                    lista_posicion_incorrecta.clear() # Borro las posiciones de las distintas opciones incorrectas
                    bandera = True
                    bandera_incorrecto = True
                    bandera_correcto = True
                    click_si_no = True
                    contador = 0
                    mostrar = True
                    mostrar_correcto = True
                    primera_vuelta = False
                    contador_opciones = 1
                elif not click_salir: # En el caso que presione Quit sale del juego
                    click_sound.play()
                    VENTANA.blit(background_image, (0, 0))
                    flag = False

        elif bandera_correcto == False: # Este if funciona como condicional mas abajo en el codigo
            click_si_no = False
            if mostrar: # Dentro de este if muestro las ocpiones la pregunta el score y los comodines
                lista = retornar_preguntas(lista_preguntas, premios[contador])
                score_inicial = premios[contador]
                score_total += score_inicial
                contador += 1
                num_random = random.randint(0, len(lista)-1)
                pregunta = lista[num_random]["Pregunta"]
                respuestas = lista[num_random]["Respuestas_incorrectas"]
                respuesta_correcta = lista[num_random]["Respuesta_correcta"]

                for i in respuestas: # este for cumple la funcion de cambiar la posicion de las opciones para blitearlas
                    match contador_opciones:
                        case 1:
                            x = 150
                            y = 280
                        case 2:
                            x = 550
                            y = 280 
                        case 3: 
                            x = 150
                            y = 450
                        case 4:
                            x = 550
                            y = 450
                    # El codigo siguiente sirve para centrar las opciones a las cajas de textos y mostrarlas
                    opciones = fuente_chica.render((f"{contador_opciones}  -  " + i ),True, BLANCO, GRIS)
                    opciones_rect = opciones.get_rect()
                    destino_opciones = pygame.Rect(x, y, width_opciones, height_opciones)
                    opciones_rect.center = destino_opciones.center
                    pygame.draw.rect(VENTANA, GRIS, destino_opciones)
                    VENTANA.blit(opciones, opciones_rect)
                    contador_opciones += 1

                    ###########################################
                    # Esto es importarte para utilizarlo mas adelante
                    if i == respuesta_correcta: # Agrego a la lista posicion_correcta la x e y donde se encuentra la opcion correcta en la pregunta en pantalla
                        lista_posicion_correcta.append(x)
                        lista_posicion_correcta.append(y)
                    else: # Agrego a la lista posicion_incorrecta la x e y donde se encuentran las opciones incorrectas
                        lista_posicion_incorrecta.append(x)
                        lista_posicion_incorrecta.append(y)
                    ###############################################
                # Aca muestro la pregunta y la centro
                texto_pregunta = fuente_grande.render(pregunta, True, BLANCO, GRIS)
                texto_pregunta_rect = texto_pregunta.get_rect()
                destino = pygame.Rect(x_titulo, y_titulo, width_titulo, height_titulo)
                texto_pregunta_rect.center = destino.center
                pygame.draw.rect(VENTANA, GRIS, destino)
                VENTANA.blit(texto_pregunta,texto_pregunta_rect)
                ####################################################################
                # Muestro los comodines con sus inconos
                pygame.draw.circle(VENTANA, color_publico, (x_publico, y_comodin), 50)
                pygame.draw.circle(VENTANA, color_llamada, (x_llamada, y_comodin), 50)
                pygame.draw.circle(VENTANA, color_mitad, (x_mitad, y_comodin), 50)
                incono_publico = fuente.render("P", True, BLANCO, color_publico)
                VENTANA.blit(incono_publico, (89, 640))
                incono_llamada = fuente.render("C", True, BLANCO, color_llamada)
                VENTANA.blit(incono_llamada, (217, 640))
                incono_mitad = fuente_grande.render("50/50", True, BLANCO, color_mitad)
                VENTANA.blit(incono_mitad, (323, 653))
                ######################################################################
                # Y por ultimo muestro los score
                mostrar_premio = fuente_grande.render(f"PREGUNTA  POR  :  {premios[contador-1]}  $", True, BLANCO, GRIS)
                VENTANA.blit(mostrar_premio, (104, 25))
                score = fuente.render(f"Score  :  {score_total}", True, BLANCO, GRIS)
                VENTANA.blit(score, (110, 780))
                mostrar = False # Con esto dejo de mostrar todo lo anterior pero no lo borro
            ################################################################################################################################
            # si paso el cursor por cualquiera de las cajas de texto genero un recuadro rojo al rededor de lo contrario queda igual
            if evento.type == pygame.MOUSEMOTION and not primera_vuelta:
                primera_opcion = click_cursor(evento, lista_posicion_correcta[0], lista_posicion_correcta[1], width_opciones, height_opciones)
                segunda_opcion = click_cursor(evento, lista_posicion_incorrecta[0], lista_posicion_incorrecta[1], width_opciones, height_opciones)
                tercera_opcion = click_cursor(evento, lista_posicion_incorrecta[2], lista_posicion_incorrecta[3], width_opciones, height_opciones)
                cuarta_opcion = click_cursor(evento, lista_posicion_incorrecta[4], lista_posicion_incorrecta[5], width_opciones, height_opciones)
                publico_cursor = cursor_en_circulo(evento, x_publico, y_comodin, 50)
                llamada_cursor = cursor_en_circulo(evento, x_llamada, y_comodin, 50)
                mitad_cursor = cursor_en_circulo(evento, x_mitad, y_comodin, 50)

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

                if publico_cursor:
                    dibujar_figura("circle", VENTANA, ROJO, [], x_publico, y_comodin, 0, 0, 4, 50)
                else:
                    dibujar_figura("circle", VENTANA, GRIS, [], x_publico, y_comodin, 0, 0, 4, 50)
                if llamada_cursor:
                    dibujar_figura("circle", VENTANA, ROJO, [], x_llamada, y_comodin, 0, 0, 4, 50)
                else:
                    dibujar_figura("circle", VENTANA, GRIS, [], x_llamada, y_comodin, 0, 0, 4, 50)
                if mitad_cursor:
                    dibujar_figura("circle", VENTANA, ROJO, [], x_mitad, y_comodin, 0, 0, 4, 50)
                else:
                    dibujar_figura("circle", VENTANA, GRIS, [], x_mitad , y_comodin, 0, 0, 4, 50)
                
                mostrar_correcto = False # esta bandera da paso a el codigo siguiente pero no da paso a otros if de mas abajo
                ######################################################################################################################################
            if evento.type == pygame.MOUSEBUTTONUP and not mostrar_correcto: # valido en que comodin hizo click
                click_publico = cursor_en_circulo(evento, x_publico, y_comodin, 50)
                click_llamada = cursor_en_circulo(evento, x_llamada, y_comodin, 50)
                click_mitad = cursor_en_circulo(evento, x_mitad, y_comodin, 50)

                
                if click_publico and uso_publico: # Entra as este if por una vez mientras no pierdas
                    click_sound.play()
                    pygame.draw.rect(VENTANA, GRIS, (x_estadisticas, y_estadisticas, with_estadisticas, height_estadisticas))
                    lista_porcentajes_respuestas = mostrar_publico(lista, num_random)
                    contador_estadisticas = 1
                    for i in lista_porcentajes_respuestas: # Muestra las estadisticas con la misma logica que mostre las opciones de las preguntas
                        match contador_estadisticas:
                            case 1:
                                y_mostrar_estadisticas = 620
                            case 2:
                                y_mostrar_estadisticas = 670
                            case 3:
                                y_mostrar_estadisticas = 723
                            case 4:
                                y_mostrar_estadisticas = 775
                        mostrar_estadisticas = fuente_grande.render(f"{i}", True, BLANCO, GRIS)
                        VENTANA.blit(mostrar_estadisticas, (x_mostrar_estadisticas, y_mostrar_estadisticas))
                        contador_estadisticas += 1
                        uso_publico = False
                else:
                    if not uso_publico:
                        color_publico = ROJO # Si se uso el comodin lo pinto de rojo

                if click_llamada and uso_llamada:
                    click_sound.play()
                    mostrar_llamada = fuente_grande.render(respuesta_correcta, True, BLANCO, GRIS)
                    pygame.draw.rect(VENTANA, GRIS, (x_estadisticas, y_estadisticas, with_estadisticas, height_estadisticas))
                    VENTANA.blit(mostrar_llamada, (x_mostrar_estadisticas, 695))
                    uso_llamada = False
                else:
                    if not uso_llamada:
                        color_llamada = ROJO # Si se uso el comodin lo pinto de rojo

                if click_mitad and uso_mitad: # En este if utilizo las listas de opciones correctas e incorrectas
                    click_sound.play()
                    #Dibuja un rectangulo negro en 2 opciones incorrectas
                    pygame.draw.rect(VENTANA, NEGRO, (lista_posicion_incorrecta[0], lista_posicion_incorrecta[1], width_opciones, height_opciones))
                    pygame.draw.rect(VENTANA, NEGRO, (lista_posicion_incorrecta[2], lista_posicion_incorrecta[3], width_opciones, height_opciones))
                    uso_mitad = False
                else:
                    if not uso_mitad:
                        color_mitad = ROJO # Si se uso el comodin lo pinto de rojo

                ################################################################################################################################
                # Valido si hizo click en una opcion incorrecta o en la correcta con las posiciones que agregue a las listas de opciones correctas e incorrectas
                segunda_etapa = click_cursor(evento, lista_posicion_correcta[0], lista_posicion_correcta[1], width_opciones, height_opciones)
                segunda_etapa_incorrecto = click_cursor(evento, lista_posicion_incorrecta[0], lista_posicion_incorrecta[1], width_opciones, height_opciones)
                segunda_etapa_incorrecto1 = click_cursor(evento, lista_posicion_incorrecta[2], lista_posicion_incorrecta[3], width_opciones, height_opciones)
                segunda_etapa_incorrecto2 = click_cursor(evento, lista_posicion_incorrecta[4], lista_posicion_incorrecta[5], width_opciones, height_opciones)
                if not segunda_etapa: #Si hizo click en la opcion correcta cambia de estado las flag
                    click_sound.play()
                    next_level_sound.play()
                    mostrar_correcto = True # Esto tambien desactiva los click en los comodines y activa el if de mas abajo
                    primera_vuelta = True # Esto desactiva la parte donde se genera un recuadro rojo si paso el cursor
                elif not segunda_etapa_incorrecto or not segunda_etapa_incorrecto1 or not segunda_etapa_incorrecto2: # Si es incorrecto borra todo 
                    click_sound.play()
                    end_game_sound.play()
                    VENTANA.blit(background_image_byn, (0, 0))
                    bandera_incorrecto = False # Ademas de borrar todo vuelve a la parte de arriba y activa bel if de incorrectos
                ###############################################################################################################################

            if evento.type == pygame.MOUSEBUTTONUP and mostrar_correcto and primera_vuelta: #siempre y cuando haya hecho click en la opcion correcta entra al if
                # Me borra todo y muesta la caja de siguiente pregunta
                VENTANA.blit(background_image, (0, 0))
                pygame.draw.rect(VENTANA, GRIS, (x_continuar, y_continuar, width_continuar, height_continuar))
                pygame.draw.rect(VENTANA, GRIS, (x_titulo, y_titulo, width_titulo, height_titulo))
                VENTANA.blit(imagen_correcto, (100, -145))
                VENTANA.blit(imagen_siguiente_pregunta,(250, 255))

                presiono_siguiente_pregunta = click_cursor(evento, x_continuar, y_continuar, width_continuar, height_continuar)
                if not presiono_siguiente_pregunta: # Si presiono siguiente pregunta me resetea determinadas variables y listas
                    click_sound.play()
                    VENTANA.blit(background_image, (0, 0))
                    lista_posicion_correcta.clear() # Me borra estas listas para volver a reutilizarlas otra vez sin problemas
                    lista_posicion_incorrecta.clear()
                    mostrar = True # Con esto activo de vuelta el if de mostrar preguntas y opciones
                    contador_opciones = 1 # Vuelvo a poner en uno el contador para mostrar las opciones
                    mostrar_correcto = True
                    primera_vuelta = False # al cambiar de estado esta flag sale de est if del anterior para poder volver a mostrar las preguntas sin problemas

            if evento.type == pygame.MOUSEMOTION and mostrar_correcto: # este if funciona para pintar de rojo si paso el cursor por las cajas de texto
                cursor_en_siguiente_pregunta = click_cursor(evento, x_continuar, y_continuar, width_continuar, height_continuar)
                if not cursor_en_siguiente_pregunta:
                    pygame.draw.rect(VENTANA, ROJO, (x_continuar, y_continuar, width_continuar, height_continuar), 4)
                else:
                    pygame.draw.rect(VENTANA, GRIS, (x_continuar, y_continuar, width_continuar, height_continuar), 4)
                
    pygame.display.update()

pygame.quit()
sys.exit()










