import random

class Die:

    def __init__(self,sides):
        self.sides = sides

    def roll(self,num_of_dice):
        return random.randint(1,int(self.sides))
