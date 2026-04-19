import pandas as pd
import matplotlib.pyplot as plt
import os

def graficar_altura_vs_tiempo(df, ruta_salida="resultados/graficas/altura_vs_tiempo.png"):
    """Genera y guarda la gráfica de Altura vs Tiempo."""
    # Asegurar que el directorio exista
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    
    # Crear la figura
    plt.figure(figsize=(10, 6))
    
    # Trazar los datos
    plt.plot(df['Tiempo_s'], df['Altura_m'], color='#1f77b4', linewidth=2.5, label='Nivel del agua')
    
    # Personalizar la gráfica
    plt.title('Dinámica de Vaciado: Altura vs Tiempo', fontsize=14, fontweight='bold')
    plt.xlabel('Tiempo (segundos)', fontsize=12)
    plt.ylabel('Altura del fluido (metros)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Rellenar el área bajo la curva para darle un toque visual a "agua"
    plt.fill_between(df['Tiempo_s'], df['Altura_m'], color='#1f77b4', alpha=0.2)
    
    plt.legend()
    plt.tight_layout()
    
    # Guardar y cerrar
    plt.savefig(ruta_salida, dpi=300) # Alta resolución
    plt.close()
    # print(f"📊 Gráfica de Altura guardada en: {ruta_salida}")

def graficar_volumen_vs_tiempo(df, ruta_salida="resultados/graficas/volumen_vs_tiempo.png"):
    """Genera y guarda la gráfica de Volumen vs Tiempo (valor extra)."""
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['Tiempo_s'], df['Volumen_m3'], color='#2ca02c', linewidth=2.5, label='Volumen del tanque')
    
    plt.title('Dinámica de Vaciado: Volumen vs Tiempo', fontsize=14, fontweight='bold')
    plt.xlabel('Tiempo (segundos)', fontsize=12)
    plt.ylabel('Volumen (Metros cúbicos - m³)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.fill_between(df['Tiempo_s'], df['Volumen_m3'], color='#2ca02c', alpha=0.2)
    
    plt.legend()
    plt.tight_layout()
    
    plt.savefig(ruta_salida, dpi=300)
    plt.close()
    # print(f"📊 Gráfica de Volumen guardada en: {ruta_salida}")
