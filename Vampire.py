from Monster import *
from random import randint

class Vampire(Monster):

     def __init__(self):
         self.health = randint(100, 200)
         self.attack = 0