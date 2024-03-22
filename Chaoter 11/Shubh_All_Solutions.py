#11/09/20  Shubh_All_Solutions.py
#THE PORTION THAT IS REPEATED IS DONE IN TWO CASES
#1 IF YOU FOUND A SOLUTION OR 2. isValid(i, j, grid) WAS NOT TRUE
#WE KEEP TWO BOOLEAN VARIABLES FOR THESE TWO CASES
#THEY BECOME TRUE IF WE LAND IN ANY OF THE ABOVE TWO CASES
#(COULD WE KEEP ONE VARIABLE BUT PERHAPS TWO IS CLEARER)

#THE CODE THAT WAS REPEATED IS DONE ONLY IF ONE OF THE
#TWO BOOLEAN VARIABLES IS TRUE.

#IT IS ALWAYS BETTER NOT TO HAVE GLOBAL VARIABLES
#SO TRIED TO REMOVE at_least_one_sol_found BY KEEPING
#A COUNTER FOR THE NUMBER OF SOLUTIONS FOUND AND
#THE SEARCH FUNCTIONS RETURNS THE NUMBER OF SOLUTIONS FOUND.
#IF THAT IS ZERO THEN NO SOLUTIONS WERE FOUND

#SOMETIME THERE ARE VERY MANY SOLUTIONS AND YOU CAN NOT PRINT
#ALL OF THEM - TOO MANY - SO WE COULD KEEP THE MAXIMUM NUMBER
#OF SOLUTIONS WE WILL PRINT.
#SO WE COULD ADD A COUNTER IN THE SERACH FUNCTION THAT
#WILL COUNT THE NUMBER OF SOLUTIONS FOUND AND IF WE HAVE
#FOUND THE MAX NUMBER WE COME OUT OF SEARCH.

#I HAVE ADDED ANOTHER SET FOR GRID - THAT ONE HAS MANY
#SOLUTIONS - YOU COULD CHECK THE PROGRAM WITH THAT ALSO
#
#YOUR GRID HAS TWO SOLUTIONS.

#ALSO AM PRINTING THE SOLUTION AS WE FIND IT.

# Grid with 1 solution
##grid = [[5,3,0,0,7,0,0,0,0],
##        [6,0,0,1,9,5,0,0,0],
##        [0,9,8,0,0,0,0,6,0],
##        [8,0,0,0,6,0,0,0,3],
##        [4,0,0,8,0,3,0,0,1],
##        [7,0,0,0,2,0,0,0,6],
##        [0,6,0,0,0,0,2,8,0],
##        [0,0,0,4,1,9,0,0,5],
##        [0,0,0,0,8,0,0,7,9]]

## Grid with no solution
##grid = [[5,3,0,0,7,0,0,0,0],
##        [6,0,0,1,9,5,0,0,0],
##        [0,9,8,0,0,0,0,6,0],
##        [8,1,0,0,6,0,0,0,3],
##        [4,0,0,8,0,3,0,0,1],
##        [7,0,0,0,2,0,0,0,6],
##        [0,6,0,0,0,0,2,8,0],
##        [0,0,0,4,1,9,0,0,5],
##        [0,0,0,0,8,0,0,0,9]]


###Try this example - it has many solutions
###Make your program stop after a certain
###number of solutions - say 10.
##grid= [ [1,0,4,0,0,9,7,0,8],  
##        [0,2,0,3,0,0,6,0,0],
##        [6,0,3,0,0,0,0,0,1],
##        [0,0,5,0,0,0,0,0,0],
##        [2,0,0,0,0,0,3,0,0],
##        [0,0,0,9,0,1,0,0,0],
##        [3,0,0,0,5,0,1,0,9],
##        [0,0,1,2,0,0,0,0,0],
##        [0,4,0,0,0,0,0,7,0]
##      ]  


##at_least_one_sol_found = False

#THIS IS THE MAXIMUM NUMBER OF SOLUTIONS THAT WE WILL PRINT
#SOME PUZZLES HAVE MANY MANY SOLUTIONS

import sys


def readPuzzle(filename):
    """
    reads a Sudoku puzzle and stores into grid - a list of 9 list of rows
    """
    grid = []
    if filename=="":
        #User will type in the data row by row as a string
        #0 for empty cell
        for i in range(9):
            grid.append([])
            row = input("Data for row",i,":")
            for c in row:
                grid[i].append(eval(c))
    else:
        #We expect the input from a text file in the same directory
        try:
            fin = open(filename)
            i=0
            for line in fin:
                row = line.strip()
                grid.append([])
                for c in row:
                    grid[i].append(eval(c))
                i=i+1    
            fin.close()        
                   
        except IOError:
            print("No such file found!")
            sys.exit()
    return grid



MAX_SOLUTIONS = 5

def main():

    grid = readPuzzle("Sudoku_grid")
    
    if not isValidGrid(grid):
        print("Invalid input")

    c = search(grid)

    if c == 0:
        print("No solution")
    else:
        if c < MAX_SOLUTIONS:
            print("Found",c,"solutions!")
        else:
            print("Here are the first",c,"solutions!")
    
# Read a Sudoku puzzle from the keyboard 
def readAPuzzle():  
    print("Enter a Sudoku puzzle:")
    grid = []
    for i in range(9):
        line = input().split()
        grid.append([eval(x) for x in line])
    return grid               

# Obtain a list of free cells from the puzzle 
def getFreeCellList(grid):
    freeCellList = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                freeCellList.append([i, j])

    return freeCellList

# Display the values in the grid 
def printGrid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end = " ")
        print()

# Search for a solution 
def search(grid):
    #COUNTER FOR THE NUMBER OF SOLUTIONS FOUND
    count = 0
    freeCellList = getFreeCellList(grid)
    numberOfFreeCells = len(freeCellList)
    if numberOfFreeCells == 0:
        printGrid(grid) # No free cells
    
    k = 0 # Start from the first free cell
    while k >= 0:
        sol_found = False
        invalid = True
        i = freeCellList[k][0]
        j = freeCellList[k][1]
        if grid[i][j] == 0:
          grid[i][j] = 1 # Fill the free cell with number 1
    
        if isValid(i, j, grid):
          if k + 1 == numberOfFreeCells:
            # No more free cells
            sol_found = True # A solution is found
            count = count + 1 #number of solutions found
            #So print it
            print("Solution",count,"................")
            printGrid(grid)
            print('.................................')
            if count >= MAX_SOLUTIONS:
                return count
          else:
            # Move to the next free cell
            k += 1
            invalid = False  #The cell was valid


        if invalid or sol_found:
            #IN THESE TWO CASES WE HAVE TO DO THE FOLLOWING
            if grid[i][j] < 9:
              # Fill the free cell with the next possible value
              grid[i][j] = grid[i][j] + 1
              
            else:
              # grid[i][j] is 9, backtrack
              while grid[i][j] == 9:
                
                grid[i][j] = 0 # Reset to free cell
                k -= 1 # Backtrack to the preceding free cell
                i = freeCellList[k][0]
                j = freeCellList[k][1]
        
              # Fill the free cell with the next possible value, 
              # search continues from this free cell at k
              grid[i][j] = grid[i][j] + 1

    return count

# Check whether grid[i][j] is valid in the grid 
def isValid(i, j, grid):
    # Check whether grid[i][j] is valid at the i's row
    for column in range(9):
        if column != j and grid[i][column] == grid[i][j]:
          return False
    
    # Check whether grid[i][j] is valid at the j's column
    for row in range(9):
        if row != i and grid[row][j] == grid[i][j]:
          return False
    
    # Check whether grid[i][j] is valid in the 3-by-3 box
    for row in range((i // 3) * 3, (i // 3) * 3 + 3):
        for col in range((j // 3) * 3, (j // 3) * 3 + 3):
            if row != i and col != j and grid[row][col] == grid[i][j]:
                return False
    
    return True # The current value at grid[i][j] is valid

# Check whether the fixed cells are valid in the grid 
def isValidGrid(grid): 
    for i in range(9):
        for j in range(9):
            if grid[i][j] < 0 or grid[i][j] > 9 or \
                (grid[i][j] != 0 and not isValid(i, j, grid)): 
                return False

    return True # The fixed cells are valid

main()
