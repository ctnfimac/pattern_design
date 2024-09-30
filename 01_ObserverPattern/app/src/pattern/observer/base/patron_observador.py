from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, subject) -> None:
        pass



class Subject(ABC):

    @abstractmethod
    def agregar_suscriptor(self, suscriptor: Observer) -> None:
        pass

    @abstractmethod
    def eliminar_suscriptor(self, suscriptor: Observer) -> None:
        pass

    @abstractmethod 
    def notificar_suscriptores(self) -> None:
        pass