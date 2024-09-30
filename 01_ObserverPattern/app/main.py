"""La idea es poder hacer un crud completo de una tabla
   llamada auto, en donde tendra dos tipos de observadores
   Email y Slack
"""
from src.models.Automovil import Automovil
from src.pattern.observer.email.suscriptor_automovil_crud import SuscriptorEmailAutomovilCrud


if __name__ == "__main__":

   auto = Automovil()

   suscriptor1 = SuscriptorEmailAutomovilCrud("info@christianperalta.com.ar")
   suscriptor2 = SuscriptorEmailAutomovilCrud("info@christianperalta.com.ar")
   
   auto.agregar_suscriptor(suscriptor1)
   auto.agregar_suscriptor(suscriptor2)
   
   auto_obtenido = auto.getAutomovil(1)
   print(auto_obtenido)

   #autos_obtenidos = auto.getAutomovil()
   #print(autos_obtenidos)

   #agrego un automovil nuevo
   #auto.addAutomovil('Volkswagen','Golf','Turbo','FFFFFF',60500000)

   #edito un automovil
   #auto.updateAutomovil(5, modelo='Eliminar', precio=0)
    
   #elimino un automovil
   #auto.deleteAutomovil(5)


    