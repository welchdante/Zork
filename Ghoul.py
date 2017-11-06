from Monster import *
from random import randint

class Ghoul(Monster):

     def __init__(self):
         self.health = randint(40,80)
         self.attack = 0