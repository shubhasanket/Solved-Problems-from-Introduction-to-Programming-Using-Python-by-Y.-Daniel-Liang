'''11.36 Simulation using Turtle: self-avoiding random walk) A self-avoiding walk in a
lattice is a path from one point to another that does not visit the same point twice.
Self-avoiding walks have applications in physics, chemistry, and mathematics.
They can be used to model chainlike entities such as solvents and polymers. Write
a Turtle program that displays a random path that starts from the center and ends at
a point on the boundary, as shown in Figure 11.11a, or ends at a dead-end point
(i.e., surrounded by four points that have already been visited), as shown in Figure
11.11b. Assume the size of the lattice is 16 * 16.'''

import turtle as t 
import random

a = 24 ## a is the scale
size = 16 ## size of the lattice

def draw_lattice():## Draw the lattice
     t.ht()
     t.color("light grey")
     t.tracer(1000, 0) #Screen will updtae after that many moves
     #t.speed(0)
     t.pensize(2)

     x = a*10
     for y in range (-a*10, a*10 + 1, int(2*a*10/size)):
          t.penup()
          t.goto(-x, y)
          t.pendown()
          t.goto(x, y)

     y = a*10
     for x in range (-a*10, a*10 + 1, int(2*a*10/size)):
          t.penup()
          t.goto(x, y)
          t.pendown()
          t.goto(x, -y)

     t.update()
     
def create_grid():## Create a 16X16 list
     g = []
     for i in range (17):
          g.append([])
          for j in range (17):
               g[i].append(0)
     return g 

def draw_new_pos(l1, l2):
     
     if l1[0] != l2[0]:
          if l1[0] > l2[0]: # the walker moves one step up
               n = 90 # 90 degres anti-clockwise from the horizontal
          else:             # the walker moves one step down
               n = 270 
     else:
          if l1[1] > l2[1]: # The walker moves one step to the left 
               n = 180
          else:
               n = 0 # the walker moves one step to the right

     t.setheading(n)
     t.forward(int(2*a*10/size))


               
def main():
     # Initialize
     draw_lattice()
     create_grid()
     t.color("black")
     t.penup()
     t.goto(0,0) ## Start position on the lattice
     t.pendown()
     g = create_grid() ## Create the grid 
     lpos = [8,8] # Start position on the grid
     g[8][8] = -1 
     npos = [-1,-1] # New postion of the walker to be assigned
     end_game = False

     while not end_game:
          
          #Check to determine if the walker has reached the boundary
          if lpos[0] - 1 == -1 or lpos[0] + 1 == 17 or lpos[1] - 1 == -1 or lpos[1] + 1 == 17:
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

               if len(possibble_places) == 0: ## Dead end
                    end_game = True
                    
               else:
                    npos = random.choice(possibble_places) # Choose one of the possible places
                    draw_new_pos(lpos, npos)
                    lpos = npos # Assign the updated position to lpos
                    g[npos[0]][npos[1]] = -1 # Update the grid

     t.update()
     t.done()
     


main()

