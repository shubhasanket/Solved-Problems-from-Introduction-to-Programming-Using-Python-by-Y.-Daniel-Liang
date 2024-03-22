from Bar_Chart import Barchart
from tkinter import *

def main(l): # l is a 3 dimensional list
     window = Tk()
     window.title("BarChart Reusable")

     for i in range (len(l)):
          c = Barchart(window, l[i])
          c.grid(row=1, column=(i+1))

     window.mainloop()

l = [[[40, "CS", "red"], [30, "IS", "blue"], [50, "IT", "yellow"]],
     [[140, "Freshman", "red"], [130, "Sophomore", "blue"],
      [150, "Junior", "yellow"], [80, "Senior", "green"]]
     ]

main(l)
     
