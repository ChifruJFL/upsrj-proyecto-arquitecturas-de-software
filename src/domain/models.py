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

from datetime import datetime

class BinaryFile(object):
    """
    Domain entity representing a binary file record.
    """

    def __init__(self, file_id, filename, environment, status,
                 uploaded_at=None, signed_path=None, signature=None):
        self.id = file_id
        self.filename = filename
        self.environment = environment          # 'dev' or 'prod'
        self.status = status                     # 'pending', 'approved', etc.
        self.uploaded_at = uploaded_at or datetime.now().isoformat()
        self.signed_path = signed_path
        self.signature = signature

    def to_dict(self):
        """Return a dictionary representation of the BinaryFile."""
        return {
            "id":          self.id,
            "filename":    self.filename,
            "environment": self.environment,
            "status":      self.status,
            "uploaded_at": self.uploaded_at,
            "signed_path": self.signed_path,
            "signature":   self.signature
        }

    @classmethod
    def from_dict(cls, data):
        """Create a BinaryFile instance from a dictionary."""
        return cls(
            file_id     = data.get("id"),
            filename    = data.get("filename"),
            environment = data.get("environment"),
            status      = data.get("status"),
            uploaded_at = data.get("uploaded_at"),
            signed_path = data.get("signed_path"),
            signature   = data.get("signature")
        )