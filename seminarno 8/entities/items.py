from errors import*
class Item:
    def __init__(self,name):
        if type(name) != str:
                raise InvalidDataFormat()
        self.name = name
        self.durability = 100

    def print(self):
        print(f"Item: {self.name}, {self.durability}")    