from .Subject import Subject
from .Observer import Observer
from typing import List

class SubjectAutomovil(Subject):

    _crud: str = ''
    _observers: List[Observer] = []

    def add(self, observer:Observer) -> None:
        self._observers.append(observer)

    def delete(self, observer:Observer) -> None:
        self._observers.remove(observer)
 
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    # metodos de la logica de negocio
    def operation(self, action: str) -> None:
        self._crud = action
        self.notify()