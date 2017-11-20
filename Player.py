from random import randint
from Weapon import *

class Player:
	
	def __init__(self):
		self.hp = randint(100,125)
		self.base_attack = 0
		self.weapons = []
		
	def gen_weapons(self, weapons):
		is_hershey_kiss = False
		new_weapon = Weapon(is_hershey_kiss)
		self.weapons.append(new_weapon)
		is_hershey_kiss = True
		for x in range(9):
			new_weapon = Weapon(is_hershey_kiss)
			self.weapons.append(new_weapon)
		return weapons