from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def add_email_field(self):
        pass
    
    @abstractmethod
    def add_nombre_field(self):
        pass

    @abstractmethod
    def add_apellido_field(self):
        pass

    @abstractmethod
    def add_dni_field(self):
        pass

    @abstractmethod
    def add_password_field(self):
        pass

    @abstractmethod
    def add_password2_field(self):
        pass

    @abstractmethod
    def build(self):
        pass

    