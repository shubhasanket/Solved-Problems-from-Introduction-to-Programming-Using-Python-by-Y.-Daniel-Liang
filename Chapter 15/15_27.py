##from tkinter import *

SIZE = 8
class EightQueens:
    def __init__(self):
        self.queens = SIZE *[-1]
        self.all = []
        for column in range (SIZE):# for all possible places in the first row
            self.queens[0] = column
            self.search(0,column)
##        print(len(self.all))
##        print(self.all)

        for i in range (len(self.all)):#Print the board
            print(i+1)
            self.print_board(self.all[i])
            
##        print(self.queens)

    def search(self, row, column):
        if row == SIZE:# and self.queens not in self.all:
            # A solution has been found
            l = [] + self.queens
            if l not in self.all:
                self.all.append(l)
        
        elif self.isValid(row, column):
##            print(row, column)
            for i in range (SIZE):
                if row < SIZE-1:
##                    print(self.queens)
##                    print(row)
                    self.queens[row+1] = i
                self.search(row+1, i)

    def isValid(self, row, column):# Checking if the placement is valid
        for i in range (1, row+1):
            if (self.queens[row-i] == column
                or self.queens[row-i] == column-i
                or self.queens[row-i] == column+i):
                return False
        return True


    def print_board(self,l):  ## Print the board
         
         for i in range(SIZE):
              for j in range(SIZE):
                   if j == l[i]:
                        print('|Q|', end = '')
                   else:
                        print('| |', end = '')
              print("")
         print("......................................")

EightQueens()
