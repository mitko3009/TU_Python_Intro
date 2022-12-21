from errors import*
class Character:
    CH_TYPES = ("Warrior", "Mage","Priest", "Rogue")

    def __init__(self,name,gender,class_in_game):
        if class_in_game not in Character.CH_TYPES:
            raise InvalidDataFormat()
        if type(name) != str or type(gender) != str:
                raise InvalidDataFormat()       
        self.name = name
        self.gender = gender
        self.class_in_game = class_in_game
        self.main_wapon = None
        self.external_item = None

    def print(self):
        print(f"Character:{self.name}, {self.gender}, {self.class_in_game}, Wapon: {self.main_wapon}, Item: {self.external_item}")    