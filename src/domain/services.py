# ============================================================
# Universidad Politécnica de Santa Rosa Jáuregui
# Alumno: Luis Ángel Silva Ramírez
# Materia: Arquitecturas de Software
# Profesor: Jesús Salvador López Ortega
# Grupo: ISW28
# Archivo: services.py
# Descripción: Este archivo implementa el servicio de firma digital 
#              de archivos binarios mediante la clase SigningService. 
#              Utiliza criptografía asimétrica con el algoritmo RSA y 
#              el esquema de relleno PKCS1v15 junto con el hash SHA-256 
#              para garantizar la integridad y autenticidad de los datos. 
#              La clase recibe un cargador de claves (key_loader) que 
#              obtiene la clave privada necesaria para generar la firma 
#              del archivo binario.
# ============================================================

import os
import hashlib
from typing import Tuple
from src.domain.models import BinaryFile
from src.common.vars import DATA_DIR, SIGNED_DIR

class SigningService:
    
    def __init__(self, output_dir: str = SIGNED_DIR):
        self.output_dir = output_dir
    
    def sign_file(self, binary: BinaryFile) -> Tuple[str, str]:
        try:
          
            filename_only = os.path.basename(binary.filename)
            source_path = os.path.join(DATA_DIR, filename_only)
            
            # Definimos la ruta de salida
            signed_filename = f"signed_{filename_only}"
            signed_path = os.path.join(self.output_dir, signed_filename)
        
            # Compute SHA-256 signature
            sha256_hash = hashlib.sha256()
            
            # Leemos el archivo original para calcular el hash
            with open(source_path, 'rb') as file:
                for block in iter(lambda: file.read(4096), b""):
                    sha256_hash.update(block)
            
            signature = sha256_hash.hexdigest()
            
            # Creamos la copia firmada
            with open(source_path, 'rb') as src, open(signed_path, 'wb') as dst:
                dst.write(src.read())
                dst.write(b"\n\n# SIGNATURE: " + signature.encode("utf-8"))
            
            print(f"[SigningService] File '{filename_only}' signed successfully.")            
            return signature, signed_path
        
        except Exception as e:
            print(f"[SigningService] Error while signing '{binary.filename}': {e}")
            raise