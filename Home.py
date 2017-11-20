from random import randint
from Monster import *
from Person import *
from Zombie import *
from Vampire import *
from Ghoul import *
from Werewolf import *

class Home:

    def gen_monsters(self):
        num_monsters = randint(0,9)
        monsters = self.gen_random_monsters(num_monsters)
        return monsters
    
    def gen_random_monsters(self, num_monsters):
        self.monsters_in_house = []
        for i in range(0, num_monsters):
            which_monster  = randint(0,4)
            monster = self.gen_single_monster(which_monster)
            self.monsters_in_house.append(monster)
        #print(self.monsters_in_house)
        return self.monsters_in_house

    def gen_single_monster(self, which_monster):    
        if which_monster == 0:
            monster = self.create_person()
        if which_monster == 1:
            monster = self.create_zombie()
        if which_monster == 2:
            monster = self.create_vampire()
        if which_monster == 3:
            monster = self.create_ghoul()
        if which_monster == 4:
            monster = self.create_werewolf()
        return monster
    
    def create_person(self):
        person = Person()
        return person
    
    def create_zombie(self):
        zombie = Zombie()
        return zombie

    def create_vampire(self):
        vampire = Vampire()
        return vampire

    def create_ghoul(self):
        ghoul = Ghoul()
        return ghoul

    def create_werewolf(self):
        werewolf = Werewolf()
        return werewolf
    
    def get_population(self, monsters_in_house):
        population = len(monsters_in_house)
        return population
