import numpy as np

class TanqueVaciado:
    def __init__(self, radio_tanque, radio_orificio, altura_inicial, gravedad=9.81):
        """
        Inicializa los parámetros físicos del tanque para el modelo matemático.
        """
        self.R = radio_tanque           # Radio del tanque en metros
        self.r = radio_orificio         # Radio del orificio de salida en metros
        self.h0 = altura_inicial        # Altura inicial del fluido en metros
        self.g = gravedad               # Gravedad (m/s^2)
        
        # Calcular las áreas (A = pi * radio^2)
        self.A_tanque = np.pi * (self.R ** 2)
        self.A_orificio = np.pi * (self.r ** 2)

    def ecuacion_diferencial(self, t, h):
        """
        Representa la EDO de la Ley de Torricelli: dh/dt = -(a/A) * sqrt(2*g*h)
        """
        # Si el tanque ya está vacío (altura <= 0), la variación es 0
        if h <= 0:
            return 0
            
        # Calcular dh/dt
        dh_dt = -(self.A_orificio / self.A_tanque) * np.sqrt(2 * self.g * h)
        return dh_dt

    def calcular_tiempo_vaciado_teorico(self):
        """
        Calcula el tiempo exacto que tardaría en vaciarse resolviendo la EDO analíticamente.
        """
        tiempo = (self.A_tanque / self.A_orificio) * np.sqrt((2 * self.h0) / self.g)
        return tiempo
    