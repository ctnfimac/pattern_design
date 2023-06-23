from abc import ABC, abstractmethod
# from .Subject import Subject


class Observer(ABC):

    @abstractmethod
    def update(self, subject) -> None:
        pass
