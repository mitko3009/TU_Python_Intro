from items import *
from errors import*

class Wapon(Item):
    def __init__(self, name,attack):
        super().__init__(name)
        if type(name) != str or type(attack) != str:
                raise InvalidDataFormat()
        self.attack = attack

    def print(self):
        print(f"Wapon: {self.name}. {self.durability}, {self.attack}")    
