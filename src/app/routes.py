# ============================================================
# Universidad Politécnica de Santa Rosa Jáuregui
# Alumno: Luis Angel Silva Ramirez
# Materia: Arquitecturas de Software
# Profesor: Jesús Salvador López Ortega
# Grupo: ISW28
# Archivo: routes.py
# Descripción: Define las rutas principales del sistema:
# - /upload  : Recibe archivos y envía correo de aprobación
# - /files   : Lista los registros JSON
# - /sign    : Firma un archivo existente
# ============================================================

from flask import request, jsonify, render_template
from src.application.use_cases import UploadBinaryUseCase, SignBinaryUseCase, ApproveBinaryUseCase
from src.infrastructure.file_repository import FileRepository
from src.infrastructure.json_repository import JsonRepository
from src.infrastructure.email_service import EmailService
from src.domain.services import SigningService

def register_routes(app):

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/files', methods=['GET'])
    def list_files():
        return jsonify(JsonRepository().list_records()), 200

    # --- SOLO UNA RUTA /upload ---
    @app.route('/upload', methods=['POST'])
    def upload_binary():
        file = request.files['file']
        environment = request.form.get('environment', 'dev')

        target_email = app.config['APPROVER_EMAIL']

        use_case = UploadBinaryUseCase(
            FileRepository(),
            JsonRepository(),
            EmailService()
        )
        
        binary = use_case.execute(file, environment, target_email)
        return jsonify(binary.to_dict())

    @app.route("/sign", methods=["POST"])
    def sign_file():
        data = request.get_json()
        use_case = SignBinaryUseCase(FileRepository(), JsonRepository(), SigningService())
        result = use_case.execute(data.get("file_id"))
        if result: 
            return jsonify(result.to_dict()), 200
        return jsonify({"error": "Error signing"}), 500

    # --- ESTA ES LA RUTA QUE BUSCA EL CORREO ---
    @app.route('/approve/<file_id>', methods=['GET'])
    def approve_file(file_id):
        sign_use_case = SignBinaryUseCase(FileRepository(), JsonRepository(), SigningService())
        approve_use_case = ApproveBinaryUseCase(sign_use_case)
        
        success = approve_use_case.execute(file_id)
        
        if success:
            return """
            <div style="font-family: sans-serif; text-align: center; padding: 50px;">
                <h1 style="color: #28a745;">¡Archivo Aprobado y Firmado! ✅</h1>
                <p>El proceso de producción ha finalizado correctamente.</p>
                <p>Puede cerrar esta ventana y refrescar su panel de control.</p>
            </div>
            """
        else:
            return "<h1 style='color: red;'>Error ❌</h1><p>El archivo no existe o ya fue firmado.</p>"

    @app.route('/clear', methods=['POST'])
    def clear_history():
        try:
            JsonRepository().delete_all()
            FileRepository().delete_all()
            return jsonify({"msg": "ok"}), 200
        except: 
            return jsonify({"error": "err"}), 500
