''' Kngiht's tour problem will with all the possible starting positions using Warnsdorff's method.
'''
import sys
import time

SIZE = 8


def solve(n, start_x = 3, start_y = 3):
     # Create a grid
     grid = create_grid()
     
     # All the possible moves of the knight from a given point on the grid of any size
     move_x = [1,2,2,1,-1,-2,-2,-1]
     move_y = [-2,-1,1,2,2,1,-1,-2]

     if n == 38: # For n == 28, the move_x and move_y lists stated above do not produce a solution. So we check the possibilities in the reverse order.
          move_x.reverse()
          move_y.reverse()

     moves_grid = create_grid_for_moves(move_x, move_y)

     #Variables to store the knight's current position
     pos_x = start_x
     pos_y = start_y

     # The number of succesful moves
     n = 1

     #Update the grid with the knight's startuing position
     grid[pos_x][pos_y] = n

     moves_grid = update_grid_for_moves(pos_x, pos_y, moves_grid, move_x, move_y) # update moves_grid

     ## Execute the following loop as long as the knight has not completed a succesful tour
     while n != SIZE**2:
          l = [len(move_x) + 1,0] # to store the move that has the least possible moves 
          for i in range (len(move_x)): 
               if check(pos_x + move_x[i], pos_y + move_y[i], grid): # if the porposed move is valid
                    a = moves_grid[pos_x + move_x[i]][pos_y + move_y[i]]
                    if a > -1 and a < l[0]:
                        l = [moves_grid[pos_x + move_x[i]][pos_y + move_y[i]], i]

          pos_x += move_x[l[1]] # Update the position of the Knight
          pos_y += move_y[l[1]]         
          n += 1
          grid[pos_x][pos_y] = n
          moves_grid = update_grid_for_moves(pos_x, pos_y, moves_grid, move_x, move_y)

     print_grid(grid)
     
     for u in grid:
          s = ''
          for v in u:
               if v == 0:
                    s = "INCOMPLETE"
                    print(s)
                    break
               

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
               print(format(l[i][j], "3d"),end = "")
          print()
                          

def check(x, y, grid):
##     print(x,y)
     if x >= 0 and y >= 0 and x < SIZE and y < SIZE:
          if grid[x][y] == 0:
               return True
     return False

def create_grid_for_moves(lx,ly):
     l = []
     for i in range (SIZE):
          l.append([])
          for j in range (SIZE):
               d = 0
               for k in range (len(lx)):
                    if 0 <= i + lx[k] < SIZE and 0 <= j + ly[k] < SIZE:
                         d += 1
               l[i].append(d)
     return l

def update_grid_for_moves(x,y,g,lx,ly):
     g[x][y] = -1
     for i in range (len(lx)):
          if 0 <= x + lx[i] < SIZE and 0 <= y + ly[i] < SIZE:
               g[x + lx[i]][y + ly[i]] -= 1
     return g

def main():
     for i in range(SIZE):
          for j in range(SIZE):
               print(str(i*8 + j + 1) + ")")
               print()
               solve(i*8 + j + 1,i,j)
               print()
               print()
               
     
##solve()
main()
