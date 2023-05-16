"""
Este patron de diseño sirve para hacer un seguimiento a las actividades que tenga un "Sujeto".
El o los que hacen este seguimiento son los "Observadores", puedo tener varios por ejemplo uno que observe 
si el Sujeto(en caso que sea un auto) si exede el limite de velocidad, y otro observador que indique si estoy 
acelerando o frenando, otro observador que indique si hay algun desperfecto en el auto.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Subject(ABC):
   
    @abstractmethod
    def subscribe(self, observador):
        pass
   
    @abstractmethod
    def unsubscribe(self, observador):
        pass
   
    @abstractmethod    
    def notify(self):
        pass


class ConcreteSubject(Subject):
    _crud: str = None
    _resultado: int = None
    _observers: List[Observer] = []
   
    def subscribe(self, observador):
        self._observers.append(observador)
       
    def unsubscribe(self, observador):
        self._observers.remove(observador)
       
    def notify(self):
        print('Notificando observadores:')
        for observer in self._observers:
            observer.update(self)

    # metodos de la logica de negocio      
    def addTwoNumbers(self, a, b):
        self._resultado = a + b
        self.notify()
   
    def operationCrud(self, operacion:str):
        self._crud = operacion
        self.notify()
   
   
class Observer(ABC):
    @abstractmethod
    def update(self, subject:Subject) -> None:
        pass
   

class OperationsObserverA(Observer):
   
    def update(self, subject:Subject) -> None:
        if subject._resultado:
            if subject._resultado >= 0:
                print('ObservadorA detecto resultado positivo o 0')
            elif subject._resultado < 0:
                print('ObservadorA detecto resultado negativo')
        else:
            print('ObservadorA No detecto operación')
            
        subject._resultado = None


class CrudObserverB(Observer):
    def update(self, subject:Subject) -> None:
        if subject._crud == 'Alta':
            print('ObservadorB agrego nuevo registro')
        elif subject._crud == 'Baja':
            print('ObservadorB elimino un registro')
        elif subject._crud == 'Modifica':
            print('ObservadorB Modificó un registro')
        elif subject._crud == 'Ver':
            print('ObservadorB Obtuvo un registro')
        else:
            print('ObservadorB No detecto operacion')
        subject._crud = None




if __name__ == '__main__':
    subject = ConcreteSubject()
    observer_a = OperationsObserverA()
    observer_b = CrudObserverB()
   
    subject.subscribe(observer_a)
    subject.subscribe(observer_b)
    
    print('\nsumaDosNumeros(4,-8)')
    subject.addTwoNumbers(4,-8)

    print("\noperacionCrud('Alta')")
    subject.operationCrud('Alta')

    print('\nsumaDosNumeros(4,0)')
    subject.addTwoNumbers(4,0)
   
    subject.unsubscribe(observer_a)

    print('\nsumaDosNumeros(4,1)')
    subject.addTwoNumbers(4,1)