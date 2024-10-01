# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# Versión modificada por Laura Oliveros & Laura Triana.

# Es necesaria la instalación e importación de vpython, un módulo de gráficos 3D
from vpython import *

"""Se define el número máximo de niveles para el modelo atómico de Bohr"""
n_max = 10 
"""A continuación se definen diferentes parámetros que permitirán obtener el modelo del gráfico en una ventada
según las características especificadas"""
scene.title = "Bohr model of the atom"
scene.height = 500 "Altura de la ventana"
scene.width = 500 "Anchura de la ventana"
scene.range = 2e-9 "Escala de visualización"
scene.zoom = scene.spin = False "Desactivar zoom"
background = color.white "Color de fondo de la escena"
flash = color.black 
scene.background = background "Color de fondo"

# Se define la función que establece las órbitas, sus argumentos son: radio, grosor y color.
def circle(radius, thickness, tint):
    """
    Establece las órbitas circulare que puede tener el electrón en el átomo de hidrógeno con una serie
    de puntos

    Args:
    radius(float): Radio de la órbita circular.
    thickness(float): Grosor de la línea que representa la órbita.
    tint(vector): Color de la órbita, definido como un vector RGB de VPython.

    Returns:
    rtype: Objeto de curva que representa la órbita circular.
    """
    
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

"""
Se definen las variables clásicas necesarias para llevar a cabo la simulación como: la constante
de Planck, constante de Coulomb, carga y masa del electrón.
"""
hbar = 1.05e-34
oofpez = 9e9
qe = 1.6e-19
m = 9e-31

"""
Se crean las órbitas relacionadas a sus radios (dependientes de cada número cuántico)
"""
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
    """
    Detecta un clic en la ventana de la simulación y cambia la variable global `clicked` a True.
    """
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
