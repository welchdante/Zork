from random import randint

class Home:

    def gen_monsters(self):
        num_monsters = randint(0,9)
        print("Num monsters:")
        print(num_monsters)
        self.gen_random_monster(num_monsters)
    
    def gen_random_monster(self, num_monsters):
        self.monsters_in_house = []
        for i in range(0, num_monsters):
            which_monster  = randint(0,4)
            monster = self.find_monster_type(which_monster)
            self.monsters_in_house.append(monster)

        print(self.monsters_in_house)

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
        print("Making a zombie")
        zombie = Zombie()
        return zombie

    def create_vampire(self):
        print("Making a vampire")
        vampire = Vampire()
        return zampire

    def create_ghoul(self):
        print("Making a ghoul")
        ghoul = Ghoul()
        return ghoul

    def create_werewolf(self):
        print("Making a werewolf")
        werewolf = Werewolf()
        return werewolf

home = Home()
home.gen_monsters()