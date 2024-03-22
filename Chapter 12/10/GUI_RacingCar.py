from tkinter import *


class RacingCar(Canvas):
    def __init__(self, container, height=100, width=500, sleeptime=50):
        """RacingCar is a subclass of Canvas. It creates a car and keeps it
        in motion.
        """
        Canvas.__init__(self, container, height=height, width=width, bg="white")
        self.height = height
        self.width = width
        self.sleeptime = sleeptime
        self.x = 0
        self.y = self.height
        self.dx = 3
        self.createCar()
        self.runcar()

    def runcar(self):
        """This method updates the position of the car"""
        if self.x < self.width:
            self.move("car", self.dx, 0)
            self.x += self.dx

        else:
            self.delete("car")
            self.x = 0
            self.createCar()

        self.after(self.sleeptime, self.runcar)

    def createCar(self):
        """This method creates a car"""
        self.create_rectangle(
            self.x, self.y - 20, self.x + 50, self.y - 10, fill="red", tags="car"
        )

        self.create_polygon(
            self.x + 10, self.y - 20, self.x + 20, self.y - 30, self.x + 30,
            self.y - 30, self.x + 40, self.y - 20, fill="blue", tags="car"
        )

        self.create_oval(
            self.x + 10, self.y - 10, self.x + 20, self.y, fill="black", tags="car"
        )
        self.create_oval(
            self.x + 30, self.y - 10, self.x + 40, self.y, fill="black", tags="car"
        )
