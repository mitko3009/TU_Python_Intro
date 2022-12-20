from user import *
from account import *

class InvalidUserData:
    def __init__(self, *args):
        message = f"Invalid user data"
        super().__init__(message, *args)

class UserNotFound:
    def __init__(self, *args):
        message = f"User not found"
        super().__init__(message, *args)

class UserAlreadyExists:
    def __init__(self, *args):
        message = f"User already exists"
        super().__init__(message, *args)

class UserAlreadyOwnsAccount:
    def __init__(self, *args):
        message = f"User already owns account"
        super().__init__(message, *args)

class AccountNotFound:
    def __init__(self, *args):
        message = f"Account not found"
        super().__init__(message, *args)

class UnsufficientBalance:
    def __init__(self, *args):
        message = f"Unsufficient balance"
        super().__init__(message, *args)

class InvalidAccountData:
    def __init__(self, *args):
        message = f"Invalid account data"
        super().__init__(message, *args)

class InvalidAccountType:
    def __init__(self, *args):
        message = f"Invalid account type"
        super().__init__(message, *args)

class InvalidMenuChoice:
    def __init__(self, *args):
        message = f"Invalid menu choice"
        super().__init__(message, *args)

users = []
users.append(User("Ivan","111111"))
users.append(User("Nikola","222222"))
users.append(User("Misho","333333"))
users.append(User("Gosho","444444"))
users.append(User("Kiril","55555"))
users.append(User("Sasho","666666"))

egns = []
egns.append("111111")
egns.append("222222")
egns.append("333333")
egns.append("444444")
egns.append("555555")
egns.append("666666")



while True:
    print("1. Create user")
    print("2. Create user account")
    print("3. Print all users")
    print("4. Print all user`s accounts")
    print("5. Deposit money on users account")
    print("6. Withdraw money from user`s account")
    print("7. Exit")
    choice = input("Choose an item from the menu: \n> ")



    if choice == "1":
        name = input("Enter name: ")
        eng = input("Enter egn: ")
        users.append(User(name,eng))
        egns.append(eng)

    elif choice == "2":
       egn = input("Enter user`s egn: ")
       if egns.__contains__(egn):
           iban = input("Enter iban: ")
           currency = input("Enter currency: ")
           type = input("Enter type: ")
           for u in users:
               if u.egn == egn:
                   u.add_account(Account(iban,currency,type))
       else:
           raise AccountNotFound

    elif choice == "3":
       for u in users:
           u.get_print()

    elif choice == "4":
        egn = input("Enter user`s egn: ")
        if egns.__contains__(egn):
            for u in users:
                if u.egn == egn:
                    print(u.accounts)
        else:
            raise AccountNotFound

    elif choice == "5":
        egn = input("Enter user`s egn: ")
        if egns.__contains__(egn):
            for u in users:
                if u.egn == egn:
                    iban = input("Enter account iban")
                    amount = input("Enter amount to deposit: ")

        else:
            raise AccountNotFound

    elif choice == "6":
        egn = input("Enter user`s egn: ")
        if egns.__contains__(egn):
            for u in users:
                if u.egn == egn:
                    iban = input("Enter account iban")
                    amount = input("Enter amount to withdraw: ")

        else:
            raise AccountNotFound

    elif choice == "7":
        break
    else:
        print("Error: Invalid choice\n")