# importamos la libreria pygame 
import pygame 

# inicializamos los modulos dde pygame 
pygame.init()

# establecer titulo a la ventana
pygame.display.set_caption("surface")

# Estableces las dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# definimos color
azul = (0,0,255)
amarillo = (255,255,0)
rojo = (255,0,0)

# crear una superficie 
azul_superficie = pygame.Surface((400,100))
amarillo_superficie = pygame.Surface((400,200))
rojo_superficie = pygame.Surface((400,100))


# Rellenamos la superficie de azul
azul_superficie.fill(azul)
amarillo_superficie.fill(amarillo)
rojo_superficie.fill(rojo)


# Insertar a nueva superficie en la ventana
ventana.blit(amarillo_superficie, (0,0))
ventana.blit(azul_superficie, (0,200))
ventana.blit(rojo_superficie, (0,300))

#actualiza la visualizacion de la ventana
pygame.display.flip()

#bucle de juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()

