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

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


class SigningService:
    """
    Servicio encargado de firmar archivos binarios usando RSA y SHA-256.
    Requiere un key_loader que devuelva la clave privada desde un archivo PEM.
    """

    def __init__(self, key_loader):
        self.key_loader = key_loader

    def sign_binary(self, binary_data: bytes, private_key_path: str) -> bytes:
        """
        Firma un archivo binario con una clave privada RSA.
        Args:
            binary_data (bytes): Contenido binario del archivo.
            private_key_path (str): Ruta al archivo PEM con la clave privada.
        Returns:
            bytes: Firma digital generada.
        """
        private_key = self.key_loader(private_key_path)
        signature = private_key.sign(
            binary_data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return signature
