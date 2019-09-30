"""
To create a random walk, we’ll create a RandomWalk class, which will make random decisions about which direction the walk should take.
The class needs three attributes: one variable to store the number of points in the walk and two lists to store the x- and y-coordinate values of each
point in the walk.
We’ll use only two methods for the RandomWalk class: the __init__() method and fill_walk(), which will calculate the points in the walk.
Let’s start with __init__() as shown here:
"""

from random import choice

class RandomWalk():
    def __init__(self, numpoints=5000):
        self.numpoints = numpoints
        self.choice_range = 5

        # These are the two lists of coordinates which start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Append the new coordinates to x/y value lists"""
        while len(self.x_values) < self.numpoints:
            # Add the value of x-steps/y-steps to the latest coordinates
            x_step = self.get_steps()
            y_step = self.get_steps()
            updated_coordinates_x = self.x_values[-1] + x_step
            updated_coordinates_y = self.y_values[-1] + y_step
            self.x_values.append(updated_coordinates_x)
            self.y_values.append(updated_coordinates_y)

    def get_steps(self):
        """Refactoring calculation of steps from the fill_walk() function"""
        direction = choice([1,-1])
        distance = choice([x for x in range(1, self.choice_range)])
        return direction * distance
