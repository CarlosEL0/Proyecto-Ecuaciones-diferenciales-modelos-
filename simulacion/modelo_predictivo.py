import os
from simulacion.modelo_matematico import TanqueVaciado
from simulacion.simulador import ejecutar_simulacion, guardar_datos
from simulacion.graficas import graficar_altura_vs_tiempo, graficar_volumen_vs_tiempo
from simulacion.animacion_gif import generar_gif_vaciado

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def ejecutar_simulador_interactivo():
    # Variable de control para el ciclo principal (Buena práctica)
    continuar_simulando = True
    
    while continuar_simulando:
        limpiar_pantalla()
        print("="*50)
        print(" 🌊 SIMULADOR PREDICTIVO: VACIADO DE TANQUE 🌊")
        print("="*50)
        print("\nPor favor, ingresa los datos físicos de tu sistema:")
        
        # Variable de control para la validación de entrada de datos
        datos_validos = False
        
        while not datos_validos:
            try:
                radio_t = float(input(" - Radio del tanque (en metros): "))
                radio_o = float(input(" - Radio del orificio de salida (en metros): "))
                altura = float(input(" - Altura inicial del agua (en metros): "))
                
                if radio_t <= 0 or radio_o <= 0 or altura <= 0:
                    print("❌ Error: Todos los valores deben ser mayores a cero.\n")
                elif radio_o >= radio_t:
                    print("❌ Error: El orificio no puede ser más grande que el tanque.\n")
                else:
                    datos_validos = True 
                
            except ValueError:
                print("❌ Error: Debes ingresar números válidos.\n")
                
        # --- EJECUCIÓN DEL FLUJO ---
        print("\n⚙️  1. Inicializando modelo matemático...")
        mi_tanque = TanqueVaciado(radio_t, radio_o, altura)
        
        print("⚙️  2. Resolviendo ecuaciones diferenciales...")
        df_resultados = ejecutar_simulacion(mi_tanque)
        
        tiempo_total_min = df_resultados['Tiempo_s'].iloc[-1] / 60
        
        print(f"\n✅ ¡Simulación completada! Tiempo estimado: {tiempo_total_min:.2f} minutos")
        
        print("\n⚙️  3. Exportando resultados y visualizaciones...")
        guardar_datos(df_resultados, "resultados/datos/simulacion_usuario.csv")
        graficar_altura_vs_tiempo(df_resultados, "resultados/graficas/usuario_altura.png")
        graficar_volumen_vs_tiempo(df_resultados, "resultados/graficas/usuario_volumen.png")
        
        print("⚙️  4. Renderizando animación GIF...")
        generar_gif_vaciado(df_resultados, "resultados/animaciones/simulacion_usuario.gif", radio_tanque=radio_t)
        
        # --- CONTROL DEL CICLO PRINCIPAL (CON VALIDACIÓN ESTRICTA) ---
        confirmacion_valida = False
        while not confirmacion_valida:
            respuesta = input("\n¿Deseas realizar otra simulación? (s/n): ").strip().lower()
            
            if respuesta == 's':
                confirmacion_valida = True
                # El bucle principal 'while continuar_simulando' volverá a iniciar
            elif respuesta == 'n':
                confirmacion_valida = True
                continuar_simulando = False # Apagamos la bandera para salir definitivamente
                print("\n🌊 ¡Gracias por usar el Simulador! Hasta la próxima. 🚀\n")
            else:
                # Si el usuario presiona un número o cualquier otra tecla
                print("❌ Entrada no válida. Por favor, escribe 's' para continuar o 'n' para salir.")

if __name__ == "__main__":
    ejecutar_simulador_interactivo()