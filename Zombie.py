from Monster import *
from random import randint

class Zombie(Monster):

      def __init__(self):
            self.health = randint(50,100)
            self.attack = 0