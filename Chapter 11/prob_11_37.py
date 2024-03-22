'''11.36 (Simulation: self-avoiding random walk) Write a simulation program to show that
the chance of getting dead-end paths increases as the grid size increases. Your program
simulates lattices with sizes from 10 to 80. For each lattice size, simulate a
self-avoiding random walk 10,000 times and display the probability of the deadend
paths.'''

import random
     
def create_grid(size):## Create a 16X16 list
     g = []
     for i in range (size + 1):
          g.append([])
          for j in range (size + 1):
               g[i].append(0)
     return g 

               
def sub_main(size):
     dead_end_times = 0
     
     for i in range (10000):
          # Initialize
          g = create_grid(size) ## Create the grid 
          lpos = [size//2,size//2] # Start position on the grid
          g[size//2][size//2] = -1 
          npos = [-1,-1] # New postion of the walker to be assigned
          end_game = False

          while not end_game:
               
               #Check to determine if the walker has reached the boundary
               if lpos[0] - 1 == -1 or lpos[0] + 1 == size + 1 or lpos[1] - 1 == -1 or lpos[1] + 1 == size + 1:
                    end_game = True

               else: # If the walker has not reached the boundary, make a list of the possible places he can go
                    possibble_places = []
                    #check 1
                    if g[lpos[0] - 1][lpos[1]] != -1: # Check if he can go one step up
                         possibble_places.append([lpos[0] - 1, lpos[1]])
                    #check 2
                    if g[lpos[0] + 1][lpos[1]] != -1: # Check if he can go one step down
                         possibble_places.append([lpos[0] + 1, lpos[1]])
                    #check 3
                    if g[lpos[0]][lpos[1] - 1] != -1: # Check if he can go one step to the left
                         possibble_places.append([lpos[0], lpos[1] - 1])
                    #check 4
                    if g[lpos[0]][lpos[1] + 1] != -1: # Check if he can go one step to the right
                         possibble_places.append([lpos[0], lpos[1] + 1])

                    if len(possibble_places) == 0: ## Adead end
                         end_game = True
                         dead_end_times += 1 
                         
                    else:
                         npos = random.choice(possibble_places) # Choose one of the possible places
                         lpos = npos # Assign the updated position to lpos
                         g[npos[0]][npos[1]] = -1 # Update the grid

     print("For a lattice of size " + str(size)+ " the probability of dead-end paths is " + str(round(dead_end_times/100, 2))
           + "%.")
     


def main():
     for i in range (10, 81):
          sub_main(i)

main()

