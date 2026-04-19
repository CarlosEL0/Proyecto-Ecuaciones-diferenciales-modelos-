import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import os

def generar_gif_vaciado(df, ruta_salida="resultados/animaciones/vaciado_tanque.gif", radio_tanque=1.0):
    """Genera una animación GIF del vaciado del tanque a partir de los datos."""
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    
    # Reducir la cantidad de "frames" (cuadros) para que el GIF no sea muy pesado.
    # Si tenemos 400 registros, tomamos aprox. 100 cuadros para el GIF.
    paso = max(1, len(df) // 100)
    df_frames = df.iloc[::paso].copy()
    
    altura_max = df['Altura_m'].max()
    
    # Configurar el "lienzo" de la animación
    fig, ax = plt.subplots(figsize=(6, 8))
    ax.set_xlim(-radio_tanque * 1.5, radio_tanque * 1.5)
    ax.set_ylim(0, altura_max * 1.15)
    ax.set_aspect('equal')
    ax.axis('off') # Ocultar los ejes cartesianos para que parezca un dibujo físico
    
    plt.title('Simulación Dinámica de Vaciado', fontsize=14, fontweight='bold', pad=20)
    
    # Dibujar las paredes y el fondo del tanque (líneas estáticas)
    ax.plot([-radio_tanque, -radio_tanque], [0, altura_max], color='black', lw=4) # Pared izquierda
    ax.plot([radio_tanque, radio_tanque], [0, altura_max], color='black', lw=4)   # Pared derecha
    ax.plot([-radio_tanque, radio_tanque], [0, 0], color='black', lw=6)           # Fondo
    
    # Dibujar el "agua" como un rectángulo azul. Inicia completamente lleno.
    agua = patches.Rectangle((-radio_tanque, 0), radio_tanque * 2, altura_max, color='#3498db', alpha=0.8)
    ax.add_patch(agua)
    
    # Etiqueta de texto dinámico para mostrar el tiempo y altura
    texto_info = ax.text(0, altura_max * 1.05, '', ha='center', fontsize=12, fontweight='bold', color='#2c3e50')
    
    # Esta es la función que matplotlib llamará para dibujar cada cuadro del GIF
    def actualizar(frame_idx):
        fila = df_frames.iloc[frame_idx]
        altura_actual = fila['Altura_m']
        tiempo_actual = fila['Tiempo_s']
        
        # Actualizamos la altura del rectángulo de agua
        agua.set_height(altura_actual)
        # Actualizamos el texto
        texto_info.set_text(f'Tiempo: {tiempo_actual:.1f} s | Nivel: {altura_actual:.2f} m')
        
        return agua, texto_info

    # print(f"🎬 Generando GIF con {len(df_frames)} cuadros. Esto puede tardar unos segundos...")
    
    # Crear la animación
    anim = animation.FuncAnimation(
        fig, 
        actualizar, 
        frames=len(df_frames), 
        interval=50, # 50 milisegundos de pausa entre cuadros
        blit=True
    )
    
    anim.save(ruta_salida, writer='pillow', fps=20)
    plt.close()
