# energia_niveles.py

# Constante de energía en eV
E_0 = -13.6  # Energía del nivel n=1 en eV

# Función para calcular la energía de un nivel n
def energia_nivel(n):
    """
    Calcula la energía de un nivel cuántico n en el átomo de hidrógeno.
    
    Args:
    n (int): El número cuántico principal.
    
    Returns:
    float: La energía del nivel n en electronvoltios (eV).
    """
    return E_0 / n**2

# Función para calcular los niveles de energía hasta un nivel máximo
def niveles_energia(n_max):
    """
    Calcula la energía de los niveles del 1 al n_max en el átomo de hidrógeno.
    
    Args:
    n_max (int): El número cuántico máximo para el que se calcularán los niveles de energía.
    
    Returns:
    list: Lista con las energías de los niveles.
    """
    return [energia_nivel(n) for n in range(1, n_max + 1)]
