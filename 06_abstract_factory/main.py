"""
Instrucciones:
1.Completen las Clases de Productos:
•	ElectricCar debe implementar Vehicle y mostrar el mensaje "Ensamblando un auto eléctrico".
•	GasCar debe implementar Vehicle y mostrar el mensaje "Ensamblando un auto de combustión".
•	ElectricEngine debe implementar Engine y mostrar el mensaje "Arrancando motor eléctrico".
•	GasEngine debe implementar Engine y mostrar el mensaje "Arrancando motor de combustión".

2.	Completen las Clases de Fábricas:
•	ElectricVehicleFactory debe crear un ElectricCar y un ElectricEngine.
•	GasVehicleFactory debe crear un GasCar y un GasEngine.

3. Prueben el Código:
    •	Ejecuten el código para asegurarse de que cada fábrica produce el tipo correcto de vehículo y motor.
"""

from abc import ABC, abstractmethod

#
class Vehicle(ABC):
    @abstractmethod
    def _assemble(self) -> None:
        pass


class Engine(ABC):
    @abstractmethod
    def _start(self) -> None:
        pass


class Batery(ABC):
    @abstractmethod
    def _connect(self) -> None:
        pass

##
class ElectricCar(Vehicle):
    def _assemble(self) -> None:
        print("Ensamblando un auto eléctrico")


class GasCar(Vehicle):
    def _assemble(self) -> None:
        print("Ensamblando un auto de combustión")


class ElectricEngine(Engine):
    def _start(self) -> None:
        print("Arrancando motor eléctrico")


class GasEngine(Engine):
    def _start(self) -> None:
        print("Arrancando motor de combustión")


class ElectricBatery(Batery):
    def _connect(self) -> None:
        print("Conectando Bateria con cero emisiones y alta eficiencia")


class GasBatery(Batery):
    def _connect(self) -> None:
        print("Conectando Bateria común")

###
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

    @abstractmethod
    def create_engine(self) -> Engine:
        pass

    @abstractmethod
    def connect_batery(self) -> Batery:
        pass

####
class ElectricVehicleFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return ElectricCar()

    def create_engine(self) -> Engine:
        return ElectricEngine()
    
    def connect_batery(self) -> Batery:
        return ElectricBatery()
    

class GasVehicleFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return GasCar()

    def create_engine(self) -> Engine:
        return GasEngine()
    
    def connect_batery(self) -> Batery:
        return GasBatery()
    


def main(factory:VehicleFactory):
    vehicle = factory.create_vehicle()
    engine = factory.create_engine()
    batery = factory.connect_batery()

    vehicle._assemble()
    engine._start()
    batery._connect()

if __name__ == "__main__":
    print("Creando vehículo eléctrico:")
    main(ElectricVehicleFactory())

    print("\nCreando vehículo de combustión:")
    main(GasVehicleFactory())