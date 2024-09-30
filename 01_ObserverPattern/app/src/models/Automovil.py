from .Database import Database
from src.pattern.observer.email.email_subject import EmailSubject

class Automovil(EmailSubject):
    _id:int
    _marca:str
    _modelo:str
    _motor:str
    _color:str
    _precio:float


    def __init__(self, **kwargs)->None:
        super().__init__()
        if kwargs:
            self._id = id
            self._marca = kwargs['marca']
            self._modelo = kwargs['modelo']
            self._motor = kwargs['motor']
            self._color = kwargs['color']
            self._precio = kwargs['precio']
        self._db = Database()
        #self.__subject = SubjectAutomovil()
        #observer_crud = ObserverAutomovilCrud()
        #self.__subject.add(observer_crud)

    def __str__(self) -> str:
        return f'{self._marca} {self._modelo}'


    def getAutomovil(self, id:int = None) -> list:
        try:
            self._db.connect()
            if id:
                self._db.cur.execute('SELECT rowid, marca, modelo, motor, color, precio FROM automovil WHERE rowid=?', (id,))
            else:
                self._db.cur.execute('SELECT rowid, marca, modelo, motor, color, precio FROM automovil')
            registros = self._db.cur.fetchall()
            self._db.disconnect()
            self.notificar_la_operacion('Ver')
            return registros    
        except Exception as e:
            print(f'Error en getAutomovil: {e.__str__()}')


    def addAutomovil(self, *args) -> None:
        try:
            self._db.connect()
            self._db.cur.execute('INSERT INTO automovil VALUES(?,?,?,?,?)', args)
            self._db.conexion.commit()
            self._db.disconnect()
            self.notificar_la_operacion('Alta')
        except Exception as e:
            print(f'Error en addAutomovil: {e.__str__()}')   


    def deleteAutomovil(self, rowId:int) -> None:
        try:
            if rowId:
                self._db.connect()
                self._db.cur.execute('DELETE FROM automovil WHERE rowid = ?', (rowId,))
                self._db.conexion.commit()
                self._db.disconnect()
                #self.__subject.operation('Baja')
                self.notificar_la_operacion('Baja')
        except Exception as e:
            print(f'Error en deleteAutomovil: {e.__str__()}')  


    def updateAutomovil(self, id, **kwargs) -> None:
        try:
            query_sets = ''
            for key, value in kwargs.items():
                if type(value) == str:
                    value = f"'{value}'"
                query_sets = query_sets + f'{key} = {value}, '

            query = f"""UPDATE automovil SET {query_sets[:-2]} WHERE rowid = ?"""
            self._db.connect()
            self._db.cur.execute(query, (id,))
            self._db.conexion.commit()
            self._db.disconnect()
            #self.__subject.operation('Modifica')
            self.notificar_la_operacion('Modifica')
        except Exception as e:
            print(f'Error en updateAutomovil: {e.__str__()}')      


        