from flask_mail import Message
from flask import current_app, url_for

class EmailService:
    def send_approval_email(self, recipient_email: str, file_id: str, filename: str):
        try:
            approval_link = url_for('approve_file', file_id=file_id, _external=True)

            # --- CUERPO EN HTML ---
            html_body = f"""
            <div style="font-family: Arial, sans-serif; padding: 20px;">
                <h2 style="color: #004aad;">Solicitud de Aprobación para Producción</h2>

                <p>El archivo <strong>{filename}</strong> ha sido subido y requiere aprobación para ser firmado digitalmente.</p>

                <p style="margin-top: 25px;">
                    <a href="{approval_link}" 
                       style="
                           background-color: #007bff;
                           color: white;
                           padding: 12px 20px;
                           text-decoration: none;
                           font-size: 16px;
                           border-radius: 6px;
                           display: inline-block;">
                        ✔ Aprobar archivo
                    </a>
                </p>

                <p>O puede abrir el siguiente enlace si el botón no funciona:</p>

                <p><a href="{approval_link}">{approval_link}</a></p>

                <hr style="margin-top: 30px;">
                <p style="font-size: 12px; color: #666;">
                    Si usted no solicitó esto, puede ignorar el mensaje.
                </p>
            </div>
            """

            # --- CUERPO EN TEXTO PLANO ---
            text_body = (
                "SOLICITUD DE FIRMA PARA PRODUCCIÓN\n\n"
                f"El archivo '{filename}' está en espera de aprobación.\n\n"
                "Para aprobarlo haga clic en el siguiente enlace:\n"
                f"{approval_link}\n\n"
                "Si no solicitó esto, ignore este mensaje."
            )

            msg = Message(
                subject=f"Requiere Aprobación: {filename}",
                recipients=[recipient_email],
                body=text_body,
                html=html_body
            )

            current_app.mail.send(msg)
            print(f" Correo HTML enviado a {recipient_email}")
            return True

        except Exception as e:
            print(f" Error enviando correo: {e}")
            return False
