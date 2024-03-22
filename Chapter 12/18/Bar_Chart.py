"""12.18 (Tkinter: the BarChart class) Develop a class named
BarChart that extends Canvas for displaying a bar chart:
BarChart(parent, data, width = 400, height = 300)
Where data is a list, each element in the list is a nested list
that consists of a value, a title for the value, and a color for the bar
in the bar chart. For example, for data = [[40, "CS", "red"], [30, "IS", "blue"],
[50, "IT", "yellow"]], the bar chart is as shown in the left part of Figure 12.28.
For data= [[140, "Freshman", "red"], [130, "Sophomore", "blue"],
[150, "Junior", "yellow"], [80, "Senior", "green"]], the bar
chart is as shown in the right part of Figure 12.28. Write a test program
that displays two bar charts, as shown in Figure 12.28.
"""
from tkinter import *

class Barchart(Canvas):
     def __init__(self, parent, data, width=400, height=300):
          Canvas.__init__(self, parent, width=width, height=height, bg="white")
          l = data
          max_height = (4/5) * height # max height of a bar
          min_y = (0.9)*height # strarting point of the bars
          gap = round(width/30) # white space on the left and on the right
          length = round((width - 2*gap) / len(l)) # width of each bar
          val = 15
               
          scale = l[0][0]
          for i in range (1, len(l)): # Find the biggest value of the set 
               if scale < l[i][0]:
                    scale = l[i][0]

          for i in range (len(l)):
               self.create_rectangle(gap + i*length, min_y - ((max_height*l[i][0])/scale),
                                     gap + (length*(i+1)), min_y, fill=l[i][2]
                                     )
               self.create_text(gap + (i+0.5) * length, min_y + val, text=l[i][1])
