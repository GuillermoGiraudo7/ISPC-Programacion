import pytest
from Pulidora import Pulidora  

def test_encender():
    pulidora = Pulidora()
    pulidora.encender()
    assert pulidora.estado == 'encendida'

def test_apagar():
    pulidora = Pulidora()
    pulidora.encender()
    pulidora.apagar()
    assert pulidora.estado == 'apagada'

def test_ajustar_velocidad():
    pulidora = Pulidora()
    pulidora.encender()
    pulidora.ajustar_velocidad(50)
    assert pulidora.velocidad == 50

def test_ajustar_velocidad_fuera_de_rango():
    pulidora = Pulidora()
    pulidora.encender()
    with pytest.raises(ValueError, match="La velocidad debe estar entre 0 y 100."):
        pulidora.ajustar_velocidad(150)

def test_seleccionar_modo():
    pulidora = Pulidora()
    pulidora.encender()
    pulidora.seleccionar_modo('avanzado')
    assert pulidora.modo == 'avanzado'

def test_seleccionar_modo_invalido():
    pulidora = Pulidora()
    pulidora.encender()
    with pytest.raises(ValueError, match="Modo no válido. Modos disponibles: básico, avanzado, ultra"):
        pulidora.seleccionar_modo('invalido')

def test_pulir_lente():
    pulidora = Pulidora()
    pulidora.encender()
    pulidora.ajustar_velocidad(10)
    pulidora.nivel_lente = 5
    pulidora.pulir_lente(2)
    assert pulidora.nivel_lente == 4

def test_pulir_lente_ya_limpio():
    pulidora = Pulidora()
    pulidora.encender()
    pulidora.ajustar_velocidad(10)
    pulidora.nivel_lente = 0
    with pytest.raises(ValueError, match="El lente ya está limpio."):
        pulidora.pulir_lente(1)

def test_reportar_estado():
    pulidora = Pulidora()
    pulidora.encender()
    pulidora.ajustar_velocidad(30)
    pulidora.seleccionar_modo('ultra')
    pulidora.nivel_lente = 10
    estado = pulidora.reportar_estado()
    assert estado == {'estado': 'encendida', 'velocidad': 30, 'modo': 'ultra', 'nivel_lente': 10}

def test_str():
    pulidora = Pulidora()
    pulidora.encender()
    pulidora.ajustar_velocidad(25)
    pulidora.seleccionar_modo('básico')
    pulidora.nivel_lente = 7.50
    assert str(pulidora) == "Pulidora (Estado: encendida, Velocidad: 25, Modo: básico, Nivel de Lente: 7.50)"