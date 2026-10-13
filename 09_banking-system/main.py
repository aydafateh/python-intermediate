class Menus:
    def main_menu(self):
        menu = {
            "1" : "check balance",
            "2" : "transfer money",
            "3" : "deposit money",
            "4" : "withdraw money",
            "5" : "transection history",
            "6" : "user information",
            "7" : "change pin",
            "8" : "Exit"
        }
        return menu
    def user_info(self, name, phone, account):
        user = {
            "name" : name,
            "phone" : phone,
            "account" : account
        }
        return user

class Validator:
    @staticmethod
    def check_information(name:str, phone:str, account:str) -> bool:
        if name and name.replace(" ", "").isalpha() and phone.startswith("09") :
            if phone.isnumeric() and len(phone) == 11 :
                if account.isnumeric()and len(account) >= 6 :
                    return True
                else:
                    print("invalid account")
                    return False
            else:
                print("invalid phone (11 digits, 09...)")
                return False
        else:
            print("invalid name")
            return False
        
    @staticmethod
    def is_menu(value):
        return value in {"1", "2", "3", "4", "5", "6", "7", "8"}
        
    @staticmethod
    def is_positive_amount(value):
        return value.isdigit() and int(value) > 0

    @staticmethod
    def is_valid_pin(value):
        return value.isdigit() and len(value) == 4
    
class Io:
    @staticmethod
    def get_information(validator):
        while True:
            name = input("enter your name: ").strip().lower()
            phone = input("Enter your phone (11 digits, starting with 09): ").strip()
            account = input("Enter your account number (at least 6 digits): ").strip()
            
            if validator.check_information(name, phone, account):
                return name, phone, account
            print("Please enter your information again.\n")
               
    @staticmethod 
    def get_option_menu(validator):
        while True:
            option = input("Select an option (1-8): ").strip()
            
            if validator.is_menu(option):
                return option
            print("Invalid option. Choose a number from 1 to 8.")
            
    @staticmethod
    def get_amount(validator):
        while True:
            amount = input("enter amount: ").strip()
            
            if validator.is_positive_amount(amount):
                return int(amount)
            print("Invalid amount. Enter a positive whole number.")
    
    @staticmethod
    def get_pin(validator, prompt="enter PIN"):
        while True:
            pin = input(prompt).strip()
            
            if validator.is_valid_pin(pin):
                return pin
            print("Invalid PIN. It must contain exactly 4 digits.")

    @staticmethod
    def get_account(validator):
        while True:
            account = input("Enter recipient account number: ").strip()
            
            if account.isdigit() and len(account) >= 6:
                return account
            print("Invalid account number. Enter at least 6 digits.")
    
class BankAccount:
    def __init__(self, account_number, balance=10000, pin=1234):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin
        self.transactions = []
        
    def _record_transaction(self, transaction_type, amount, details=""):
        entry = f"{transaction_type}: {amount}"
        if details:
            entry += f" ({details})"
        self.transactions.append(entry)
        
    def check_balance(self):
        print(f"\nyour balance is ${self.balance} ")  
        
    def transfer(self, validator):
        recipient = Io.get_account(validator)
        if recipient == self.account_number:
            print("You cannot transfer money to your own account.")
            return

        amount = Io.get_amount(validator)
        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        self._record_transaction("Transfer", amount, f"to account {recipient}")
        print("\nTransfer successful!")
        print(f"Your new balance is: ${self.balance}")
        
    
    def deposit(self, validator):
        amount = Io.get_amount(validator)
        self.balance += amount
        self._record_transaction("Deposit", amount)
        print("\ndeposit successful!")
        print(f"your new balance is: ${self.balance}")
    
    def withdraw(self, validator):
        amount = Io.get_amount(validator)
        if amount > self.balance:
            print("Insufficient balance.")
            return
        
        self.balance -= amount
        self._record_transaction("Withdrawal", amount)
        print("\nwithdraw successful!")
        print(f"your new balance is: {self.balance}$")
    
    def transaction_history(self):
        if not self.transactions:
            print("\nno transactions found")
            
        print("\n==== Transaction History ====")
        for index, transaction in enumerate(self.transactions, start=1):
            print(f"{index}. {transaction}")
    
    def change_pin(self, validator):
        print("\n====change pin====")
        current_pin = Io.get_pin(validator, "Enter current PIN (4 digits): ")
        
        if current_pin != self.pin:
            print("Incorrect PIN.")
            return
    
        new_pin = Io.get_pin(validator, "Enter new PIN (4 digits): ")
        if new_pin == self.pin:
            print("Your new PIN must be different from your current PIN.")
            return

        self.pin = new_pin
        print("PIN changed successfully.")
    
class Application:
    def run(self):
        menus = Menus()
        validator = Validator()
        
        print("==== Welcome to MyBank ====")
        name, phone, account_number = Io.get_information(validator)
        user = menus.user_info(name, phone, account_number)
        bank = BankAccount(account_number=account_number)
        
        while True:
            print("\n==== Main Menu ====")
            for key , value in menus.main_menu().items():
                    print(f"{key}. {value}")
            option = Io.get_option_menu(validator)
            
            if option == "1":
                bank.check_balance()
            elif option == "2" :
                bank.transfer(validator)
            elif option == "3" :
                bank.deposit(validator)
            elif option == "4" :
                bank.withdraw(validator)
            elif option == "5" :
                bank.transaction_history()
            elif option == "6" :
                print("\n===== User Information =====")
                for key, value in user.items():
                    print(f"{key.title()}: {value}")
            elif option == "7" :
                bank.change_pin(validator)
            elif option == "8":
                print("Goodbye!")
                break
        
if __name__ == "__main__":
    app = Application()
    app.run()
    