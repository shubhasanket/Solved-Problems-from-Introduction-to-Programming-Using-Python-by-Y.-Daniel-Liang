''' Kngiht's tour problem. We get to choose the starting point.
'''
import sys
import time

SIZE = 8


def solve(start_x = 3, start_y = 3):
     # Create a grid
     grid = create_grid()
     
     # All the possible moves of the knight from a given point on the grid of any size
     move_x = [1,-1,2,-2,2,-2,1,-1]
     move_y = [-2,-2,-1,-1,1,1,2,2]

     #Variables to store the knight's current position
     pos_x = start_x
     pos_y = start_y

     # The number of succesful moves
     n = 1

     #Update the grid with the knight's startuing position
     grid[pos_x][pos_y] = n

     # list to retain the indexes of the move_x and move_y lists that were used to confirm a spot on the grid
     l = [0]*(SIZE**2)
     # Lists to store the knight's previous positions
     last_x = [0]*(SIZE**2)
     last_y = [0]*(SIZE**2)

     t = time.time()
     
##     l[n] = 0 # We determine the first positiona

     ## Execute the following loop as long as the knight has not completed a succesful tour
     while n != SIZE**2:
          ch = False
          
          for i in range (l[n], len(move_x)):
##               print("n = ", n)
               if not ch:
                    if check(pos_x + move_x[i], pos_y + move_y[i], grid): # if the porposed move is valid
                         last_x[n] = pos_x
                         last_y[n] = pos_y
                         l[n] = i + 1 # This data will be used when we backtrack
                         pos_x += move_x[i] # Update the position of the Knight
                         pos_y += move_y[i]
                         n += 1
                         grid[pos_x][pos_y] = n
                         ch = True
                         #break
##                         print(ch)
                         #sys.exit()

          if not ch:
               grid[pos_x][pos_y] = 0
##               print("...",n)
               l[n] = 0 # reset the index value to 0
               n -= 1
               pos_x = last_x[n]
               pos_y = last_y[n]

               
##          print("l[n]", l)
          if n < 1:
               print("No solution Found")
               sys.exit()

          if time.time() - t > 15:
               t = time.time()
               print_grid(grid)
               print()
               print()
               
     print_grid(grid)
     print("Done")
# Create the empty grid

def create_grid():

##     l = [[-1]*8]*8
##     return l

     l = []
     for i in range (SIZE):
          l.append([])
          for j in range (SIZE):
               l[i].append(0)
     return l
                    
def print_grid(l):
     for i in range (len(l)):
          for j in range (len(l[i])):
               print(l[i][j], end = " ")
          print()
                          

def check(x, y, grid):
##     print(x,y)
     if x >= 0 and y >= 0 and x < SIZE and y < SIZE:
          if grid[x][y] == 0:
               return True
     return False


solve()
