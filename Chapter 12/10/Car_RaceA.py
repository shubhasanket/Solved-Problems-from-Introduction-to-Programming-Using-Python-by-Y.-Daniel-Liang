"""12.10(Tkinter: four cars) Write a program that simulates four cars racing, as shown in
Figure 12.22. You should define a subclass of Canvas to display a car.
"""

from tkinter import *
from GUI_RacingCar import RacingCar
import random

class Race:
    def __init__(self, numberOfCars = 4, carSpeeds = [50,50,50,50]):
        """This class creates 4 instances of object 'Racingcar' with
        specified velocities
        """
        window = Tk()
        window.title("Car Race")
        for i in range(numberOfCars):
            c = RacingCar(window, sleeptime = carSpeeds[i])
            c.grid(row = i + 1, column = 1)

        window.mainloop()

#Race()
def main():

    #Change the number of cars
    n = random.randint(2,6)

    carList = []
    #Generate random speeds for the n cars
    for i in range(n):
        s = random.randint(2,9) * 10
        carList.append(s)
        
    print(n,"cars with speeds",carList,"racing against each other")    
    Race(n, carList)  #20,50,70,30

main()    

'''
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

        window.mainloop()

#Race()
Race([20, 50, 70, 30])  #20,50,70,30
'''
