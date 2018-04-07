import random

class Die:

    def __init__(self,sides):
        self.sides = sides

    def roll(self):
        return random.randint(0,self.sides)
