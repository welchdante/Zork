class Zombie(Monster):
	import random

    def __init__(self):
		self.hp = random.randint(50,100)
		self.attack = random.randint(0,10)