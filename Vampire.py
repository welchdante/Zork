class Vampire(Monster):
	import random
	
     def __init__(self):
		self.hp = random.randint(100,200)
		self.attack = random.randint(10,20)
		
		