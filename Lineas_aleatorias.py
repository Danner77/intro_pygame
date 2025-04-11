import pygame
import sys
import math
import random

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,250,0)
blanco = (255,255,255)
naranja = (255,165,0)
cian = (0,255,255)
colormode = (255)

PI = math.pi

pygame.init()

ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Dibujar formas con pygame")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

############################
# Bucle principal del juego
############################
while True: 
    clock.tick(50)

    # Ciclo para la deteccion de los eventos del juego
    for event in pygame.event.get():
        # Si se hace click en el boton de cerrar la ventana, el juego se termina
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rellenar la ventana de color
    ventana.fill(negro)

    # Dibujar formas con el modulo pygame.draw
    # Texto
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("Colegio Guanenta", 1, blanco )
    ventana.blit(texto,(50,50))

    # Dibujar una linea
    for i in range(100):

        loco1 = random.randint(50,450)
        loco2 = random.randint()
    
    







    # Actualiza la visualizacion del la ventana
    pygame.display.flip()
###################################
# Fin del Bucle principal del juego
###################################