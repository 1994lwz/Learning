from random import randint

class Die():
    
    def __init__(self):
        self. sides = 6
    
    def roll_die(self):
        self.sides = randint(1, 20)
        print("The sides is: " + str(self.sides) + "\n")
    

my_die = Die()
i = 1
while i < 11:
    my_die.roll_die()
    i += 1

