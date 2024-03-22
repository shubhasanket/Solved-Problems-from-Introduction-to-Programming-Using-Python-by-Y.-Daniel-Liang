"""Game: ATM machine) Use the Account class created in Exercise 7.3 to simulate
an ATM machine. Create ten accounts in a list with the ids 0, 1, ..., 9, and an initial
balance of $100. The system prompts the user to enter an id. If the id is entered
incorrectly, ask the user to enter a correct id. Once an id is accepted, the main
menu is displayed as shown in the sample run. You can enter a choice of 1 for
viewing the current balance, 2 for withdrawing money, 3 for depositing money,
and 4 for exiting the main menu. Once you exit, the system will prompt for an id
again. So, once the system starts, it won’t stop.
"""

from class_account import Account


class Atm(Account):
    def __init__(self, total_ids=10):
        Account.__init__(self)
        self.__l = []  # create a list to store the instances of the Account class
        self.total_ids = total_ids
        for i in range(self.total_ids):  # append 10 Accounts to the list
            self.__l.append(Account(a_id=i))
        self.__main()  # invoke main()

    def __main(self):
        check1 = True  # bool value for the while loop
        while check1:
            n = eval(input("Enter an account id: "))
            if 0 <= n < self.total_ids:  # If the id is valid
                print()
                self.__submain(n)  # invoke submain()
            else:
                print("Id does not exist")  # else print this

    def __submain(self, n):
        check2 = True  # bool value for the while loop
        while check2:
            print("Main menu")
            print("1: check balance")
            print("2: withdraw")
            print("3: deposit")
            print("4: exit")

            x = (
                -1
            )  # assigning -1 to ensure that the loop continues till we have a valid x
            while x < 0 or x > 4:
                x = eval(input("Enter a choice: "))

                if x < 0 or x > 4:
                    print("Enter a valid choice!")

            if x == 1:  # case 1: print the balance of the account
                print("The balance is", self.__l[n].get_balance())

            elif x == 2:  # casw 2: withdraw an amount
                v = eval(input("Enter an amount to withdraw: "))
                c = self.__l[n].withdraw(v)
                if c:
                    print("Withdrawal unsuccesful")

            elif x == 3:  # case 3: deposit an amount
                v = eval(input("Enter an amount to deposit: "))
                c = self.__l[n].deposit(v)
                if c:
                    print("Deposit unsuccesful")

            else:  # case 4: change the bool value of check2 to break the loop and return the handl to main()
                check2 = False

            print()


Atm()
