import os
import sys
from django.shortcuts import render
from django.conf import settings
from .forms import TanqueForm

# Añadir el directorio raíz al path para poder importar el módulo 'simulacion'
sys.path.append(str(settings.BASE_DIR.parent))

from simulacion.modelo_matematico import TanqueVaciado
from simulacion.simulador import ejecutar_simulacion
from simulacion.graficas import graficar_altura_vs_tiempo, graficar_volumen_vs_tiempo
from simulacion.animacion_gif import generar_gif_vaciado

def index(request):
    form = TanqueForm()
    resultados = None

    if request.method == 'POST':
        form = TanqueForm(request.POST)
        if form.is_valid():
            # Extraer datos del formulario
            r_tanque = form.cleaned_data['radio_tanque']
            r_orificio = form.cleaned_data['radio_orificio']
            h_inicial = form.cleaned_data['altura_inicial']

            # 1. Crear instancia del modelo
            tanque = TanqueVaciado(r_tanque, r_orificio, h_inicial)

            # 2. Ejecutar simulación numérica
            df = ejecutar_simulacion(tanque)

            # 3. Definir rutas de salida (dentro de la carpeta 'resultados' que Django sirve)
            # Nota: settings.MEDIA_ROOT apunta a 'resultados/'
            ruta_grafica_h = os.path.join(settings.MEDIA_ROOT, 'graficas', 'altura_vs_tiempo.png')
            ruta_grafica_v = os.path.join(settings.MEDIA_ROOT, 'graficas', 'volumen_vs_tiempo.png')
            ruta_gif = os.path.join(settings.MEDIA_ROOT, 'animaciones', 'vaciado_tanque.gif')

            # 4. Generar visualizaciones
            graficar_altura_vs_tiempo(df, ruta_salida=ruta_grafica_h)
            graficar_volumen_vs_tiempo(df, ruta_salida=ruta_grafica_v)
            generar_gif_vaciado(df, ruta_salida=ruta_gif, radio_tanque=r_tanque)

            # 5. Preparar datos para el template
            resultados = {
                'grafica_altura': os.path.join(settings.MEDIA_URL, 'graficas/altura_vs_tiempo.png').replace('\\', '/'),
                'grafica_volumen': os.path.join(settings.MEDIA_URL, 'graficas/volumen_vs_tiempo.png').replace('\\', '/'),
                'gif_vaciado': os.path.join(settings.MEDIA_URL, 'animaciones/vaciado_tanque.gif').replace('\\', '/'),
                'tiempo_total': round(df['Tiempo_s'].iloc[-1], 2),
                'altura_inicial': h_inicial
            }

    return render(request, 'index.html', {
        'form': form,
        'resultados': resultados
    })
