# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# Versión modificada por Laura Oliveros & Laura Triana.

# Es necesaria la instalación e importación de vpython, un módulo de gráficos 3D
from vpython import *

n_max = 10 # Número máximo de niveles
# Se realiza la configuración de la escena: título, tamaño de la ventana
scene.title = "Bohr model of the atom"
scene.height = 500
scene.width = 500
scene.range = 2e-9
scene.zoom = scene.spin = False
background = color.white
flash = color.black
scene.background = background

# Se define la función que establece las órbitas, sus argumentos son: radio, grosor y color.
def circle(radius, thickness, tint):

    # Ángulo entre dos puntos consecutivos siendo 50 la cantidad de puntos total
    dtheta = 2*pi/50

    # Array de ángulos de 0 a 2pi
    angles = arange(0, 2*pi + dtheta, dtheta)

    # Se crea la curva con el color tint y el grosor de la línea
    c = curve(color=tint, radius=thickness)

    # Adición de puntos para cada ángulo con las coordenadas x y y 
    for a in angles:
        c.append(radius * vector(cos(a), sin(a), 0))
    return c

# Creación del núcleo del átomo con su radio y color
nucleus = sphere(radius=1e-11, color=color.red)

# Variables físicas necesarias, constante de Planck, constante de Coulomb,
# carga elemental y masa de electrón
hbar = 1.05e-34
oofpez = 9e9
qe = 1.6e-19
m = 9e-31

# Se crean las órbitas relacionadas a sus radios (dependientes de cada número cuántico)
levels = []
for n in range(1, n_max + 1):  # Usamos n_max para determinar el número de órbitas
    r = (n**2) * (hbar**2) / (oofpez * (qe**2) * m)
    levels.append(circle(r, 1e-11, vector(0, 0.5, 0)))

# Configuración inicial del electrón en la primera órbita
N = 1  # Nivel de energía inicial
r = (N**2) * 0.53e-10
omega = N * hbar / (m * r**2)
electron = sphere(radius=4e-11, color=color.blue, pos=vector(r, 0, 0))
dt = (2 * pi / omega) / 100
t = 0.0

# Función para detectar clics en la escena
clicked = False

def getclick():
    global clicked
    clicked = True

scene.bind("click", getclick)

up = True
tflash = -1 

while True:
    rate(400)
    
    if clicked:
        clicked = False  
        scene.background = flash 
        tflash = clock() 

        if up:
            N += 1
            if N >= n_max:
                N = n_max
                up = False
        else:
            N -= 1
            if N <= 1:
                N = 1
                up = True

        r = (N**2) * 0.53e-10
        omega = N * hbar / (m * r**2)

    if tflash > 0 and clock() - tflash >= 0.5:
        scene.background = background
        tflash = -1

    electron.pos = r * vector(cos(omega * t), sin(omega * t), 0)
    t += dt
