"""12.10(Tkinter: four cars) Write a program that simulates four cars racing, as shown in
Figure 12.22. You should define a subclass of Canvas to display a car.


I tried to run the program from the command prompt and it did not work.
COMMENT: There is no mainloop so the program just goes through - not waiting for anything.

Once I included window.mainloop(), it worked.
COMMENT:Now the mainloop will go on waiting for events - so till you close the windows
COMMENT:your program will run.
I have gone through the modifications you have made.

The reason why I had removed window.mainloop() was to have two different
windows functioning simultaneously. When it was not commented out,
only one window opened. After I closed the first window,
the second window opened. Is it possible to have two windows
functioning simultaneously by running the program from the command prompt
when window.mainloop() is included?

MORE COMMENTS
When you were commenting out the window.mainloop() - you were using the
mainloop of IDLE - so the program worked - but will not work from the
terminal because there is no more any mainloop .

When you do not comment it out - what happens is that when you
call Race() - the first time - it is running only the first Race
and using the mainloop of that Race. When you close it - that mainloop closes,
you go to the second Race and then run the mainloop of the second Race
and run it till it is closed. So only one mainloop is running at a time.

A program should have only one mainloop - so we shift it outside Race!

The main program opens a window (root) which is the parent of any Race Window.
When you call Race - you pass it the root window. The Toplevel function opens
a window inside a parent window - which is in our case the root window. So each
time you call Race - a new window in created inside the same root window.
And the mainloop of the root controls all the child windows. All the windows
are open and all the cars in all the windows run.

Notice the following in the init of Race:
        self.window.protocol("WM_DELETE_WINDOW", self.closeWindow)
        
When you press the X of a window - it calls the self.closeWindow of that Race instance.
This function reduces the number of windows open, and closes that Race window
using self.window.destroy()

and when the number
of Race windows open equals 0 - it closes the parent window (which is the root window).

See the comments about wCount ... this way we avoid the use of a global variable.
We should always limit the use of global variables ...

A PROGRAM HAS TO WORK FROM THE TERMINAL - ALL USERS DO NOT USE IDLE. IN FACT AFTER A WHILE
YOU MIGHT ALSO NOT BE USING IT.

"""

from tkinter import *
from GUI_RacingCar import RacingCar

class Race:
    #This is a class variable - it is declared outside any function
    #of a class but can be accessed/altered by any function by
    #preceding it by the class name (i.e. Race.wCount)
    wCount = 0
    def __init__(self, root, race, l=[50] * 4):
        """This class creates 4 instances of object 'Racingcar' with
        specified velocities
        """
        self.parent = root
        self.race = race
        print("Starting race",self.race)
        
        #Toplevel creates a window in the root window
        self.window = Toplevel(self.parent)
        
        self.window.title("Car Race"+str(self.race))
        
        #When you hit the cross on this window - it will call
        #the self.closeWindow function
        self.window.protocol("WM_DELETE_WINDOW", self.closeWindow)
        
        Race.wCount += 1  #Increase the count of the Race Windows open
        
        car1 = RacingCar(self.window, sleeptime=l[0])
        car1.grid(row=1, column=1)
        car2 = RacingCar(self.window, sleeptime=l[1])
        car2.grid(row=2, column=1)
        car3 = RacingCar(self.window, sleeptime=l[2])
        car3.grid(row=3, column=1)
        car4 = RacingCar(self.window, sleeptime=l[3])
        car4.grid(row=4, column=1)


    def closeWindow(self):
        #User the cross on the right top corner of this window
        print("Ending Race", self.race)
        Race.wCount -= 1  #Decrease the count of the Race Windows open
        print("Closing window", self.race)
        print("Windows remaining",Race.wCount)
        self.window.destroy()   #Close this Race Window
        if Race.wCount == 0:
            print("No more windows left")
            #If no more Race Windows are open then
            #close the main window
            self.parent.destroy()
            
        #THERE CAN BE ONLY ONE MAINLOOP - so we shift it to
        #to the the main program - otherwise each instance
        #of Race will have its main loop
            
        #window.mainloop()

def main():
        #Create the main window - inside which various
        #race windows will be created
        root = Tk()
        #We do not want to see the root window - the following command does that
        #it is there but not seen.
        root.withdraw()
        #We send to Race - the main parent window and the race number
        #Race number is not required just to help us understand
        Race(root, 1)
        Race(root, 2,[20, 50, 70, 22])
        Race(root, 3)

        root.mainloop()
main()
