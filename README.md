# Estructura de un juego en pygame

## inicializacion

- como en todo programa en pythonse debe inportar los modulos o librerias a utilizar
``import pygame``

- inicializar pygame con la funcion init (). Inicializa todos los modulos de pygame importados.
`pygame.init()`

## Visualizacion de la ventana 

`ventana = pygame.display.set_mode((600,400))`

- set mode() es la funcion encargada  de definir el tamaño de la ventana. en el ejemplo, se esta definiendo una ventana de 600px de ancho, por 400px de alto.

``pygame.display.set_caption"¡ "mi ventana"

set_caption() es la funcion que añade un titulo a la ventana.

### Funcion set_mode

- set_mode(size = (0,0), flags = 0, depth = 0, display = 0)

size = (600,400) : define el tamaño de la ventana.

- flags: define uno o mas comportamientos para la ventana:
    
       valores:
         pygame.FULLSCREEN
         pygame.REZIZABLE
       ejemplo:
         flags = pygame.FULLSCREEN | pygame.
        REZIZABLE: pantalla completa.
        dimennsiones modificadas.

## bucle de el juego - game loop
- bucle infinito que se interumpira al cumplir certos criterios.
- Reloj interno de el juego
- En cada iteracion de el bucle de el juego podemos mover a un personaje. o tener en cuenta que un objeto a alcanzado a otro o que se a cruzado la linea de llegada lo quiere decir que la partida a terminado.
- Cada iteracion es una oportunidad para actualizar todos los datos relacionados con el estado actual de la partida
- En cada iteracion se realizan las siguientes tareas: 

 1. comprobar que no se alcanzan las condiciones de parada, en cuyo caso se interumpe el bucle
 2. actualizar los recursos necesarios para la iteracion actualizar
 3. obtener las entradas de el sistema, o de interaccion con el jugador.
 4. Actualizar todas las entidades que caracterizan el juego.
 5. Refescar la pantalla.

 ## Superficies pygame
 -superficie:
  - Elemento geometrico.
  - Linea, poligono, imagen, texto que se muestra en la pantalla.
  - El poligono se puede o no rellenar de color.
  - las superficies se crean de diferente manera dependiendo de el tipo:
        
        imagen: image.load()

        texto: font.render()

        superficie generica: pygame.Surface()

        ventana del juego: pygame.display.set_mode()

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

pygame.quit()```


## gestion de tiempo y los eventos

### modulo time

- este modulo ofrece varioas funciones que permiten cronometrar la secion actual desde el init() o pausar la ejecucion, por ejemplo.
- funciones:
   - pygame.time.get_ticks
   - pygame.time.waitpygame.time.delay

- Objeto clock
  - la funcion tick permite actualizar el reloj asosiado con el juego actual.
  - se llama cada vez que se actualiza la pantalla del juego.
  - permite especifiar el numero maximo de fotogramas que se muestran por segundo,  y por tanto, limitar y controlar la velocidad del ejecucion.
  - si insertamos en un bucle de juego la siguiente linea, garantizamos que nunca se ira ,mas rapido de 50 fotogramas por segundo: 
`clock_tick(50)`

### Gestion de eventos 

- hay diferentes formas para que el programa sepa que se genero un evento.
- es esencial que los programas puedan conocer inmediatamente las accions de el jugador a travez de el teclado,mouse,joystick o cualquier otro periferico. 
 
 #### funcion pygame.event.get
 - permite obtener todos los eventos en espera de ser proceados y que estan disponobles en una cola

 - si no hay ninguno, entoces se obtine una coleccion vacia.

 ```python
 # usamos un buclke for para recorrer todos los eventos de la coleccion obtenidana al llamar a la funcion get.
 for event int pygame.event.get():
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_ESCAPE:
      PARAR_JUEGO = True
```
#### funcion pygame.event.wait

esta funcion espera que ocurra un evento y en cuanto sucede esta disponible

```python
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
```
#### funcion pygame.event.poll
- devuelve solo uno de los eventos que estan en la cola de espera 
      
