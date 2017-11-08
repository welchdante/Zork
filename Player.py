class Player:
	import random
	
     def __init__(self):
		self.hp = random.randint(100,125)
		self.base_attack = random.randint(10,20)
		self.weapons = [10]
		
		#This is to only allow one of the weapons to be created as Hershey Kisses because they are unlimited
		weapons[10] = Weapon().__init__(self,false)
		
		#Creates the player's 10 base weapons
		for x in xrange(9):
			self.weapons[x] = Weapon().__init__(self)