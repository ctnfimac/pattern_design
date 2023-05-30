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
    # ruta_db = f'{os.getcwd()}/{carpeta_db}/{nombre_db}'
    # con = sqlite3.connect(ruta_db)
    # cur = con.cursor()
    # cur.execute('SELECT * FROM automovil')
    # for row in cur.fetchall():
    #     print(row)

    # auto = Automovil(1,'Ford','Ka','1.4','00FF00',3000000)
    # print(auto)
    # db = Database()
    # db.connect()
    # db.cur.execute('SELECT * FROM automovil')
    # registros = db.cur.fetchall()
    # print(type(registros))
    # for row in db.cur.fetchall():
    #     print(row)
    # db.disconnect()
    # print(os.getcwd())

    # auto = Automovil(id = 2, marca = 'Volkswagen', modelo='Polo',
    #                  motor='1.6', color='ffffff', precio=5000000)
    auto = Automovil()
   #  autos_obtenidos = auto.getAutomovil(1)
   #  print(autos_obtenidos)

    #agrego un automovil nuevo
    auto.addAutomovil('Ford','Ka','1.4','00FF00',3000000)
  


    
    