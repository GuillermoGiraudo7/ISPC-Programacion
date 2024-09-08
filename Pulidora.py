class Pulidora:                     #Pulidora de Lentes Ópticos
    def __init__(self):
        self.estado = 'apagada'
        self.velocidad = 0
        self.modo = 'básico'
        self.nivel_lente = 0

    def encender(self):             #Encendido
        if self.estado == 'apagada':
            self.estado = 'encendida'
        else:
            raise Exception("La pulidora ya está encendida.")

    def apagar(self):               #Apagado
        if self.estado == 'encendida':
            self.estado = 'apagada'
        else:
            raise Exception("La pulidora ya está apagada.")

    def ajustar_velocidad(self, velocidad):     #Velocidad
        if self.estado == 'encendida':
            if 0 <= velocidad <= 100:           # Rango de velocidad de ejemplo
                self.velocidad = velocidad
                return f"Velocidad ajustada a {velocidad}."
            else:
                raise ValueError("La velocidad debe estar entre 0 y 100.")
        else:
            raise Exception("La pulidora debe estar encendida para ajustar la velocidad.")

    def seleccionar_modo(self, modo):
        if self.estado == 'encendida':
            modos_validos = ['básico', 'avanzado', 'ultra']
            if modo in modos_validos:
                self.modo = modo
                return f"Modo seleccionado: {modo}."
            else:
                raise ValueError(f"Modo no válido. Modos disponibles: {', '.join(modos_validos)}")
        else:
            raise Exception("La pulidora debe estar encendida para seleccionar el modo.")

    def pulir_lente(self, cantidad):
        if self.estado == 'encendida':
            if self.nivel_lente > 0:
                pulido = min(cantidad, self.velocidad * 0.1)
                self.nivel_lente -= pulido
                if self.nivel_lente < 0:
                    self.nivel_lente = 0
                return f"Se ha pulido el lente en {pulido} unidades."
            else:
                raise ValueError("El lente ya está limpio.")
        else:
            raise Exception("La pulidora debe estar encendida para pulir el lente.")

    def reportar_estado(self):
        return {
            'estado': self.estado,
            'velocidad': self.velocidad,
            'modo': self.modo,
            'nivel_lente': self.nivel_lente
        }

    def __str__(self):
        return (f"Pulidora (Estado: {self.estado}, Velocidad: {self.velocidad}, "
                f"Modo: {self.modo}, Nivel de Lente: {self.nivel_lente:.2f})")