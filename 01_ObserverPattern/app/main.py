"""La idea es poder hacer un crud completo de una tabla
   llamada auto, en donde tendra dos tipos de observadores
   Email y Slack
"""
from src.models.Automovil import Automovil
from src.pattern.observer.email.suscriptor_automovil_crud import SuscriptorEmailAutomovilCrud
from src.pattern.observer.slack.suscriptor_slack_automovilcrud import SuscriptorSlackAutomovilCrud


if __name__ == "__main__":

   auto = Automovil()

   suscriptor_email_1 = SuscriptorEmailAutomovilCrud("ingreso_email_corporativo")
   suscriptor_slack_1 = SuscriptorSlackAutomovilCrud('T07PJF93HN0/B07PUB7V2UC/DTz4glJGMXPPr1odMcZGCUCK')
   
   auto.agregar_suscriptor(suscriptor_email_1)

   auto.agregar_suscriptor(suscriptor_slack_1)

   auto_obtenido = auto.getAutomovil(1)
   #print(auto_obtenido)

   #autos_obtenidos = auto.getAutomovil()
   #print(autos_obtenidos)

   #agrego un automovil nuevo
   auto.addAutomovil('Volkswagen','Virtus','Turbo','FF00FF',61000000)

   #edito un automovil
   #auto.updateAutomovil(5, modelo='Eliminar', precio=0)
    
   #elimino un automovil
   #auto.deleteAutomovil(5)


    