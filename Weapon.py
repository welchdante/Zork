class Weapon:
	import random
     def __init__(self, other = true):
		
		
		if(other = true)
		
			r = random.randint(0,2)
			if(r = 0)
				self.weapon_name = "Sour Straws"
				self.attack = random.uniform(1,1.75)
				self.use_value = 2
				return self
			
			if(r = 1)
				self.weapon_name = "Chocolate Bars"
				self.attack = random.uniform(2,2.4)
				self.use_value = 4
				return self
		
			if(r = 2)
				self.weapon_name = "Nerd Bombs"
				self.attack = random.uniform(3.5,5)
				self.use_value = 1
				return self
		
		else
			self.weapon_name = "Hershey Kisses"
			self.attack = 1
			self.use_value = 999999
			return self
		