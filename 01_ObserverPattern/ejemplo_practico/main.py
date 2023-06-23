"""La idea es poder hacer un crud completo de una tabla
   llamada auto, en donde tendra dos observadores
   observador 1: guardará en un log las distintas operaciónes de un crud
   observarod 2: guardará en un log si un auto cambia de motor o color
"""

from src.models.Automovil import Automovil


# Carpeta donde se encuentra la base de datos Sqlite3 a utilizar
carpeta_db = 'db'
nombre_db = 'test.db'

if __name__ == "__main__":

   auto = Automovil()
   #  autos_obtenidos = auto.getAutomovil(1)
   autos_obtenidos = auto.getAutomovil()
   print(autos_obtenidos)

   #agrego un automovil nuevo
   # auto.addAutomovil('Chevrolet','Onix','1.4','00FFFF',3500000)
    
   #elimino un automovil
   # auto.deleteAutomovil(4)

   #edito un automovil
   # auto.updateAutomovil(4, modelo='Prisma', precio=5000000)
  


    
    