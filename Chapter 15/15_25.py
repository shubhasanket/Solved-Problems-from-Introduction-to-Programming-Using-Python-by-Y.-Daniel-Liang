'''(Tkinter: Koch snowflake fractal ) Section 15.8 presented the Sierpinski triangle
fractal. In this exercise, you will write a program to display another fractal,
called the Koch snowflake, named after a famous Swedish mathematician. A
Koch snowflake is created as follows:
1. Begin with an equilateral triangle, which is considered to be the Koch fractal
of order (or level) 0, as shown in Figure 15.14a.
2. Divide each line in the shape into three equal line segments and draw an outward
equilateral triangle with the middle line segment as the base to create a
Koch fractal of order 1, as shown in Figure 15.14b.
3. Repeat Step 2 to create a Koch fractal of order 2, 3, ..., and so on, as shown in
Figure 15.14c–d.
'''
from tkinter import *
import math

class KochSnowflakes:
    def __init__(self):
        window = Tk()
        window.title("Koch Snowflakes")

        self.width = 200
        self.height = 200
        self.canvas = Canvas(window, width = self.width,
                             height = self.height)
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()

        label = Label(frame1, text = "Enter an order: ")
        label.pack(side = LEFT)
        self.order = StringVar()
        entry = Entry(frame1, textvariable = self.order,
                      justify = RIGHT)
        entry.pack(side=LEFT)
        button = Button(frame1, text = "Display Koch snowflakes",
                        command = self.display)
        button.pack(side = LEFT)

        window.mainloop()

    def display(self):
        self.canvas.delete("line")
        p1 = [self.width/2, 10]
        p2 = [10, self.height - 10]
        p3 = [self.width - 10, self.height - 10]
        self.displayTriangles(int(self.order.get()), p1, p2, p3)

    def displayTriangles(self, order, p1, p2, p3):
        
        
        
