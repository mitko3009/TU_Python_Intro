import random


class InvalidParameterError(Exception):
    def __init__(self, name,*args):
        message = f"Invalid class parameter: {name}"
        super().__init__(message,*args)

class MissingParameterError(Exception):
    pass

class InvalidAgeError(InvalidParameterError):
    def __init__(self, age, *args):
        super().__init__(age, *args)

class InvalidSoundError(InvalidParameterError):
    def __init__(self, sound, *args):
        super().__init__(sound, *args)

class JungleAnimal:
    def __init__(self,name,age,sound):
        if type(name) != str:
            raise InvalidParameterError(name)
        if type(age) != int:
            raise InvalidAgeError(age)
        if type(sound) != str:
            raise InvalidParameterError(sound)

        self.name = name
        self.age = age
        self.sound = sound


    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    def print(self):
        pass

    def daily_task(self):
        pass


class Jaguar(JungleAnimal):
    def __init__(self,name,age,sound):
        super().__init__(name, age, sound)
        if age > 15:
            raise InvalidAgeError(age)
        if self.sound.count("r") < 2 or self.sound.count("R") < 2:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"Jaguar {self.name}, {self.age}, {self.sound}")

    def daily_task(self, animals):
        for a in animals:
            if type(a) == Lemur or type(a) == Human:
                print(f"{self.name} the Jaguar hunted down {animals[a].name} the {type(animals[a]).__name__}")
                animals.pop(a)
                break



class Lemur(JungleAnimal):
    def __init__(self,name,age,sound):
        super().__init__(name, age, sound)
        if self.age > 10:
            raise InvalidAgeError(age)
        if 'e' not in self.sound:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"f{self.name}, {self.age}, {self.sound}")

    def daily_task(self, fruitsCount):
        if fruitsCount >= 10:
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return  fruitsCount - 10

        if fruitsCount < 10:
            print(f"{self.name} the Lemur could only find {fruitsCount} fruits")
            return 0
        if fruitsCount <= 0:
            super().make_sound()
            super().make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            return 0



class Human(JungleAnimal):
    def __init__(self,name,age,sound):
        super().__init__(name, age, sound)
        if self.age > 10:
            raise InvalidAgeError(age)
        if 'e' not in self.sound:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"{self.name}, {self.age}, {self.sound}")

    def daily_task(self, animals, buildings):
        for i in range(len(animals)):
            if animals[0] == self:
                if type(animals[i + 1]) == Human:
                    buildings.append(Building())
            if animals[len(animals - 1)] == self:
                if type(animals[len(animals) - 2]) == Human:
                    buildings.append(Building())
            if i != 0 and i != len(animals) - 1:
                if type(animals[i + 1]) == Human or type(animals[i - 1]) == Human:
                    buildings.append(Building())



class Building:
    def __init__(self,buildingType = "Hut"):
        self.buildingType = buildingType

# MAIN LOGIC:

fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

for i in range(102):
   number = random.randint(0, 9)

   if number >= 0 and number <=3:
       age = random.randint(1,20)
       name = names[random.randint(1,len(names) - random.randint(1,15))]
       sound = sounds[random.randint(1,len(sounds) - random.randint(1,8))]
       animals.append(Lemur(name,age,sound))

   if number >= 4 and number <=7:
       age = random.randint(1,20)
       name = names[random.randint(1,len(names) - random.randint(1,15))]
       sound = sounds[random.randint(1,len(sounds) - random.randint(1,8))]
       animals.append(Jaguar(name,age,sound))

   if number >= 8 and number <=9:
       age = random.randint(1,20)
       name = names[random.randint(1,len(names) - random.randint(1,15))]
       sound = sounds[random.randint(1,len(sounds) - random.randint(1,8))]
       animals.append(Human(name,age,sound))


print(f"The jungle now has {len(animals)} animals")


for anim in animals:
    if type(anim) == Lemur:
        anim.daily_task(fruits)
    if type(anim) == Jaguar:
        anim.daily_task(animals)
    if type(anim) == Human:
        anim.daily_task(animals,buildings)



print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)
