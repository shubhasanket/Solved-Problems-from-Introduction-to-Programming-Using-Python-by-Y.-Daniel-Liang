"""16.18 (Largest block) The problem for finding a largest block
is described in Exercise 11.47. Design an algorithm for solving
this problem and analyze its complexity. Can you design an O(n2)
algorithm for this problem?
"""

##Made a few changes. In __init__ made the variables in self.cells IntVars instead of StringVar
##In refresh, creating another plain numeric array self.t (size by size) whose top row and left column
##is the same as the values in self.cells and the rest of the elements are 0.
##In find - we go through all the elements of the self.t array (except the top row  and left column).
##     maximum = 0 
##     if the corresponding element in self.cells is zero do not change
##     if the corresponding element in self.cells is one then
##     
##          self.t[i][j] = 1 + minimum(the values of the cell on the left,the cell on the left and above,
##                                     and the cell just above)
##          if this new value of self.t[i][j] is bigger than any other value we remember it
##          make maximum equal to that and make max_i = i and max_j = j
##     When we have gone through the size of the biggest block is maximum, and max_i and max_j
##     are the coordinates of the right and bottom most cell of the biggest block
##
##     Take a small example and see why this might work
##
##When we randomly generate numbers - often the blocks are just 2 by 2.
##To create deliberately bigger blocks, make DEBUG True and in refresh
##see the changes made!
##
##Check if the program still works and if it is a little better.

'''(Tkinter: largest block) Write a program that displays a 10X10 square matrix, as
shown in Figure 11.17b. Each element in the matrix is a 0 or 1, randomly generated
with a click of the Refresh button. Display each number centered in a text box.
Allow the user to change the entry value. Click the Find Largest Block button to find
a largest square submatrix that consists of 1s. Highlight the numbers in the block,
'''

from tkinter import *
from random import *

DEBUG = not True   #if True we create in refresh method our own block to check our routines

##SIZE = 10
class Find_Largest_Block:
     
     def __init__(self, SIZE = 10):

          self.size = SIZE
          self.window = Tk() # Create a window
          self.window.title("Find Largest Block") # Set title
        
          self.frame = Frame(self.window) # Hold entries 
          self.frame.pack()
        
          self.cells = [] # A list of variables tied to entries
          for i in range(self.size):
              self.cells.append([])
              for j in range(self.size):
                  self.cells[i].append(IntVar())   ####

          self.entries = [] # A list of all the Entry boxes, required to change its characteristics later in the program
          for i in range(self.size): 
              self.entries.append([])
            
              for j in range(self.size):
                  e = Entry(self.frame, width = 2, justify = RIGHT, 
                      textvariable = self.cells[i][j], font = ('Verdana', 10), disabledbackground = 'light grey')
                        
                  e.grid(row = i, column = j)

                  self.entries[i].append(e) #Adding the entries to the list
               
               
          self.frame1 = Frame(self.window) #Create a frame 
          self.frame1.pack()
        
          bt_solve = Button(self.frame1, text = "Refresh", font = ('Verdana', 15), # Button to execute the refresh routine
                          command = self.refresh)
          bt_solve.pack(side = LEFT)

          bt_clear = Button(self.frame1, text = "Find Largest Block", font = ('Verdana', 15), # Button to execute the find routine
                            command = self.find) 
          bt_clear.pack(side = LEFT)

          self.refresh()
          self.window.mainloop() # Create an event loop


     def refresh(self):
          # Setting random values of 0 and 1 to the cells
          
          #We also create another two dimensional array (size x size) self.t
          #whose first row is same as the array in self.cells
          #and rest of the rows are filled with 0
          
          self.refresh_grid()
          self.t = []
          for i in range (self.size):
               row = []
               for j in range(self.size):
                    n = randint(0,1)
                    self.cells[i][j].set(n)
                    if i == 0 or j == 0:   #Top row or left column same as self.cells[i][j]
                         row.append(n)
                    else:
                         row.append(0)      #other cells 0
               self.t.append(row)

          if DEBUG:
               #Deliberately create a block of size m whose top left and top corner is at top, left
               #Make sure your values of m, top, left are valid
               m = 6
               top = left = 4
               for i in range(top, top + m):
                    for j in range(left, left + m):
                         self.cells[i][j].set(1)
                         self.t[i][j] = 1
                    

     def find(self):
          '''
          We come here after having run the refresh method. This method creates another 2 dimensional
          array self.t - whose top row and the leftmost column is the same as the displayed array
          and whose other cells are 0.
          The following routine will look at rows (except the top row) and columns (except the left most col)
          of the original array and set the values of the cells in self.t
          
          '''
          maximum = 0
          for i in range(1,self.size):  #do not look at the top row
               for j in range(1, self.size):  #do not look at the leftmost column
                    if self.cells[i][j].get() == 1:
                         #m = 1 + minimum of cell to the left, cell to the left and above, cell above
                         m = 1 + min( self.t[i][j-1],self.t[i-1][j-1],self.t[i-1][j] )
                         self.t[i][j] = m
                         if m > maximum:
                              maximum = m
                              max_i = i
                              max_j = j
          if maximum <= 1:
               print("No matrix of size 2 or above found")
               print("Put this message in a Message Box if you want")
          else:
               for i in range(max_i - maximum +1, max_i+1):
                    for j in range(max_j - maximum + 1, max_j+1):
                         self.entries[i][j]['state'] = "disabled"


     def refresh_grid(self):
          
          for u in self.entries:
               for v in u:
                    v['state'] = 'normal' 
          
     
          
Find_Largest_Block(35)
          
'''
     def findOld(self):
          # This routine will only look for square submatrices with rows and columns >= 2
          l = [[0,0,1]] # To store the top left corners of the biggest submatrices and their size

          for i in range (self.size):
               for j in range (self.size):

                         if int(self.cells[i][j].get()) == 1:
                              end_loop = False
                              x = 1

                              while not end_loop:
                                   if (j + x) < self.size  and (i + x) < self.size: # Check if the indexes are not crossing the boundaries
                                        if int(self.cells[i][j+x].get()) == 1: # and that the following number on the same row is 1
                                             check = True                                                        
                                             
                                             for k in range (x+1):
                                                  if int(self.cells[i+k][j+x].get()) != 1 or int(self.cells[i+x][j+k].get()) != 1:
                                                       check = False # The sub matrix of size x is not made up of only 1s

                                             if check: # We have found a submatrix of size x
                                                  if l[0][2] < x + 1: # This means we have found a greater submatrix than before
                                                       l = []
                                                       l.append([i,j,x+1])

                                                  elif l[0][2] == x + 1: # This means we have found a submatrix of the same size as found before
                                                       l.append([i,j,x+1])

                                                  x += 1 # Increment x and check for the next value
                                                  
                                             else: # End the loop
                                                  end_loop = True                                                  
                                        
                                        else: # End the loop
                                             end_loop = True

                                   else: # End the loop
                                        end_loop = True
                        
          self.update_grid(l)
          print(l)


          
     def update_grid(self,l): # Displaying the largest box (the first in the list)

          for i in range (l[0][2]):
               for j in range (l[0][2]):
                    self.entries[l[0][0] + i][l[0][1] + j]['state'] = "disabled"
'''
