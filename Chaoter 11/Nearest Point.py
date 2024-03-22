'''(Geometry: find nearest points) When a new point is added to the plane, Listing
11.5 finds the pair of two nearest points by examining the distance between every
pair of two points. This approach is correct, but not efficient. A more efficient algorithm
can be described as follows:
Let d be the current shortest distance between two
     nearest points p1 and p2
Let p be the new point added to the plane
     For each existing point t:
          if distance(p, t) < d:
               d = distance(p, t)
               p1, p2 = p, t
Rewrite Listing 11.5 using this new approach.
'''
from tkinter import *

RADIUS = 4
class NearestPointsGUI:
     def __init__(self, height = 400, width = 700):
          self.points = [] # Store self.points
          window = Tk() # Create a window
          window.title("Find Nearest Points") # Set title

          self.canvas = Canvas(window, width = width, height = height, bg = "white")
          self.d = (width**2 + height**2)**0.5 # setting self.d to the maximum value possible in the given canvas
          self.p1 = 0 # p1 and p2 are the indexes of the points with the shortest distances.
          self.p2 = 0
          self.canvas.pack()

          self.canvas.bind("<Button-1>", self.addPoint)

          window.mainloop()

     def addPoint(self, event):
          if not self.isTooCloseToOtherPoints(event.x, event.y):
               self.addThisPoint(event.x, event.y)

     def addThisPoint(self, x, y):
          # Display this point
          self.canvas.create_oval(x - RADIUS, y - RADIUS,
               x + RADIUS, y + RADIUS)
          # Add this point to self.points list
          self.points.append([x, y])
          if len(self.points) > 2:
               p1, p2 = self.nearestPoints()
               self.canvas.delete("line")
               self.canvas.create_line(self.points[p1][0],
                    self.points[p1][1], self.points[p2][0],
                    self.points[p2][1], width = int(RADIUS/2), tags = "line")

     def isTooCloseToOtherPoints(self, x, y):
          for i in range(len(self.points)):
               if self.distance(x, y, self.points[i][0], self.points[i][1]) <= 2*RADIUS:
                    return True

               
     def nearestPoints(self):

     # Compute distance between every two points
          l = len(self.points)-1
          for i in range(l):
               d = self.distance(self.points[i][0], self.points[i][1], self.points[l][0], self.points[l][1])
               if self.d > d:
                    self.d = d
                    self.p1, self.p2 = i, l # Update p1, p2

          return self.p1, self.p2


     # Compute the distance between two points (x1, y1) and (x2, y2)
     def distance(self,x1, y1, x2, y2):
          return ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5




NearestPointsGUI()














     
