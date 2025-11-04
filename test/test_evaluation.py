# ============================================================
# Universidad Politécnica de Santa Rosa Jáuregui
# Alumno: Luis Ángel Silva Ramírez
# Materia: Arquitecturas de Software
# Profesor: Jesús Salvador López Ortega
# Grupo: ISW28
# Archivo: test_evaluation.py
# Descripción: Este archivo contiene pruebas unitarias diseñadas para 
#              validar el funcionamiento de los procesos criptográficos 
#              implementados en el módulo principal del proyecto. A través 
#              de la clase TestCryptography, se verifica que las claves y 
#              los tokens generados sean del tipo correcto, que no estén 
#              vacíos y que el mensaje desencriptado coincida con el texto 
#              original. Utiliza la librería unittest para ejecutar las 
#              pruebas y confirmar la integridad del sistema de cifrado.
# ============================================================

import sys
import unittest
from common.vars import *

sys.path.insert(0, BASE_DIR)

import main

class TestCryptography(unittest.TestCase):

    def test_cryptography(self):
        # Recuperar objetos desde main
        key = main.key
        fernet = main.f
        token = main.token

        # Validaciones didácticas
        self.assertIsInstance(key, bytes, "La clave debe ser de tipo bytes")
        self.assertIsInstance(token, bytes, "El token debe ser de tipo bytes")
        self.assertTrue(len(token) > 0, "El token no debe estar vacío")

        # Desencriptar y validar
        decrypted = fernet.decrypt(token)
        expected = b"A really secret message. Not for prying eyes."
        self.assertEqual(decrypted, expected, "El mensaje desencriptado debe coincidir con el original")
        
        print("Everything fine with cryptography.")
        
if __name__ == '__main__':
    unittest.main()