class Werewolf(Monster):
	import random
	
    def __init__(self):
		self.hp = 200
		self.attack = random.randint(0,40)
		