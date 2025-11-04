# ============================================================
# Universidad Politécnica de Santa Rosa Jáuregui
# Alumno: Luis Ángel Silva Ramírez
# Materia: Arquitecturas de Software
# Profesor: Jesús Salvador López Ortega
# Grupo: ISW28
# Archivo: models.py
# Descripción: Este archivo define el modelo de dominio BinaryFile, 
#              el cual representa la entidad de un archivo binario 
#              dentro del sistema. Utiliza la clase dataclass para 
#              simplificar la creación de la estructura de datos con 
#              sus atributos principales: identificador, nombre del 
#              archivo, entorno, estado, fecha de carga, ruta firmada 
#              y firma digital. Este modelo se emplea para almacenar 
#              y gestionar la información de los archivos subidos.
# ============================================================

from dataclasses import dataclass
from datetime import datetime

@dataclass
class BinaryFile:
    id: str
    filename: str
    environment: str
    status: str
    uploaded_at: datetime
    signed_path: str = None
    signature: str = None
