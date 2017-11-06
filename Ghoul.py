class Ghoul(Monster):
	import random
    
	def __init__(self):
		self.hp = random.randint(40,80)
		self.attack = random.randint(15,30)