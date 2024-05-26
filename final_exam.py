from datetime import datetime
class Account:
    def __init__(self, account_number, name, email, address, account_type):
        self.account_number = account_number
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []
        self.loan_taken = False
        self.loan_amount = 0
        self.num_loans_taken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append((datetime.now(), "Deposit", amount))

    def withdraw(self, amount):
        if bank.bankrupt:
            print("The bank is bankrupt.")
        elif amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= amount
            self.transaction_history.append((datetime.now(), "Withdrawal", amount))
            print("Withdrawal successful.")

    def check_balance(self):
        print(f"Available balance: {self.balance}")

    def check_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(f"Date: {transaction[0]}, Type: {transaction[1]}, Amount: {transaction[2]}")

    def take_loan(self, amount):
        if not bank.loan_status:
            print("Loan feature is currently turned off.")
            return
        if amount > 2 * self.balance:
            print("Cannot take a loan.")
        elif self.num_loans_taken >= 2:  
            print("You have already taken two time loans")
        else:
            self.loan_taken = True
            self.balance += amount
            self.loan_amount += amount 
            self.transaction_history.append((datetime.now(), "Loan", amount))
            self.num_loans_taken += 1  
            print("Loan taken successfully.")
            self.check_balance()
  
    def transfer(self, recipient_account, amount):
        if bank.bankrupt:
            print("The bank is bankrupt.")
        if amount > self.balance:
            print("Insufficient balance.")
        elif recipient_account is None:
            print("Transfer cannot be completed.")
        else:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append((datetime.now(), f"Transfer to {recipient_account.name}", amount))
            recipient_account.transaction_history.append((datetime.now(), f"Transfer from {self.name}", amount))
            print(f"Transfer of {amount} to {recipient_account.name} successful.")
            self.check_balance()  
            recipient_account.check_balance()  

class Bank:
    def __init__(self):
        self.total_balance_amount = 0
        self.total_loan = 0
        self.loan_status = True
        self.accounts = []
        self.bankrupt = False

    def create_account(self,account_number, name, email, address, account_type):
        account = Account(account_number,name, email, address, account_type)
        self.accounts.append(account)

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} deleted successfully.")
                return
        print("Account not found.")

    def show_users(self):
        print("User Accounts:")
        for account in self.accounts:
            print(f"Name: {account.name}, Account Number: {account.account_number}")

    def get_total_balance(self):
        self.total_balance_amount = sum(account.balance for account in self.accounts)
        print(f"Total Balance: {self.total_balance_amount}")

    def get_total_loan(self):
        self.total_loan = sum(account.loan_amount for account in self.accounts)
        print(f"Total Loan: {self.total_loan}")

    def off_loan(self):
        self.loan_status = False
        print("Loan turned off.")

    def on_loan(self):
        self.loan_status = True
        print("Loanturned on.")

    def set_bankrupt(self, value):
        self.bankrupt = value
        if value:
            print("Bankrupt turned ON.")
        else:
            print("Bankrupt turned OFF.")

bank = Bank()

while True:
    print("\nWelcome to the Bank Management System:")
    print("1) Admin")
    print("2) User")
    print("3) Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAdmin Options:")
        print("1) Create Account")
        print("2) Delete Account")
        print("3) Show User Accounts")
        print("4) Check Total Balance")
        print("5) Check Total Loan")
        print("6) Turn On/Off Loan Feature")
        print("7) Set bankrupt mode")
        
        admin_choice = input("Enter your choice: ")
        
        if admin_choice == "1":
            account_number = int(input("Enter account number: "))
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account(account_number, name, email, address, account_type)
        elif admin_choice == "2":
            account_number = int(input("Enter account number to delete: "))
            bank.delete_account(account_number)
        elif admin_choice == "3":
            bank.show_users()
        elif admin_choice == "4":
            bank.get_total_balance()
        elif admin_choice == "5":
            bank.get_total_loan()
        elif admin_choice == "6":
            print("1) Turn On Loan Feature")
            print("2) Turn Off Loan Feature")
            loan_choice = input("Enter your choice: ")
            if loan_choice == "1":
                bank.on_loan()
            elif loan_choice == "2":
                bank.off_loan()
            else:
                print("Invalid choice.")

        elif admin_choice == '7':
            bankrupt_input = input("Set bankrupt mode (yes/no): ").lower()
            if bankrupt_input == "yes":
                bank.set_bankrupt(True)
            elif bankrupt_input == "no":
                bank.set_bankrupt(False)
            else:
                print("Invalid input.")
        else:
            print("Invalid choice.")

    elif choice == "2":
        print("\nUser Options:")
        print("1) Create Account")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Check Balance")
        print("5) Check Transaction History")
        print("6) Take Loan")
        print("7) Transfer Money")
        
        user_choice = input("Enter your choice: ")
        
        if user_choice == "1":
            account_number = int(input("Enter account number: "))
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account(account_number,name, email, address, account_type)

        elif user_choice == "2":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter amount to deposit: "))
            for account in bank.accounts:
                if account.account_number == account_number:
                    account.deposit(amount)
                    break
            else:
                print("Account not found.")

        elif user_choice == "3":
            if bank.bankrupt:
                print('The Bank is Bankrupt')
            elif bank.bankrupt is False:
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter amount to withdraw: "))
                found_account = False
                for account in bank.accounts:
                    if account.account_number == account_number:
                        found_account = True
                        account.withdraw(amount)
                        break
                if not found_account:
                    print("Account not found.")


        elif user_choice == "4":
            account_number = int(input("Enter your account number: "))
            for account in bank.accounts:
                if account.account_number == account_number:
                    account.check_balance()
                    break
            else:
                print("Account not found.")

        elif user_choice == "5":
            account_number = int(input("Enter your account number: "))
            for account in bank.accounts:
                if account.account_number == account_number:
                    account.check_transaction_history()
                    break
            else:
                print("Account not found.")

        elif user_choice == "6":
            if bank.bankrupt:
                print('The Bank is Bankrupt')
            elif bank.bankrupt is False:
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter loan amount: "))
                for account in bank.accounts:
                    if account.account_number == account_number:
                        account.take_loan(amount)
                        break
                else:
                    print("Account not found.")

        elif user_choice == "7":
            if bank.bankrupt:
                print('The Bank is Bankrupt')
            elif bank.bankrupt is False:
                account_number = int(input("Enter your account number: "))
                recipient_account_number = int(input("Enter recipient account number: "))
                amount = float(input("Enter amount to transfer: "))
                sender_account = None
                recipient_account = None
                for account in bank.accounts:
                    if account.account_number == account_number:
                        sender_account = account
                    elif account.account_number == recipient_account_number:
                        recipient_account = account
                if sender_account is not None and recipient_account is not None:
                    sender_account.transfer(recipient_account, amount)
                else:
                    print("Account does not exist")
        else:
            print("Invalid choice.")

    elif choice == "3":
        print("Thank you for using the Bank Management System.")
        break
    else:
        print("Invalid choice.")