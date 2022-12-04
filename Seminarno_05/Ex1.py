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
        return

    def daily_task(self):
        return


class Jaguar(JungleAnimal):
    def __init__(self,name,age,sound):
        if age > 15:
            raise InvalidAgeError(age)
        if str(sound).count("r") < 2:
            raise InvalidSoundError(sound)

        super().__init__(name, age, sound)

    def print(self):
        print(f"Jaguar {self.name}, {self.age}, {self.sound}")

    def daily_task(*animals):
        for a in animals:
            if type(a) == "Lemur" or "Human":
                animals



