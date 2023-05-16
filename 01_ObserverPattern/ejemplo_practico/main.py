"""La idea es poder hacer un crud completo de una tabla
   llamada auto, en donde tendra dos observadores
   observador 1: guardará en un log las distintas operaciónes de un crud
   observarod 2: guardará en un log si un auto cambia de motor o color
"""
import os
import sqlite3

# Carpeta donde se encuentra la base de datos Sqlite3 a utilizar
carpeta_db = 'db'
nombre_db = 'test.db'

if __name__ == "__main__":
    try:
        ruta_db = f'{os.getcwd()}/{carpeta_db}/{nombre_db}'
        con = sqlite3.connect(ruta_db)
        cur = con.cursor()
        cur.execute('SELECT * FROM automovil')
        # print(cur.fetchall())
        for row in cur.fetchall():
            print(row)
        # print('Hola')
        # print(f'{os.getcwd()}')
    except Exception as e:
        print(f'Error para conectarse con la db {e.__str__()}')
    