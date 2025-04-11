import pygame
import sys
import math

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,250,0)
blanco = (255,255,255)
naranja = (255,165,0)
cian = (0,255,255)
gris = (50,50,50)
celeste = (135,206,235)

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
    ventana.fill(celeste)

    # circulo del frente
    pygame.draw.circle(ventana,gris, (75,250), 50, 50)


    # Dibujar formas con el modulo pygame.draw

    # Dibujar una linea
    

    # Dibujar una linea discontinua
    # True: crea un poligono
    
    # Dibujar un rectangulo
    # Rectangulo relleno, ubicado en la coordenada sup, izq, (200,200), y de ancho 200 y altura 100
    pygame.draw.rect(ventana,azul, (100,200, 225,100))
    pygame.draw.rect(ventana,negro, (95,300, 200,20))
    pygame.draw.rect(ventana,negro, (200,85, 135,20))
    pygame.draw.rect(ventana,negro, (85,200, 25,95))
    pygame.draw.rect(ventana,negro, (85,200, 25,95))
    pygame.draw.rect(ventana,gris, (70,175, 30,150))
    pygame.draw.rect(ventana,rojo, (120,150, 35,50))
    pygame.draw.rect(ventana,gris, (118,150, 40,15))
    pygame.draw.rect(ventana,blanco, (300,20, 100,10))
    
    # Rectangulo sin relleno, esquina sup. izq: (100,100), esquina. inf.der: (150,200). Y de grosor 1.
    pygame.draw.rect(ventana,rojo, ((220,100), (100,100)),20)

    # Dibujar un poligono
    

    # Dibujar un circulo
    # Centro del circulo: (300,100)
    # Radio del circulo: 100
    # Grosor contorno del circulo: 1
    pygame.draw.circle(ventana,gris, (295,320), 40, 50)
    pygame.draw.circle(ventana,gris, (213,320), 40, 50)
    pygame.draw.circle(ventana,gris, (130,320), 40, 50)
    pygame.draw.circle(ventana,amarillo, (270,150), 35, 50)


    # Texto
    # Fuente de tipo arial, tamaño 35, negrilla y cursiva
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("Sistemas Guanenta", 1, blanco )
    ventana.blit(texto,(50,50))

    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("no se XD", 1, blanco )
    ventana.blit(texto,(150,205))


    # Actualiza la visualizacion del la ventana
    pygame.display.flip()


    Clock = pygame.time.Clock()

    XX = 300
    MOVIMIENTO = 3

    while 1:
        Clock.tick(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            

    XX = XX + MOVIMIENTO

    if XX >= 320:
        XX = 320
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3

    pygame.draw.rect(ventana, blanco, (XX, 100, 50, 50))
    pygame.display.flip()



###################################
# Fin del Bucle principal del juego
###################################