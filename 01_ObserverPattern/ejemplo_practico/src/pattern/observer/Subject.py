from abc import ABC, abstractmethod
# from .Observer import Observer


class Subject(ABC):

    @abstractmethod
    def add(self, observer) -> None:
        pass

    @abstractmethod
    def delete(self, observer) -> None:
        pass

    @abstractmethod 
    def notify(self) -> None:
        pass