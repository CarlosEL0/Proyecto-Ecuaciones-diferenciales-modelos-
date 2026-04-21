# 🚰 Simulador de Vaciado de Tanque (Ley de Torricelli)

Este proyecto es una herramienta interactiva diseñada para modelar y simular el proceso de vaciado de un tanque cilíndrico utilizando **Ecuaciones Diferenciales Ordinarias (EDO)**. Combina el rigor matemático con una interfaz web moderna y visualizaciones dinámicas.

## 🚀 Características

- **Modelo Matemático**: Implementación de la Ley de Torricelli para calcular el vaciado.
- **Simulación Numérica**: Uso de Python para resolver las ecuaciones y generar datos precisos.
- **Interfaz Web**: Panel de control profesional desarrollado en **Django** con soporte para modo oscuro.
- **Visualizaciones**:
    - 🎬 **Animación GIF**: Representación dinámica del nivel del fluido.
    - 📉 **Gráficas de Análisis**: Altura vs Tiempo y Volumen vs Tiempo (Matplotlib).
- **Diseño Moderno**: Interfaz responsiva con Bootstrap 5, fuentes Inter y modo oscuro persistente.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.x
- **Framework Web**: Django
- **Bibliotecas Científicas**: 
    - `numpy`: Cálculos numéricos.
    - `pandas`: Manejo de datos de la simulación.
    - `matplotlib`: Generación de gráficas y animaciones.
    - `scipy`: Resolución de ecuaciones diferenciales.
- **Frontend**: Bootstrap 5, Bootstrap Icons, JavaScript (ES6+).

## 📋 Requisitos Previos

Asegúrate de tener instalado Python y `pip` en tu sistema.

## ⚙️ Instalación y Uso

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/CarlosEL0/Proyecto-Ecuaciones-diferenciales-modelos-.git
   cd Proyecto-Ecuaciones-diferenciales-modelos-
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el servidor de Django**:
   Navega a la carpeta del proyecto web y arranca el servidor:
   ```bash
   cd web_django
   python manage.py runserver
   ```

4. **Acceder a la aplicación**:
   Abre tu navegador y ve a: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 🧪 Cómo realizar una simulación

1. Ingresa el **Radio del Tanque** (en metros).
2. Ingresa el **Radio del Orificio** de salida (en metros).
3. Ingresa la **Altura Inicial** del agua (en metros).
4. Haz clic en **"Calcular Simulación"**.
5. Espera unos segundos mientras el motor genera el GIF y las gráficas.

---
**Proyecto desarrollado para la materia de Cálculo - 5to Cuatrimestre.**
