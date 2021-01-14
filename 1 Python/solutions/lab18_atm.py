
class ATM:
    def __init__(self):
        self.balance = 0
        self.interest = 0.001
        self.transactions = []

    def get_balance(self):
        self.transactions.append(f"Checked balance: {round(self.balance, 2):.2f}")
        return round(self.balance, 2)

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount:.2f}, balance: {round(self.balance, 2):.2f}")

    def check_withdrawal(self, amount):
        return self.balance >= amount

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"Withdrew: {round(amount, 2):.2f}, balance: {round(self.balance, 2):.2f}")

    def calc_interest(self) :
        interest = round(self.balance * self.interest, 2)
        self.transactions.append(f"Interest payment: {round(interest, 2):.2f}, balance: {round(self.balance + interest, 2):.2f}")
        return interest
    


atm = ATM() # create an instance of our class
# account = ATM()
# account.check_withdrawal()

print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.get_balance() # call the get_balance() method
        print(f'Your balance is ${balance:.2f}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount:.2f}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount:.2f}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${round(amount, 2)} in interest')
    elif command == 'transactions':
        for item in atm.transactions:
            print(item)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - print list of transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')