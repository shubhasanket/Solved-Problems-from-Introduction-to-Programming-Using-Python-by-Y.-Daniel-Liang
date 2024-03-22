# Two_CirclesA
# A. Trying to add a small feature - when you are in any Entry box, pressing ENTER
# should redraw the circles - instead of having to type a number, lift your fingers - hold the
# mouse and click on the Redraw Circles button

# B. And also if we could - if desired - color the circles differently.
# So added an outline parameter - the init of Circle2D - whose default
# value is black.



''' A
1. Added
window.bind('<Return>', self.update)
so that any time you press ENTER the program calls the update function
2.
window.bind('<Return>', self.update)
The above line will call self.update when you press ENTER but will
also pass the event object even if it not required.

The following line calls self.update - here self.update is a function
with no parameters.

bt = Button(frame1, text="Redraw Circles", command=self.update)

The way out is to change the original self.update which had no parameters -
changed it to

def update(self, event = None):

Check if this works. Go to any ENTRY box - change a value and press ENTER -
it should call self.update and redraw according to the new values
'''

''' B
1. In Circle2D - changed __init__ to have an extra parameter - outline = "black"

2. In TwoCircles - added two parameters c1_outline and c2_outline - default values
are black ... but the user could change the colors.
TwoCircles(c1_outline = "blue", c2_outline = "red") to change colors of both circles
or just
TwoCircles() - both black
TwoCircles(c2_outline="green") c1 will be black and c2 will be green


3. See __init__ of TwoCircles -

4. Finally in self.draw we pass c1_outline and c2_outline to create_oval ...

5. Also added the width parameter while calling create_oval -
made width = 2 - default is 1 - See if you like this better

'''



from Circle2DA import Circle2D
from tkinter import *

VAR = 10


class TwoCircles(Circle2D):
    """Using the Circle2D class you defined, write a program that
    enables the user to specify the location and size of two circles
    and displays whether the circles intersect, as shown in Figure 12.20.
    Enable the user to point the mouse inside acircle and drag it.
    As a circle is being dragged, the program updates the circle’s
    center coordinates and its radius in the text fields.
    """

    def __init__(self, height=350, width=550, c1_outline = "black", c2_outline = "black"):
        ##          Circle2D.__init__(self) #commented out because it's not necessary
        self.height = height
        self.width = width

        # Create 2 intances of the Circle2D class
        self.c1 = Circle2D(x=(width / 2), y=(height / 2), r=(height / 5), outline = c1_outline)
        self.c2 = Circle2D(x=(width / 2), y=(height / 2), r=(height / 10), outline = c2_outline)

        window = Tk()
        window.title("Circles Intersection")

        self.canvas = Canvas(window, height=self.height, width=self.width, bg="white")
        self.canvas.pack()

        self.s = StringVar()  # Message variable
        self.s.set("One circle is contained in the other")
        self.draw()  # Draw routine

        frame = Frame(window)
        frame.pack()

        # The necessary labels, entries and Intvar variables
        # Row 1
        label1 = Label(frame, text="C1 center x:")
        label1.grid(row=1, column=1)
        self.c1_x = IntVar()
        self.c1_x.set(int(self.c1.get_x()))
        entry1 = Entry(frame, textvariable=self.c1_x, width=int(VAR / 2), justify=RIGHT)
        entry1.grid(row=1, column=2)
        label2 = Label(frame, text="C2 center x:")
        label2.grid(row=1, column=3, padx=(VAR, 0))
        self.c2_x = IntVar()
        self.c2_x.set(int(self.c2.get_x()))
        entry2 = Entry(frame, textvariable=self.c2_x, width=int(VAR / 2), justify=RIGHT)
        entry2.grid(row=1, column=4)

        # Row 2
        label3 = Label(frame, text="C1 center y:")
        label3.grid(row=2, column=1)
        self.c1_y = IntVar()
        self.c1_y.set(int(self.c1.get_y()))
        entry3 = Entry(frame, textvariable=self.c1_y, width=int(VAR / 2), justify=RIGHT)
        entry3.grid(row=2, column=2)
        label4 = Label(frame, text="C2 center y:")
        label4.grid(row=2, column=3, padx=(VAR, 0))
        self.c2_y = IntVar()
        self.c2_y.set(int(self.c2.get_y()))
        entry4 = Entry(frame, textvariable=self.c2_y, width=int(VAR / 2), justify=RIGHT)
        entry4.grid(row=2, column=4)

        # Row 3
        label5 = Label(frame, text="C1 radius:")
        label5.grid(row=3, column=1)
        self.c1_r = IntVar()
        self.c1_r.set(int(self.c1.get_radius()))
        entry5 = Entry(frame, textvariable=self.c1_r, width=int(VAR / 2), justify=RIGHT)
        entry5.grid(row=3, column=2)
        label6 = Label(frame, text="C2 radius:")
        label6.grid(row=3, column=3, padx=(VAR, 0))
        self.c2_r = IntVar()
        self.c2_r.set(int(self.c2.get_radius()))
        entry6 = Entry(frame, textvariable=self.c2_r, width=int(VAR / 2), justify=RIGHT)
        entry6.grid(row=3, column=4)

        frame1 = Frame(window)
        frame1.pack()

        # Redraw button
        bt = Button(frame1, text="Redraw Circles", command=self.update)
        bt.pack()

        # Binding the left key in motion to an event
        self.canvas.bind("<B1-Motion>", self.update_event)

        # Variables to determine which circle will be in motion
        self.move_c1 = False
        self.move_c2 = False

        # Binding the left click to select a circle
        self.canvas.bind("<Button-1>", self.select)
        window.bind('<Return>', self.update)

        window.mainloop()

    def select(self, event):
        """This method selects a circle that will be dragged"""
        # if the point is contained in c1 & c2
        if self.c1.containsPoint(event.x, event.y) and self.c2.containsPoint(
            event.x, event.y
        ):

            # Select c1 in this case
            if self.c1.contains(self.c2):
                self.move_c1 = False
                self.move_c2 = True

            # if the circles overlap, selct the circle
            # with the smaller radius
            elif self.c2.overlaps(self.c1):
                if self.c1.get_radius() <= self.c2.get_radius():
                    self.move_c1 = True
                    self.move_c2 = False

                else:
                    self.move_c1 = False
                    self.move_c2 = True

            # Select c2 in this case
            else:
                self.move_c1 = True
                self.move_c2 = False

        # Select c1 in this case
        elif self.c1.containsPoint(event.x, event.y):
            self.move_c1 = True
            self.move_c2 = False

        # Select c2 in this case
        elif self.c2.containsPoint(event.x, event.y):
            self.move_c1 = False
            self.move_c2 = True

        # Select none
        else:
            self.move_c1 = False
            self.move_c2 = False

    def update(self, event=None):
        """This method updtates the parametres of c1 and c2 and is called
        when the "Redraw Circles" button is clicked
        """

        self.c1.set_x(self.c1_x.get())
        self.c1.set_y(self.c1_y.get())
        self.c1.set_radius(self.c1_r.get())

        self.c2.set_x(self.c2_x.get())
        self.c2.set_y(self.c2_y.get())
        self.c2.set_radius(self.c2_r.get())

        self.draw()

    def update_event(self, event):
        """Update the parametres of c1 or c2 depending on which one of them
        is selected and is being dragged
        """
        if self.move_c1:
            self.c1.set_x(event.x)
            self.c1.set_y(event.y)
            self.c1_x.set(event.x)
            self.c1_y.set(event.y)

        elif self.move_c2:
            self.c2.set_x(event.x)
            self.c2.set_y(event.y)
            self.c2_x.set(event.x)
            self.c2_y.set(event.y)

        self.draw()

    def draw(self):
        """This method draws the circles and the writes the message"""
        self.canvas.delete("message", "c1", "c2")

        self.canvas.create_oval(
            (self.c1.get_x() - self.c1.get_radius()),
            (self.c1.get_y() - self.c1.get_radius()),
            (self.c1.get_x() + self.c1.get_radius()),
            (self.c1.get_y() + self.c1.get_radius()),
            tags="c1",outline = self.c1.outline, width = 2
        )
        self.canvas.create_oval(
            (self.c2.get_x() - self.c2.get_radius()),
            (self.c2.get_y() - self.c2.get_radius()),
            (self.c2.get_x() + self.c2.get_radius()),
            (self.c2.get_y() + self.c2.get_radius()),
            tags="c2",outline = self.c2.outline, width = 2
        )

        # Update message
        if self.c1.contains(self.c2) and self.c2.contains(self.c1):
            self.s.set("Both circles are identical")
            
        elif self.c1.contains(self.c2) or self.c2.contains(self.c1):
            self.s.set("One circle is contained in the other") 

        elif self.c1.overlaps(self.c2):
            self.s.set("The two circles intersect")

        else:
            self.s.set("The two circles do not intersect")

        self.canvas.create_text(
            self.width / 2, VAR, text=self.s.get(), font=("Arial, 12"), tags="message"
        )


TwoCircles(c1_outline = "blue", c2_outline = "red")
