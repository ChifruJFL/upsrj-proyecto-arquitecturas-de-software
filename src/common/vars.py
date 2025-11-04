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
#              proyecto.
# ============================================================

import os
from dataclasses import dataclass
from typing import Tuple

ROOT_DIR        = "upsrj-proyecto-arquitecturas-de-software"
SRC_DIR         = os.path.join(ROOT_DIR, "src")
TEMPLATES_DIR   = os.path.join(SRC_DIR, "templates")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@dataclass
class Hosts:
    """
    Configuration for host and port settings.

    Attributes:
        main (Tuple[str, int]): IP address and port for the main host.
    """
    main: Tuple[str, int] = ('0.0.0.0', 5000)
