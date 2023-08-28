import pyfiglet

text = "Amine0x0 Bank"
font = "big"
green = "\033[92m"
cyan = "\033[36m"
red = "\033[31m"
reset = "\033[0m"

ascii_art = pyfiglet.figlet_format(text, font=font)
print(green + ascii_art + reset)

class Menu:
    def exit_program(self):
        print(red + "Exiting Program ...\n" + reset)
        exit()

    def program_start(self, name, balance):
        print(cyan + f"Hello {name}! \n" + reset)
        while True:
            user_choice = input(green + "1) Withdraw / 2) Deposit / 3) Check Balance / 4) Exit: " + reset)
            if user_choice == "1":
                balance = self.withdraw(name, balance)
            elif user_choice == "2":
                balance = self.deposit(name, balance)
            elif user_choice == "3":
                self.check_balance(name, balance)
            elif user_choice == "4":
                self.exit_program()
            else:
                print(red + "Invalid choice. Please choose a valid option.\n" + reset)

    def withdraw(self, name, balance):
        print("You're now in Withdraw menu... \n")
        user_amnt = int(input(cyan + "Enter the amount you want to withdraw: " + reset))
        if user_amnt > 0 and user_amnt <= balance:
            balance -= user_amnt
            print(green + f"Withdrawal successful. You now have {balance} $\n" + reset)
        else:
            print(red + "Invalid amount or insufficient balance.\n" + reset)
        return balance

    def deposit(self, name, balance):
        print("You're now in Deposit menu... \n")
        user_amnt = int(input(cyan + "Enter the amount you want to deposit: " + reset))
        if user_amnt > 0:
            balance += user_amnt
            print(green + f"Deposit successful. You now have {balance} $\n" + reset)
        else:
            print(red + "Invalid amount.\n" + reset)
        return balance

    def check_balance(self, name, balance):
        print(f"Hello {name}, your current balance is {balance} $\n")

class Program:
    def start(self):
        username = input(cyan + "Enter your username: " + reset)
        balance = 200
        menu = Menu()
        menu.program_start(username, balance)

# main
start = Program()
start.start()
