from .Observer import Observer
from .Subject import Subject


class ObserverAutomovilCrud(Observer):

    _estadoObservador = None
    
    def update(self, subject:Subject) -> None:
        if subject._crud == 'Alta':
            print('ObservadorCrud agrego nuevo Automovil')
        elif subject._crud == 'Baja':
            print('ObservadorCrud elimino un Automovil')
        elif subject._crud == 'Modifica':
            print('ObservadorCrud Modificó un Automovil')
        elif subject._crud == 'Ver':
            print('ObservadorCrud Obtuvo un Automovil o varios.')
        else:
            print('ObservadorCrud No detecto operacion')
        subject._crud = None
