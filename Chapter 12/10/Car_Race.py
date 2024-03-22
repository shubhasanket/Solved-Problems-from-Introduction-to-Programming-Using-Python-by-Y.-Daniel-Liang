"""12.10(Tkinter: four cars) Write a program that simulates four cars racing, as shown in
Figure 12.22. You should define a subclass of Canvas to display a car.
"""

from tkinter import *
from GUI_RacingCar import RacingCar


class Race:
    def __init__(self, l=[50] * 4):
        """This class creates 4 instances of object 'Racingcar' with
        specified velocities
        """
        window = Tk()
        window.title("Car Race")

        car1 = RacingCar(window, sleeptime=l[0])
        car1.grid(row=1, column=1)
        car2 = RacingCar(window, sleeptime=l[1])
        car2.grid(row=2, column=1)
        car3 = RacingCar(window, sleeptime=l[2])
        car3.grid(row=3, column=1)
        car4 = RacingCar(window, sleeptime=l[3])
        car4.grid(row=4, column=1)

##        window.mainloop()

Race()
Race([20, 50, 70, 30])
