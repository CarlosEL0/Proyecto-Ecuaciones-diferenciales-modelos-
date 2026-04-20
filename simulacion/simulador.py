import numpy as np
import pandas as pd
import os
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg') # Fundamental para que Django no colapse
import matplotlib.pyplot as plt
def generar_grafica_altura(df):
    plt.figure(figsize=(8, 5))
    
    # Tomas las columnas de tu DataFrame de Pandas
    plt.plot(df['Tiempo_s'], df['Altura_m'], color='#3b82f6', linewidth=2.5)
    plt.fill_between(df['Tiempo_s'], df['Altura_m'], color='#3b82f6', alpha=0.2)
    
# Importamos el modelo matemático que creaste en el paso anterior

from simulacion.modelo_matematico import TanqueVaciado

def ejecutar_simulacion(tanque):
    """
    Resuelve la EDO del tanque usando scipy.integrate de forma numérica.
    """
    # Esta función le "avisa" al simulador que debe detenerse cuando la altura llegue a 0
    def evento_vacio(t, y):
        return y[0]
    evento_vacio.terminal = True
    evento_vacio.direction = -1

    # Calculamos un tiempo máximo con un margen de seguridad para que la simulación no se corte antes
    t_max_estimado = tanque.calcular_tiempo_vaciado_teorico() * 1.2
    
    # Resolvemos la EDO numéricamente usando el método Runge-Kutta de orden 4/5 (RK45)
    solucion = solve_ivp(
        fun=tanque.ecuacion_diferencial,
        t_span=(0, t_max_estimado),
        y0=[tanque.h0],
        method='RK45',
        events=evento_vacio,
        max_step=1.0 # Obligamos a guardar datos al menos cada 1 segundo para gráficas fluidas
    )

    # Extraemos los arreglos de resultados
    tiempos = solucion.t
    alturas = solucion.y[0]
    
    # Limpiamos los datos (evitamos minúsculos errores numéricos negativos)
    alturas = np.maximum(alturas, 0)
    
    # Agregamos el cálculo del volumen (Área * altura) para tener más datos interesantes
    volumenes = tanque.A_tanque * alturas
    
    # Convertimos todo en una tabla estructurada usando pandas
    df_resultados = pd.DataFrame({
        'Tiempo_s': tiempos,
        'Altura_m': alturas,
        'Volumen_m3': volumenes
    })
    
    return df_resultados

def guardar_datos(df, ruta="resultados/datos/simulacion_datos.csv"):
    """Guarda la tabla de resultados de la simulación en un archivo CSV."""
    # Crea la carpeta si no existe
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    df.to_csv(ruta, index=False)
    print(f"📁 Datos exportados exitosamente en: {ruta}")
