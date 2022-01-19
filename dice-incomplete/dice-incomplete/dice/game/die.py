import random


# TODO: Implement the Die class as follows...
# 1) Add the class declaration. Use the following class comment.
class Die:

    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """
# 2) Create the class constructor. Use the following method comment.
    def start(dye):

        """Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """
        dye.value = 0
        dye.points = 0

# 3) Create the roll(self) method. Use the following method comment.
    def roll(rol):

        """Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
        """
        rol.value = random.randint(1,6)
        if rol.value == 5:
            rol.points = 50
        elif rol.value == 1:
            rol.points = 100
        else:
            rol.points = 0