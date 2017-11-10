from random import randint
from Weapon import *

class Player:
	
	def __init__(self):
		self.hp = randint(100,125)
		self.base_attack = randint(10,20)
		self.weapons = []
		
	def gen_weapons(self, weapons):
		is_hersey_kiss = False
		new_weapon = Weapon(is_hersey_kiss)
		self.weapons.append(new_weapon)
		is_hersey_kiss = True
		for x in xrange(9):
			new_weapon = Weapon(is_hersey_kiss)
			self.weapons.append(new_weapon)
		return weapons

player = Player()
player.gen_weapons(player.weapons)