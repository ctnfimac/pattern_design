"""La idea es poder hacer un crud completo de una tabla
   llamada auto, en donde tendra dos observadores
   observador 1: guardará en un log las distintas operaciónes de un crud
   observarod 2: guardará en un log si un auto cambia de motor o color
"""
import os
import sqlite3
from src.models.Automovil import Automovil
from src.models.Database import Database

# Carpeta donde se encuentra la base de datos Sqlite3 a utilizar
carpeta_db = 'db'
nombre_db = 'test.db'

if __name__ == "__main__":

    # auto = Automovil(id = 2, marca = 'Volkswagen', modelo='Polo',
    #                  motor='1.6', color='ffffff', precio=5000000)
    auto = Automovil()
   #  autos_obtenidos = auto.getAutomovil(1)
   #  print(autos_obtenidos)

    #agrego un automovil nuevo
    #auto.addAutomovil('Ford','Ka','1.4','00FF00',3000000)
    
    #elimino un automovil
   #  auto.deleteAutomovil(4)

    #edito un automovil
    auto.updateAutomovil(1, modelo='Gol Trend', precio=4000000)
  


    
    