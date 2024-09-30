import pytest
from energia_niveles import energia_nivel, niveles_energia

def test_energia_nivel():
    """
    Prueba la función energia_nivel para varios niveles cuánticos del átomo de hidrógeno.
    
    Verifica que los valores calculados sean correctos dentro de un margen de error de 0.01 eV.
    """
    # Valores esperados para algunos niveles del átomo de hidrógeno
    assert energia_nivel(1) == pytest.approx(-13.6, 0.01)
    assert energia_nivel(2) == pytest.approx(-3.4, 0.01)
    assert energia_nivel(3) == pytest.approx(-1.51, 0.01)
    assert energia_nivel(4) == pytest.approx(-0.85, 0.01)

def test_niveles_energia():
    """
    Prueba la función niveles_energia para una lista de niveles cuánticos.
    
    Verifica que la lista de energías generada tenga la longitud correcta y que los valores de energía 
    coincidan con los esperados dentro de un margen de error de 0.01 eV.
    """
    # Valores esperados para los niveles del 1 al 4
    esperado = [-13.6, -3.4, -1.51, -0.85]
    calculado = niveles_energia(4)
    
    assert len(calculado) == 4
    for nivel, valor in enumerate(calculado):
        assert valor == pytest.approx(esperado[nivel], 0.01)
