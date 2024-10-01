# Testeando el archivo bohrsimulation.
# Importación de librerías 
import pytest
from bohrsimulation import *  

def test_circle_creation():
    # Datos de prueba
    radius = 1.0
    thickness = 0.1
    tint = vector(1, 0, 0)  # Color rojo
    
    # Llamada a la función
    result = circle(radius, thickness, tint)
    
    # Verifica que el resultado es un objeto de tipo curve
    assert isinstance(result, curve), "El resultado no es un objeto curve"
    
    # Verificar que el grosor de la línea
    assert result.radius == thickness, f"El grosor de la curva debería ser {thickness}"
    
    # Verificar que el color de la curva 
    assert result.color == tint, f"El color debería ser {tint}"
    
    # Verificar la cantidad de puntos generados (50)
    assert len(result.points) == 50
