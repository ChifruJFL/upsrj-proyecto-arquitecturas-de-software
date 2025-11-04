# ============================================================
# Universidad Politécnica de Santa Rosa Jáuregui
# Alumno: Luis Angel Silva Ramirez
# Materia: Arquitecturas de Software
# Profesor: Jesús Salvador López Ortega
# Grupo: ISW28
# Archivo: uses cases.py
# Descripción:  Este archivo implementa el caso de uso para la carga 
#              de archivos binarios. La clase UploadBinaryUseCase 
#              se encarga de gestionar el proceso de almacenamiento 
#              del archivo y el registro de sus metadatos en la base 
#              de datos, generando un identificador único y 
#              asignando su estado según el entorno (producción o 
#              desarrollo). Devuelve una instancia del modelo 
#              BinaryFile con la información del archivo cargado.
# ============================================================

from datetime import datetime
from uuid import uuid4
from src.domain.models import BinaryFile

class UploadBinaryUseCase:
    def __init__(self, file_repo, db_repo):
        self.file_repo = file_repo
        self.db_repo = db_repo

    def execute(self, file, environment: str) -> BinaryFile:
        binary_id = str(uuid4())
        filename = self.file_repo.save(file, binary_id)
        binary = BinaryFile(
            id = binary_id,
            filename = filename,
            environment = environment,
            status = 'pending' if environment == 'prod' else 'signed',
            uploaded_at = datetime.now()
        )
        self.db_repo.add(binary)
        return binary
