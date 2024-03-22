"""(The Account class) Design a class named Account that contains:
■ A private int data field named id for the account.
■ A private float data field named balance for the account.
■ A private float data field named annualInterestRate that stores the current
interest rate.
■ A constructor that creates an account with the specified id (default 0), initial
balance (default 100), and annual interest rate (default 0).
■ The accessor and mutator methods for id, balance, and annualInterestRate.
■ A method named getMonthlyInterestRate() that returns the monthly
interest rate.
■ A method named getMonthlyInterest() that returns the monthly interest.
■ A method named withdraw that withdraws a specified amount from the
account.
■ A method named deposit that deposits a specified amount to the account.
Draw the UML diagram for the class, and then implement the class. (Hint: The
method getMonthlyInterest() is to return the monthly interest amount, not
the interest rate. Use this formula to calculate the monthly interest: balance *
monthlyInterestRate. monthlyInterestRate is annualInterestRate
/ 12. Note that annualInterestRate is a percent (like 4.5%). You need to
divide it by 100.)
"""


class Account:
    def __init__(self, a_id=0, balance=100, annualInterestRate=0):
        self.__a_id = a_id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
        self.__monthlyInterestRate = annualInterestRate / 12

    # Returns the id
    def get_id(self):
        return self.__a_id

    # Sets the id
    def set_id(self, a):
        if a >= 0:
            self.__a_id = a

    # Returns the balance
    def get_balance(self):
        return self.__balance

    # Sets the balance
    def set_balance(self, a):
        if a >= 0:
            self.__balance = a

    # returns the annual interest rate
    def get_annualInterestRate(self):
        return self._annualInterestRate

    # sets the annual interest rate
    def set_annualInterestRate(self, a):
        if a >= 0:
            self.__annualInterestRate = a

    # returns the monthly interest in value
    def getMonthllyInterest(self):
        return self.__balance * self.__monthlyInterestRate / 100

    # method responsible for a withdrawl
    def withdraw(self, n):
        if abs(n) <= self.__balance:
            self.__balance -= abs(n)
        ##               return True
        else:
            return True

    # method responsible for a deposit
    def deposit(self, n):
        if n >= 0:
            self.__balance += n
        ##               return True
        else:
            return True


a = Account()
a.withdraw(110)
##a.set_id(90)
##a.set_balance(20000)
##print(a.get_id())
##print(a.get_balance())
