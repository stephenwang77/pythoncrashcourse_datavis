import random

class Die():
    def __init__(self, numsides=6):
        self.numsides = numsides

    def roll_die(self):
        return random.randint(1, self.numsides)
