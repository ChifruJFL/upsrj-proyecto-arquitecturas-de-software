# ============================================================
# Universidad Politécnica de Santa Rosa Jáuregui
# Alumno: Luis Ángel Silva Ramírez
# Materia: Arquitecturas de Software
# Profesor: Jesús Salvador López Ortega
# Grupo: ISW28
# Archivo: vars.py
# Descripción: Este archivo define variables de configuración y estilos 
#              utilizados en las pruebas del proyecto. Incluye la ruta 
#              base del directorio fuente (BASE_DIR) y una serie de 
#              constantes que representan códigos de color ANSI para 
#              mejorar la legibilidad de la salida en consola. Estas 
#              variables se emplean para mostrar mensajes formateados 
#              y separar secciones durante la ejecución de los tests.
# ============================================================

import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Colores ANSI
GREEN = "\033[92m"
RED = "\033[91m"
LIGHT_RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"
BOLD = "\033[1m"
SEPARATOR = f"{BOLD}{'='*50}{RESET}"
