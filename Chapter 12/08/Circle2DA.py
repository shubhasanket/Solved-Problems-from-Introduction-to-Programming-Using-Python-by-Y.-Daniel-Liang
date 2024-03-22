# Circle2D.py -
# Added an outline parameter - which can define the color of the outline
# of the circle. See __init__  - default is "black"

import math as m


class Circle2D:
    """Two private float data fields named x and y that specify the center
    of the circle with get/set methods.
    A private data field radius with get/set methods.
    A constructor that creates a circle with the specified x, y, and radius. The
    default values are all 0.
    A method getArea() that returns the area of the circle.
    A method getPerimeter() that returns the perimeter of the circle.
    A method containsPoint(x, y) that returns True if the specified point (x,
    y) is inside this circle (see Figure 8.10a).
    A method contains(circle2D) that returns True if the specified circle is
    inside this circle (see Figure 8.10b).
    A method overlaps(circle2D) that returns True if the specified circle
    overlaps with this circle (see Figure 8.10c).
    """

    def __init__(self, x=0, y=0, r=0, outline = "black"):
        self.x = x
        self.y = y
        self.radius = r
        self.outline = outline

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_radius(self):
        return self.radius

    def set_x(self, x):
        if x >= 0:
            self.x = x

    def set_y(self, y):
        if y >= 0:
            self.y = y

    def set_radius(self, r):
        if r >= 0:
            self.radius = r

    def getArea(self):
        return (self.radius ** 2) * m.pi

    def getPerimetre(self):
        return 2 * self.radius * m.pi

    def containsPoint(self, x, y):
        """Returns True is a point is contained in the circle,
        else returns false
        """

        if m.sqrt((x - self.x) ** 2 + (y - self.y) ** 2) < self.radius:
            return True
        else:
            return False

    def contains(self, circle):
        """Returns True is a given circle is contained in the circle,
        else returns False
        """

        if (
            m.sqrt((self.x - circle.x) ** 2 + (self.y - circle.y) ** 2) + circle.radius
            <= self.radius
        ):
            return True
        else:
            return False

    def overlaps(self, circle):
        """Returns True is a given circle is either contained or intersects
        the circle, else returns False
        """

        if self.contains(circle) or (
            m.sqrt((self.x - circle.x) ** 2 + (self.y - circle.y) ** 2)
            > self.radius + circle.radius
        ):
            return False
        else:
            return True


##a = Circle2D(100, 50, 20)
##b = Circle2D(150, 50, 50)
##
##print(a.get_radius())
##print(b.contains(a))
##print(a.overlaps(b))
##print(b.overlaps(a))
