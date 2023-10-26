import pygame
import random
import sys
from lista_preguntas_game import lista_preguntas
from funciones_game import retornar_preguntas
from funciones_game import dibujar_figura
from funciones_game import click_cursor
from funciones_game import cursor_en_circulo
from funciones_game import mostrar_publico

BLANCO = (255,255,255)
NEGRO = (0,0,0,)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
GRIS = (128, 128, 128)

pygame.init()

VENTANA = pygame.display.set_mode((1000,900)) #Pixeles
pygame.display.set_caption("¿Quien quirere ser millonario?") #Titulo de ventana
VENTANA.fill(NEGRO) #Color del fondo
fuente = pygame.font.SysFont("impact",50)
fuente_grande =  pygame.font.SysFont("impact",30)
fuente_chica =  pygame.font.SysFont("impact",25)
clock = pygame.time.Clock()

#cajas preguntas
x_si = 200
y_si_no = 450
x_no = 550
width = 250
height = 80
color_si = GRIS
color_no = GRIS


x_titulo = 100
y_titulo = 100
width_titulo = 800
height_titulo = 100

width_opciones = 300
height_opciones = 80
contador_opciones = 1

x_continuar = 350
y_continuar = 370
width_continuar = 300
height_continuar = 80

#####################

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

flag = True
bandera = True
bandera_incorrecto = True
bandera_correcto = True
click_si_no = True

##########################################

premios = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
contador = 0
mostrar = True
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
                    bandera_incorrecto = click_cursor(evento, x_no, y_si_no, width, height)
                    bandera_correcto = click_cursor(evento, x_si, y_si_no, width, height)
                    if not bandera_incorrecto or not bandera_correcto:
                        VENTANA.fill(NEGRO)
                        bandera = False
        if evento.type == pygame.MOUSEMOTION:
            si = click_cursor(evento, x_si, y_si_no, width, height)
            no = click_cursor(evento, x_no, y_si_no, width, height)
            if not si:
                color_si = ROJO
            elif not no:
                color_no = ROJO
        if bandera:
            primer_texto = fuente.render(f"¿Estas  listo  para  jugar?",True,BLANCO, NEGRO)
            pygame.draw.rect(VENTANA, color_si, (x_si, y_si_no, width, height))
            pygame.draw.rect(VENTANA, color_no, (x_no, y_si_no, width, height))
            caja_si = fuente.render(f"SI",True,BLANCO, color_si)
            caja_no = fuente.render(f"NO",True,BLANCO, color_no)
            VENTANA.blit(primer_texto,(265,300))
            VENTANA.blit(caja_si,(305,460))
            VENTANA.blit(caja_no,(645,460))
            color_si = GRIS
            color_no = GRIS
            
        elif bandera_incorrecto == False:
            bandera_correcto = True
            fin = False
            click_si_no = False
            uso_publico = True
            uso_llamada = True
            uso_mitad = True
            color_publico = GRIS
            color_llamada = GRIS
            color_mitad = GRIS

            fin_del_juego_texto = fuente.render("FIN DEL JUEGO",True, BLANCO, NEGRO)
            x_fin_del_juego_texto = (VENTANA.get_width() - fin_del_juego_texto.get_width()) // 2
            VENTANA.blit(fin_del_juego_texto,(x_fin_del_juego_texto, 300))

            desea_continuar = fuente_grande.render("CONTINUAR", True, BLANCO, GRIS)
            salir = fuente_grande.render("NO", True, BLANCO, GRIS)
            desea_continuar_rect = desea_continuar.get_rect()
            salir_rect = salir.get_rect()
            destino_desea_continuar = pygame.Rect(x_si, y_si_no, width, height)
            destino_salir = pygame.Rect(x_no, y_si_no, width, height)
            desea_continuar_rect.center = destino_desea_continuar.center
            salir_rect.center = destino_salir.center
            pygame.draw.rect(VENTANA, GRIS, destino_desea_continuar)
            pygame.draw.rect(VENTANA, GRIS, destino_salir)
            VENTANA.blit(desea_continuar, desea_continuar_rect)
            VENTANA.blit(salir, salir_rect)

            if evento.type == pygame.MOUSEMOTION:
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

            if evento.type == pygame.MOUSEBUTTONUP:
                click_continuar = click_cursor(evento, x_si, y_si_no, width, height)
                click_salir = click_cursor(evento, x_no, y_si_no, width, height)
                if not click_continuar:
                    VENTANA.fill(NEGRO)
                    lista_posicion_correcta.clear()
                    lista_posicion_incorrecta.clear()
                    bandera = True
                    bandera_incorrecto = True
                    bandera_correcto = True
                    click_si_no = True
                    contador = 0
                    mostrar = True
                    mostrar_correcto = True
                    primera_vuelta = False
                    contador_opciones = 1
                elif not click_salir:
                    VENTANA.fill(NEGRO)
                    flag = False

        elif bandera_correcto == False:
            click_si_no = False
            if mostrar:
                lista = retornar_preguntas(lista_preguntas, premios[contador])
                score_inicial = premios[contador]
                score_total += score_inicial
                contador += 1
                num_random = random.randint(0, len(lista)-1)
                pregunta = lista[num_random]["Pregunta"]
                respuestas = lista[num_random]["Respuestas_incorrectas"]
                respuesta_correcta = lista[num_random]["Respuesta_correcta"]

                for i in respuestas:
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
                    opciones = fuente_chica.render((f"{contador_opciones}  -  " + i ),True, BLANCO, GRIS)
                    opciones_rect = opciones.get_rect()
                    destino_opciones = pygame.Rect(x, y, width_opciones, height_opciones)
                    opciones_rect.center = destino_opciones.center
                    pygame.draw.rect(VENTANA, GRIS, destino_opciones)
                    VENTANA.blit(opciones, opciones_rect)
                    contador_opciones += 1
                    if i == respuesta_correcta:
                        lista_posicion_correcta.append(x)
                        lista_posicion_correcta.append(y)
                    else:
                        lista_posicion_incorrecta.append(x)
                        lista_posicion_incorrecta.append(y)
                
                texto_pregunta = fuente_grande.render(pregunta, True, BLANCO, GRIS)
                texto_pregunta_rect = texto_pregunta.get_rect()
                destino = pygame.Rect(x_titulo, y_titulo, width_titulo, height_titulo)
                texto_pregunta_rect.center = destino.center
                pygame.draw.rect(VENTANA, GRIS, destino)
                VENTANA.blit(texto_pregunta,texto_pregunta_rect)

                pygame.draw.circle(VENTANA, color_publico, (x_publico, y_comodin), 50)
                pygame.draw.circle(VENTANA, color_llamada, (x_llamada, y_comodin), 50)
                pygame.draw.circle(VENTANA, color_mitad, (x_mitad, y_comodin), 50)
                incono_publico = fuente.render("P", True, BLANCO, color_publico)
                VENTANA.blit(incono_publico, (89, 640))
                incono_llamada = fuente.render("C", True, BLANCO, color_llamada)
                VENTANA.blit(incono_llamada, (217, 640))
                incono_mitad = fuente_grande.render("50/50", True, BLANCO, color_mitad)
                VENTANA.blit(incono_mitad, (323, 653))

                mostrar_premio = fuente_grande.render(f"PREGUNTA  POR  :  {premios[contador-1]}  $", True, BLANCO, GRIS)
                VENTANA.blit(mostrar_premio, (100, 30))
                score = fuente.render(f"Score  :  {score_total}", True, BLANCO, GRIS)
                VENTANA.blit(score, (110, 780))
                mostrar = False

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
                
                mostrar_correcto = False

            if evento.type == pygame.MOUSEBUTTONUP and not mostrar_correcto:
                click_publico = cursor_en_circulo(evento, x_publico, y_comodin, 50)
                click_llamada = cursor_en_circulo(evento, x_llamada, y_comodin, 50)
                click_mitad = cursor_en_circulo(evento, x_mitad, y_comodin, 50)
                
                if click_publico and uso_publico:
                    pygame.draw.rect(VENTANA, GRIS, (x_estadisticas, y_estadisticas, with_estadisticas, height_estadisticas))
                    lista_porcentajes_respuestas = mostrar_publico(lista, num_random)
                    contador_estadisticas = 1
                    for i in lista_porcentajes_respuestas:
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
                        color_publico = ROJO

                if click_llamada and uso_llamada:
                    mostrar_llamada = fuente_grande.render(respuesta_correcta, True, BLANCO, GRIS)
                    pygame.draw.rect(VENTANA, GRIS, (x_estadisticas, y_estadisticas, with_estadisticas, height_estadisticas))
                    VENTANA.blit(mostrar_llamada, (x_mostrar_estadisticas, 695))
                    uso_llamada = False
                else:
                    if not uso_llamada:
                        color_llamada = ROJO

                if click_mitad and uso_mitad:
                    pygame.draw.rect(VENTANA, NEGRO, (lista_posicion_incorrecta[0], lista_posicion_incorrecta[1], width_opciones, height_opciones))
                    pygame.draw.rect(VENTANA, NEGRO, (lista_posicion_incorrecta[2], lista_posicion_incorrecta[3], width_opciones, height_opciones))
                    uso_mitad = False
                else:
                    if not uso_mitad:
                        color_mitad = ROJO

                segunda_etapa = click_cursor(evento, lista_posicion_correcta[0], lista_posicion_correcta[1], width_opciones, height_opciones)
                segunda_etapa_incorrecto = click_cursor(evento, lista_posicion_incorrecta[0], lista_posicion_incorrecta[1], width_opciones, height_opciones)
                segunda_etapa_incorrecto1 = click_cursor(evento, lista_posicion_incorrecta[2], lista_posicion_incorrecta[3], width_opciones, height_opciones)
                segunda_etapa_incorrecto2 = click_cursor(evento, lista_posicion_incorrecta[4], lista_posicion_incorrecta[5], width_opciones, height_opciones)
                if not segunda_etapa:
                    mostrar_correcto = True
                    primera_vuelta = True
                elif not segunda_etapa_incorrecto or not segunda_etapa_incorrecto1 or not segunda_etapa_incorrecto2:
                    VENTANA.fill(NEGRO)
                    bandera_incorrecto = False

            if evento.type == pygame.MOUSEBUTTONUP and mostrar_correcto and primera_vuelta:
                VENTANA.fill(NEGRO)
                respuesta = fuente.render("¡CORRECTO!",True, BLANCO, NEGRO)
                x_respuesta = (VENTANA.get_width() - respuesta.get_width()) // 2
                y_respuesta = 250
                
                continuar = fuente_grande.render("Siguiente Pregunta", True, BLANCO, GRIS)
                continuar_rect = continuar.get_rect()
                destino_continuar = pygame.Rect(x_continuar, y_continuar, width_continuar, height_continuar)
                continuar_rect.center = destino_continuar.center
                pygame.draw.rect(VENTANA, GRIS, destino_continuar)
                VENTANA.blit(continuar, continuar_rect)
                VENTANA.blit(respuesta,(x_respuesta, y_respuesta))
                presiono_siguiente_pregunta = click_cursor(evento, x_continuar, y_continuar, width_continuar, height_continuar)
                if not presiono_siguiente_pregunta:#######reset#######
                    VENTANA.fill(NEGRO)
                    lista_posicion_correcta.clear()
                    lista_posicion_incorrecta.clear()
                    mostrar = True
                    contador_opciones = 1
                    mostrar_correcto = True
                    primera_vuelta = False

            if evento.type == pygame.MOUSEMOTION and mostrar_correcto:
                cursor_en_siguiente_pregunta = click_cursor(evento, x_continuar, y_continuar, width_continuar, height_continuar)
                if not cursor_en_siguiente_pregunta:
                    pygame.draw.rect(VENTANA, ROJO, (x_continuar, y_continuar, width_continuar, height_continuar), 4)
                else:
                    pygame.draw.rect(VENTANA, GRIS, (x_continuar, y_continuar, width_continuar, height_continuar), 4)
                
    pygame.display.update()

pygame.quit()
sys.exit()










