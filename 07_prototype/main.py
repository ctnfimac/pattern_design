from abc import ABC, abstractmethod
# from copy import deepcopy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Pokemon(Prototype):
    
    def __init__(self, name:str, type:str, level:str, attacks:list[str]):
        self.name = name
        self.type = type
        self.level = level
        self.attacks = attacks


    def clone(self):# -> Pokemon: # type: ignore
        return Pokemon(self.name, self.type, self.level, self.attacks)

    def display_info(self) -> None:
        print(f"Nombre: {self.name}\nTipo: {self.type}\nNivel: {self.level}\nAtaques: {','.join(self.attacks)}")
        



if __name__ == "__main__":
    charizard_obj = Pokemon("Charizard", "Fuego", "3", ["Llama", "Ataque sismico"])

    print("CHARIZARD 1:")
    print(charizard_obj)
    charizard_obj.display_info()

    """
    print("\nDe esta forma tambien modifico el charizard 1 lo cual no es la idea\n")
    print("CHARIZARD 2:")
    charizard_obj_2 = charizard_obj
    charizard_obj_2.name = "Charmander"
    charizard_obj_2.level = "1"
    print(charizard_obj_2)
    charizard_obj_2.display_info()

    print("\n")
    print("CHARIZARD 1:")
    charizard_obj.display_info()
    """

    print("\nCHARIZARD 3:")
    charizard_obj_3 = charizard_obj.clone()
    charizard_obj_3.name = "Charmileon"
    charizard_obj_3.level = "2"
    print(charizard_obj_3)
    charizard_obj_3.display_info()

    print("\n")
    print("CHARIZARD 1:")
    print(charizard_obj)
    charizard_obj.display_info()

    """
    En python en vez de definir la interfaz se puede usar directamente deepcopy 
    """