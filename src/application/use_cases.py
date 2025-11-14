# ============================================================
# Universidad Politécnica de Santa Rosa Jáuregui
# Alumno: Luis Angel Silva Ramirez
# Materia: Arquitecturas de Software
# Profesor: Jesús Salvador López Ortega
# Grupo: ISW28
# Archivo: use_cases.py
# Descripción:
#   Este archivo implementa los casos de uso principales:
#   - Carga de archivos binarios (UploadBinaryUseCase)
#   - Listado de archivos (ListFilesUseCase)
#   - Firma digital de archivos binarios (SignBinaryUseCase)
#   Cada caso de uso orquesta las operaciones de infraestructura
#   necesarias para manipular los archivos y sus metadatos.
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import List, Dict, Any, Optional, BinaryIO

from src.domain.models import BinaryFile
from src.domain.services import SigningService
from src.infrastructure.file_repository import FileRepository
from src.infrastructure.json_repository import JsonRepository


# ============================================================
# Caso de uso: Carga de archivo binario
# ============================================================
class UploadBinaryUseCase:
    
    def __init__(self, file_repo: FileRepository, json_repo: JsonRepository):
        self.file_repo = file_repo
        self.json_repo = json_repo
    
    def execute(self, file: BinaryIO, environment: str) -> BinaryFile:
        """Guarda un archivo binario y registra sus metadatos."""
        binary_id = str(uuid4())
        filename = self.file_repo.save(file, binary_id)
        status = 'pending' if environment == 'prod' else 'signed'

        binary = BinaryFile(
            file_id=binary_id,
            filename=filename,
            environment=environment,
            status=status,
            uploaded_at=datetime.now()
        )

        # Guardar registro en la base JSON
        self.json_repo.add_record(binary)
        return binary


# ============================================================
# Caso de uso: Listado de archivos
# ============================================================
class ListFilesUseCase:
    
    def __init__(self, db_repo: JsonRepository):
        self.db_repo = db_repo

    def execute(self) -> List[Dict[str, Any]]:
        """Devuelve la lista de archivos registrados."""
        try:
            records = self.db_repo.list_records()
            return records
        except Exception as e:
            print(f"[ListFilesUseCase] Error retrieving records: {e}")
            return []


# ============================================================
# Caso de uso: Firma de archivo binario
# ============================================================
class SignBinaryUseCase:
    
    def __init__(self, file_repo: FileRepository, json_repo: JsonRepository, signing_service: SigningService):
        self.file_repo = file_repo
        self.json_repo = json_repo
        self.signing_service = signing_service

    def execute(self, file_id: str) -> Optional[BinaryFile]:
        """Firma un archivo existente y actualiza su registro."""
        record = self.json_repo.get_record(file_id)
        if record is None:
            print(f"[SignBinaryUseCase] Record not found for file_id: {file_id}")
            return None

        try:
            # Convertir el registro del repositorio JSON en objeto de dominio
            binary = BinaryFile.from_dict(record)

            # Cargar archivo original y generar la firma digital
            binary_data = self.file_repo.load(binary.filename)
            signature = self.signing_service.sign_binary(binary_data, "private_key.pem")

            # Guardar el archivo firmado
            signed_path = self.file_repo.move_to_signed(binary.filename, binary_data)

            # Actualizar el modelo con nueva información
            binary.status = 'signed'
            binary.signed_path = signed_path
            binary.signature = signature

            # Actualizar registro en la base JSON
            self.json_repo.update_record(file_id, {
                "status": binary.status,
                "signed_path": binary.signed_path,
                "signature": binary.signature
            })

            print(f"[SignBinaryUseCase] File {file_id} signed successfully.")
            return binary

        except Exception as e:
            print(f"[SignBinaryUseCase] Error signing file_id {file_id}: {e}")
            return None
