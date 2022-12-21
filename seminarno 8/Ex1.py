from entities.character import Character
from entities.wapon import Wapon
from entities.items import Item
from errors import *

characters = []
names = []


class Menu:
    def print_menu(self):
        print("1. Create a new character")

    def command_create_character(self, name, sex, ch_class):
        pass

    def run(self):
        # infinite menu loop
        while True:  
            print("1: Create new character.")
            print("2: Create wapon on existing character.")
            print("3: Create item on existing character.")
            print("4: Print all characters.")
            print("5: Delete character")
            print("6: Exit")
            choice = input("Choose an item from the menu: \n> ")
         
            try:
                if choice == "1":                    
                    name = input("Enter the character name: ")
                    gender = input("Enter the character gender: ")
                    class_in_game = input("Enter the character class_in_game: ")
                    
                    if name in names:
                        raise CharacterExists

                    characters.append(Character(name,gender,class_in_game))
                    names.append(name)

                elif choice == "2":
                     
                    name = input("Enter character name: ")
                    if name in names:
                        waponName = input("Enter wapon name")
                        attack = input("Enter wapon attack")

                        for c in characters:
                            if c.name == name:
                                c.main_wapon = Wapon(waponName,attack)
                    else:
                        raise UserNotExists       

                elif choice == "3":

                    name = input("Enter character name: ")
                    if name in names:
                        itemName = input("Enter item name")

                        for c in characters:
                            if c.name == name:
                                c.external_item = Item(itemName)
                    else:
                        raise UserNotExists 

                elif choice == "4":

                    for c in characters:
                        c.print()

                elif choice == "5":

                    name = input("Enter character name: ")
                    if name in names:
                        for c in characters:
                            if c.name == name:
                                characters.remove(c)
                                names.remove(c.name)
                    else:
                        raise UserNotExists
                if choice == "6":
                    break

                else:
                    raise InvalidCommand
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()