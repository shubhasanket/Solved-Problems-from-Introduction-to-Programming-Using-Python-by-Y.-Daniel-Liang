'''(Game: Connect Four) Connect Four is a two-player board game in which the
players alternately drop colored disks into a seven-column, six-row vertically
suspended grid, as shown at cs.armstrong.edu/liang/ConnectFour/ConnectFour.html.
The objective of the game is to connect four same-colored disks in a row, column,
or diagonal before your opponent does. The program prompts two players
to drop a red or yellow disk alternately. Whenever a disk is dropped, the program
redisplays the board on the console and determines the status of the game
(win, draw, or continue).
'''
import sys
## The rows in the list, are the columns in the display. E.g row 1 in list becomes column 1 in grid

DEBUG = not True

class Connect_Four:
     def __init__(self, column = 7, row = 6,  connect = 4):
          self.row = column ## size of the grid
          self.col = row
          self.c = connect ## Number of occurences 
          self.grid = [] ## list for the grid
          self.player = True ## Player True is red and palyer False is yellow 

          ## Creating the plane grid
          for i in range (self.row):
               self.grid.append([-1]*self.col)

          if DEBUG:
               for i in range (self.row):
                    print(self.grid[i])

          self.printGrid()
          self.prompt()

     ## This routine reads and checks boundaries of the input
     def prompt(self):
          local_check = False

          while not local_check:

               ## Reading the value
               if self.player: ## Player red == True
                    x = eval(input("Drop a red disk at column (0-" + str(self.row - 1) +"): "))

               else: ## Player yellow == False
                    x = eval(input("Drop a yellow disk at column (0-" + str(self.row - 1) +"): "))

               ## Checking the value's limits
               if not 0 <= x <= self.row:
                    print("Input is beyond the range")

               ## Checking if the column is full
               elif -1 not in self.grid[x]: 
                    print("Column", str(x), "is full. Try another column")

               else: ## Else break the loop
                    local_check = True

          i = self.grid[x].index(-1) ## To locate the first -1 occurence
          
          if self.player:  ## Player True - red
               self.grid[x][i] = "R"
          else: ## Player False - yellow
               self.grid[x][i] = "Y"

          self.player = not self.player # Switching the players

          self.printGrid()

     def printGrid(self): ## When I am printing, the grid undergoes a rotation of 90 degrees to the left. Rows become columns and columns become rows.
                          ## All the other routines stick to the original grid.
          for j in range (self.col - 1, -1, -1):
               for k in range (self.row):
                    if self.grid[k][j] == -1:
                         print("| |", end = "")
                    else:
                         print("|" + str(self.grid[k][j]) + "|", end = "")
               print("")


          self.check()


     def check(self):
          ## Variables which will be used to know if there has been a match
          global_row_check = False
          global_column_check = False
          global_dia_check = False

          ## Row check
          
          for i in range (self.row):
               
               j = 0
               while j + (self.c - 1) < self.row and global_row_check == False: ## Ensuring the maximun limit is respected
                    local_row_check = True
                    
                    for k in range(1, self.c):
                         
                         if DEBUG:
                              print("i = " + str(i) +" j = " + str(j) + " k = " + str(k))
                              
                         if self.grid[i][j] == -1 or self.grid[i][j] != self.grid[i][j+k]: ## Checking for the indexes, j to j + 3
                              local_row_check = False
                              break ## If at any point it does not match, come out from  (for k in range(1, self.c)) loop
                         
                    if local_row_check :
                         self.winner = self.grid[i][j] ## to know the winner
                         global_row_check = True
                         if DEBUG:
                              print("True")
                         
                    j += 1 ## Increase j and restart the process

               if DEBUG:
                    print(global_row_check)

          
                    
          ## Column check

          for l in range (self.col):

               m = 0
               while m + (self.c - 1) < self.col and global_column_check == False: ## Ensuring the maximun limit is respected
                    local_column_check = True
                    
                    for n in range(1, self.c):
                         
                         if DEBUG:
                              print("l = " + str(l) +" m = " + str(m) + " n = " + str(n))
                              
                         if self.grid[m][l] == -1 or self.grid[m][l] != self.grid[m+n][l]: ## Checking for the coumn indexes, n to n + 3
                              local_column_check = False
                              break ## If at any point it does not match, come out from  (for n in range(1, self.c)) loop
                         
                    if local_column_check :
                         self.winner = self.grid[m][l] ## to know the winner
                         global_column_check = True
                         if DEBUG:
                              print("True")
                         
                    m += 1 ## Increase m and restart the process

          
##          for i in range (self.l):
##
##               ## Row and Column Check
##               
##               j = 0
##               while j + (self.c - 1) < self.l and global_row_check == False: ## Ensuring the maximun limit is respected
##                    local_row_check = True
##                    local_column_check = True
##
##                    for k in range(1, self.c):
##                         if DEBUG:
##                              print("i = " + str(i) + " j = " + str(j) + " k = " + str(k))
##                              
##                         if self.grid[i][j] == -1 or self.grid[i][j] != self.grid[i][j+k]: ## Checking for the indexes, j to j + 3
##                              local_row_check = False
####                              break ## If at any point it does not match, come out from  (for k in range(1, self.c)) loop
##
##                         if self.grid[j][i] == -1 or self.grid[j][i] != self.grid[j+k][i]: ## Checking for the coumn indexes, n to n + 3
##                              local_column_check = False
####                              break ## If at any point it does not match, come out from  (for k in range(1, self.c)) loop
##                         
##                    if local_row_check :
##                         self.winner = self.grid[i][j] ## to know the winner
##                         global_row_check = True
##
##                    elif local_column_check :
##                         self.winner = self.grid[j][i] ## to know the winner
##                         global_column_check = True
##                         
##                         
##                    j += 1 ## Increase the value of j by 1

                    
          ## Diagonal Check

##          dl = []
##
##          ## This routine makes lists of  all the diagonally placed elements in the grid
##
##          for a in range (self.col):
##               l1 = []
##               l2 = []
##
##               if a < (self.l - 1):
##                    
##                    for b in range (a+1):
##                         l1.append(self.grid[a-b][b])       ## I reasoned these out. The explanation is long
##                         l2.append(self.grid[self.l - b][self.l + (a-b)]) ## Same as above
##
##               else:
##                    for b in range (a+1):
##                         l1.append(self.grid[a-b][b])
##
##               dl.append(l1)
##               dl.append(l2)     
##                              
##          if global_column_check or global_row_check:
##               print(self.winner, "is the winner")
##
##          self.prompt()    
##                         
##          


     ## Create a list dl of all the diagonals of the grid

          dl = []

          for k in range (self.row):
               i = k
               j = 0
               l1 = []
               l2 = []
               
               while 0 <= i < self.row and 0 <= j < self.col:
                    
                    l1.append(self.grid[i][j])
                    l2.append(self.grid[i][self.col - 1 - j])

                    i -= 1
                    j += 1

               dl.append(l1)
               dl.append(l2)

          for k in range (self.col - 1, 0, -1):
               i = self.col - 1
               j = k
               l1 = []
               l2 = []
               
               while 0 <= i < self.col and 0 <= j < self.col:
                    
                    l1.append(self.grid[i][j])
                    l2.append(self.grid[i][self.col - 1 - j])

                    i -= 1
                    j += 1

               dl.append(l1)
               dl.append(l2)

     ## Check for 4 consecutive occurences

##          if DEBUG:

##          for i in range(len(dl)):
##               for j in range(len(dl[i])):
##                    print(dl[i][j], end = " ")
##               print()


          for u in range (len(dl) - 1):
               if len(dl[u]) >= 4:
                    
##                    for i in range(len(dl[u])):
##                         print(dl[u][i], end = " ")
##                    print()

                    v = 0
                    while v + (self.c - 1) < len(dl[u]) and global_dia_check == False:
                         local_dia_check = True

                         for n in range(1, self.c):
                              
                              if DEBUG:
                                   print("len of dl", len(dl[u]), "v =", v, "n =", n)
                              
                              
                              if dl[u][v] == -1 or dl[u][v] != dl[u][v+n]: ## Checking for the indexes, n to n + 3
                                   local_dia_check = False
                                   break ## If at any point it does not match, come out from  (for n in range(1, self.c)) loop
                              
                         if local_dia_check :
                              self.winner = dl[u][v] ## to know the winner
                              global_dia_check = True

                              if DEBUG:
                                   print("True dia")
                         
                         v += 1

          #self.prompt()

          self.endGame(global_row_check, global_column_check, global_dia_check)      

     ## Routine responsible to check if the game ends or continues
     def endGame(self,x,y,z): 
##          print("check")

          endgame = False
          draw = False

          if x or y or z:  ## Checking if there is a winner
                print("The winner is " + self.winner)
                endgame = True
                sys.exit() #If there is a winner, leave the game
                

          if not endgame: ## Checking if it is a draw
               check = False
               for i in range(self.row):
                    if -1 == self.grid[i][self.col - 1]:
                         check = True

               if not check:
                    print("It is a draw")
                    draw = True
                    sys.exit()
                    
          if not draw:## Continue the game
               self.prompt()
                    
                                        
          

Connect_Four()
##Connect_Four(20, 15, 10)
