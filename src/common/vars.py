# ============================================================
# Universidad Politécnica de Santa Rosa Jáuregui
# Alumno: Luis Ángel Silva Ramírez
# Materia: Arquitecturas de Software
# Profesor: Jesús Salvador López Ortega
# Grupo: ISW28
# Archivo: vars.py
# Descripción: Este archivo define las rutas principales del proyecto 
#              y la configuración del host del servidor. Incluye la 
#              clase Hosts, que utiliza dataclasses para almacenar la 
#              dirección IP y el puerto donde se ejecutará la aplicación. 
#              Además, se establecen constantes con las rutas base 
#              (ROOT_DIR, SRC_DIR, TEMPLATES_DIR y BASE_DIR) que sirven 
#              para ubicar los archivos fuente y las plantillas del 
#              proyecto. También se agregan las rutas de datos 
#              (DATA_DIR y SIGNED_DIR) utilizadas por los repositorios.
# ============================================================

import os

# Calculamos la ruta base dinámicamente para que funcione en cualquier PC
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Definición de Directorios según el profe
ROOT_DIR = BASE_DIR
SRC_DIR = os.path.join(ROOT_DIR, "src")
DATA_DIR = os.path.join(ROOT_DIR, "data", "binaries") # Aquí se guardan los que subes
SIGNED_DIR = os.path.join(ROOT_DIR, "data", "signed") # Aquí se guardan los firmados
TEMPLATES_DIR = os.path.join(SRC_DIR, "app", "templates")

# Configuración del servidor
HOME_HOST = 8080

# Aseguramos que existan las carpetas
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(SIGNED_DIR, exist_ok=True)