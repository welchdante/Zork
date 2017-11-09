from random import random, randint
class Weapon:

     def __init__(self, other = true):
		if other:
		
			r = randint(0,2)
			if r == 0 :
				self.weapon_name = "Sour Straws"
				self.attack = uniform(1,1.75)
				self.use_value = 2
			
			if r == 1 :
				self.weapon_name = "Chocolate Bars"
				self.attack = uniform(2,2.4)
				self.use_value = 4
		
			if r == 2 :
				self.weapon_name = "Nerd Bombs"
				self.attack = uniform(3.5,5)
				self.use_value = 1
		
		else:
			self.weapon_name = "Hershey Kisses"
			self.attack = 1
			self.use_value = 999999
