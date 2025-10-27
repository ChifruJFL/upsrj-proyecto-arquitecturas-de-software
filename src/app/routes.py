from flask import request, jsonify
from src.application.use_cases import UploadBinaryUseCase
from src.infrastructure.file_repository import FileRepository
from src.infrastructure.json_repository import JsonReporitory

def register_routes(app):
    @app.routes("/upload", methods = ["POST"])
    def uploadfile():
        file = request.files['file']
        environment = request.form.get('environment', 'dev')
        use_case = UploadBinaryUseCase(FileRepository(),JsonReporitory())
        binary = use_case.execute(file, environment)
        return jsonify({'id':binary.id, 'status':binary.status})