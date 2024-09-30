import sys, os
from dotenv import load_dotenv
from smtplib import SMTP_SSL as SMTP # this invokes the secure SMTP protocol (port 465, uses SSL)
from email.mime.text import MIMEText
from src.pattern.observer.base.patron_observador import Observer
from src.pattern.observer.base.patron_observador import Subject

load_dotenv()

SMTPserver = os.getenv('SMTP_EMAIL_SERVER')
sender = os.getenv('SMTP_EMAIL_FROM')

USERNAME = os.getenv('SMTP_EMAIL_USERNAME')
PASSWORD = os.getenv('SMTP_EMAIL_PASSWORD')

#plain, html, xml
text_subtype = 'plain'

subject="Patron de diseño Observer"

class SuscriptorEmailAutomovilCrud(Observer):

    def __init__(self, email: str):
        self.email = email 

    
    def update(self, subject:Subject) -> None:
        msg= f'Le informamos que '

        if subject._accion_crud == 'Alta':
            msg += 'se Agrego un nuevo Automovil'
        elif subject._accion_crud == 'Baja':
            msg += 'se Elimino un Automovil'
        elif subject._accion_crud == 'Modifica':
            msg += 'se Modificó un Automovil'
        elif subject._accion_crud == 'Ver':
            msg += 'se Visualizó la información uno o varios Automoviles.'
        else:
            msg += 'hubo una operación desconocida.'
        
        self.enviar_email(msg)
        


    def enviar_email(self, msg: str):
        try:
            msg = MIMEText(msg, text_subtype)
            msg['Subject'] = subject
            msg['From'] = sender 

            conn = SMTP(SMTPserver)
            conn.set_debuglevel(False)
            conn.login(USERNAME, PASSWORD)
            try:
                conn.sendmail(sender, self.email, msg.as_string())
            finally:
                conn.quit()

        except:
            sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message
  