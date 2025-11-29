# ============================================================
# Politécnica de Santa Rosa
#
# Materia: Arquitecturas de Software
# Profesor: Luis Angel Silva Ramirez
# Grupo: ISW28
# Archivo: main.py
# Descripción: Este código implementa la estructura base de una aplicación web utilizando el framework Flask en Python.
# Su función principal es crear, configurar y ejecutar una instancia del servidor Flask, siguiendo una arquitectura modular y limpia que separa claramente las responsabilidades del sistema: configuración, definición de rutas y ejecución.
# ============================================================
import sys
from pathlib import Path
from flask import Flask
from flask_mail import Mail
from src.app.routes import register_routes
from src.common.vars import HOME_HOST

# Ajuste de rutas
sys.path.append(str(Path(__file__).parent.parent.parent))

def create_app():
    app = Flask(__name__, template_folder='templates')

    # --- CONFIGURACIÓN DEL CORREO (GMAIL) ---
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    
    # CORREO REMITENTE
    app.config['MAIL_USERNAME'] = 'filipponerisilva@gmail.com'
    
    # ⚠️ Debe ser una "contraseña de aplicación" de Gmail, NO tu contraseña real
    app.config['MAIL_PASSWORD'] = 'brdxsyyrcsukeuea'

    app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

    # CORREO AL QUE SE ENVIARÁN LAS APROBACIONES
    app.config['APPROVER_EMAIL'] = 'filipponerisilva@gmail.com'

    # Inicializar Flask-Mail
    app.mail = Mail(app)

    register_routes(app)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=HOME_HOST, debug=True)