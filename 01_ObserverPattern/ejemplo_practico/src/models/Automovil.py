from .Database import Database

class Automovil:
    _id:int
    _marca:str
    _modelo:str
    _motor:str
    _color:str
    _precio:float

    # def __init__(self,id:int, marca:str, modelo:str, 
    #              motor:str, color:str, precio:float)->None:
    #     self._id = id
    #     self._marca = marca
    #     self._modelo = modelo
    #     self._motor = motor
    #     self._color = color
    #     self._precio = precio
    #     self._db = Database()
    def __init__(self, **kwargs)->None:

        if kwargs:
            # print(kwargs['id'])
        # for dato in kwargs.items():
        #     print(dato)
            self._id = id
            self._marca = kwargs['marca']
            self._modelo = kwargs['modelo']
            self._motor = kwargs['motor']
            self._color = kwargs['color']
            self._precio = kwargs['precio']
        self._db = Database()

    def __str__(self) -> str:
        return f'{self._marca} {self._modelo}'


    def getAutomovil(self, id:int = None) -> list:
        try:
            self._db.connect()
            if id:
                self._db.cur.execute('SELECT id, marca, modelo, motor, color, precio FROM automovil WHERE id=?', (id,))
            else:
                self._db.cur.execute('SELECT * FROM automovil')
            registros = self._db.cur.fetchall()
            self._db.disconnect()
            return registros
        except Exception as e:
            print(f'Error en getAutomovil: {e.__str__()}')


    def addAutomovil(self, *kwargs) -> None:
        try:
            self._db.connect()
            self._db.cur.execute('INSERT INTO automovil VALUES(?,?,?,?,?)', kwargs)
            self._db.conexion.commit()
            self._db.disconnect()
        except Exception as e:
            print(f'Error en addAutomovil: {e.__str__()}')       


        