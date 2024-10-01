import os, requests
from dotenv import load_dotenv
from src.pattern.observer.base.patron_observador import Observer
from src.pattern.observer.base.patron_observador import Subject

load_dotenv()

class SuscriptorSlackAutomovilCrud(Observer):

    def __init__(self, url_canal_slack: str):
        self.url_canal_slack = url_canal_slack 

    
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
        
        self.enviar_notificacion_a_slack(msg)
        

    def enviar_notificacion_a_slack(self, msg: str):
        url = f"{os.getenv('SLACK_URL_API')}{self.url_canal_slack}"
        context = {'text': msg}
        response = requests.post(url, json=context)
        if response.status_code == 200:
            print('Mensaje enviado a slack exitoso')
        else:
            print('Error al querer enviar el mensaje a slack')
