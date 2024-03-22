from tkinter import * # Import tkinter
import tkinter.messagebox # Import tkinter.messagebox
from Sudoku import * # Import all methods from the Sudoku.py

class SudokuGUI:
    def __init__(self):
        self.window = Tk() # Create a window
        self.window.title("Solve Sudoku") # Set title
        
        self.frame = Frame(self.window) # Hold entries 
        self.frame.pack()
        
        self.cells = [] # A list of variables tied to entries
        for i in range(9):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(StringVar())

        self.entries = [] # A list of all the Entry boxes, required to change its characteristics later in the program
        for i in range(9): 
            self.entries.append([])
            
            for j in range(9):
                e = Entry(self.frame, width = 2, justify = RIGHT, 
                    textvariable = self.cells[i][j], font = ('Verdana', 20), disabledbackground = 'light grey')
                        
                e.grid(row = i, column = j)

                self.entries[i].append(e) #Adding the entries to the list
               
               
        self.frame1 = Frame(self.window) #Create a frame 
        self.frame1.pack()
        
        bt_solve = Button(self.frame1, text = "Solve", font = ('Verdana', 15), # Button to execute the solve routine
                          command = self.solve)
        bt_solve.pack(side = LEFT)

        bt_clear = Button(self.frame1, text = "Clear", font = ('Verdana', 15), # Button to execute the clear routine
                          command = self.clear) 
        bt_clear.pack(side = LEFT)                     
        
        self.window.mainloop() # Create an event loop

    # Check if the numbers entered form a valid solution
    def solve(self):
        
        grid = readAPuzzle(self.cells)# Routine is in the Sudoku file
        fixedCellList = getFixedCellList(grid)
        
        freeCellList = getFreeCellList(grid)
        
        if not isValidGrid(grid): # Check if the imput is valid or not
            tkinter.messagebox.showwarning('',"Invalid Input")

        elif search(grid): # If a solution is found, execute the following
           
            for k in range (len(fixedCellList)): # disable the entry boxes which have had an input

                i = fixedCellList[k][0]
                j = fixedCellList[k][1]
                self.entries[i][j]['state'] = "disabled"

            for l in range (len(freeCellList)): # set the values of the empty entry boxes to the processed values 
                i = freeCellList[l][0]
                j = freeCellList[l][1]
                self.cells[i][j].set(grid[i][j])

        else: ## When no solution is found
            tkinter.messagebox.showwarning('',"No Solution Found")
            


    def clear(self): # Clear the values in the entry boxes and change their 'state' to active
        
        for i in range(len(self.entries)):#(9):
            for j in range(len(self.entries[i])):
                self.entries[i][j]['state'] = 'normal'
                self.cells[i][j].set('')
                

SudokuGUI() # Create GUI
