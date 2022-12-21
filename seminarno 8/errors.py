class InvalidCharacterClass:
    def __init__(self, *args):
        message = f"Error: Invalid Character Class"
        super().__init__(message, *args)

class InvalidDataFormat:
    def __init__(self, *args):
        message = f"Error: Invalid Data Format"
        super().__init__(message, *args)

class CharacterExists:
    def __init__(self, *args):
        message = f"Erros: Character Exists"
        super().__init__(message, *args)

class InvalidCommand:
    def __init__(self, *args):
        message = f"Error: Invalid Command"
        super().__init__(message, *args)

class UserNotExists:
    def __init__(self, *args):
        message = f"Error: User Not Exists"
        super().__init__(message, *args)        