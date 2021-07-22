class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello {self.name}')

me = User('Kyle')
me.greet()


# class phone:
#     def __init__(self, phone_number):
#         self.number = phone_number

#     def call(self, other_number):
#         print(f'calling {other_number}.')

#     def text(self, other_number, message):
#         print(f'texting {message} to {other_number}')


# class Iphone(phone):
#     def __init__(self, phone_number):
#         super().__init__(phone_number)
#         self.fingerprint = None

#     def set_fingerPrint(self, fingerPrint):
#         self.fingerprint = fingerPrint

#     def unlock(self, fingerPrint = None):
#         if(fingerPrint == self.fingerprint):
#             print("phone unlocked")
#         else:
#             print('phone locked')


# # myPhone = phone('555-555-555')

# # myPhone.call('888-888-888')


# myIphone = Iphone('555-555-555')
# print(myIphone.number)


# myIphone.set_fingerPrint('hi')

# myIphone.unlock('hi')

class BankAccount:
    def __init__(self, accountType, balance):
        self.accountType = accountType
        self.balance = balance

    def checkBal(self):
        print(f'this is a {self.accountType} self and the balance is {self.balance}')

    def deposit(self, depositAmount):
        depositAmount = input('How much would you like to deposit?\n')
        self.balance += int(depositAmount)
        print(f'your new self balance is {self.balance}')

    def withdraw(self, withdrawAmount):
        withdrawAmount = input('how much would you like to withdraw?\n')
        if(self.balance > withdrawAmount):
            self.balance =- int(withdrawAmount)
            print(f'your new self balance is {self.balance}')
        else:
            print('You dont not have enough available funds.')
            return False

    def accumulate_interest(self, interestAmount):
        interestAmount = self.balance * .02
        self.balance += self.balance + interestAmount
        print(self.balance)



class ChildrensAccount(BankAccount):
    def __init__(self, balance ):
        super().__init__(balance)

    def accumulate_interest(self, interestAmount):
        return super().accumulate_interest(interestAmount)


ChildAccount = ChildrensAccount(0)

ChildAccount.accumulate_interest()



# myBank = BankAccount('checking', 0)

# myBank.startBank()

# myBank.deposit(depositAmount=1)

# myBank.withdraw(withdrawAmount=1)