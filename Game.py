from Neighborhood import *
from Player import * 
from random import randint

#class that holds an instance of the game
class Game:

    def __init__(self):
        self.game_over = False
        self.in_house = False

    #create the board
    def init_board(self):
        self.neighborhood = Neighborhood(10, 10)
        self.grid = self.neighborhood.make_grid(self.neighborhood.height, self.neighborhood.width)
        self.grid = self.neighborhood.fill_neighborhood(self.grid)

    #spawn and put player on random space in the grid
    def spawn_player(self, player):
        rand_width = randint(0, self.neighborhood.width - 1)
        rand_height = randint(0, self.neighborhood.height - 1)
        self.grid[rand_width][rand_height].append(player)
        self.current_width = rand_width
        self.current_height = rand_height

    #some instructions for the user
    def instructions(self):
        print("This is the simulation for how to save the world from the candy monsters.")
        print()
        print("You win when all of the houses inhabitants are converted from monsters to people")
        print()
        print("You've got some work to do...you currently have a %dx%d grid of houses full of monsters."  %(self.neighborhood.width, self.neighborhood.height))
        print()
        print("Some monsters in the houses might already be people...they want to help you.")
        print("The rest of the monsters are assholes who do NOT want to help. Sorry.")
        print()
        print("What you're allowed to do outside of houses:")
        print("W: Move North    A: Move West    S: Move South   D: Move East    E: Enter House")
        print()
        print("What you're allowed to do inside of houses:")
        print("Q: Leave House   F: Fight Monsters   0-9: Choose Weapon")
        print()
        print("Best of luck!")
        print()

    #gets and validates the user input for a move
    def get_user_move(self, player):
        possible_moves = {'w': 'North', 's': 'South', 'd': 'East', 'a': 'West', 
                            'W': 'North', 'S': 'South', 'D': 'East', 'A': 'West',
                            'e': 'Enter', 'E': 'Enter', 'q': 'Exit', 'Q': 'Exit',
                            'f': 'Fight', 'F': 'Fight'}
        if self.in_house:
            self.see_contents(player, self.current_width, self.current_height)
        move = input("What would you like to do?")
        if move in possible_moves:
            the_move = possible_moves[move]
            self.movement(player, the_move)
        else:
            print()
            print("Can't do that right now!")
            print()

    #all of the options that the player can do
    def movement(self, player, the_move):
        if the_move == 'North' and not self.in_house:
            self.move_north(player, self.current_width, self.current_height)
        elif the_move == 'South' and not self.in_house:
            self.move_south(player, self.current_width, self.current_height)
        elif the_move == 'East' and not self.in_house:
            self.move_east(player, self.current_width, self.current_height)
        elif the_move == 'West' and not self.in_house:
            self.move_west(player, self.current_width, self.current_height)
        elif the_move == 'Enter' and not self.in_house:
            self.enter_house(player, self.current_width, self.current_height)
        elif the_move == 'Exit' and self.in_house:
            self.exit_house(player)
        elif the_move == 'Fight' and self.in_house:
            self.fight(player, self.current_width, self.current_height)
        else:
            print("Invalid move")

    #moves the player up one spot in the grid
    def move_north(self, player, current_width, current_height):
        if current_height - 1 >= 0:
            self.grid[current_width][current_height].pop(len(self.grid[current_width][current_height]) - 1)
            current_height = current_height - 1
            self.grid[current_width][current_height].append(player)
            self.current_width = current_width
            self.current_height = current_height
            current_location = (self.current_width, self.current_height)
            print("Where you are: (%s, %s)" %current_location)
        else: 
            print("Stay in the neighborhood to save the world!")

    #moves the player down one spot in the grid
    def move_south(self, player, current_width, current_height):
        if current_height + 1 < self.neighborhood.height:
            self.grid[current_width][current_height].pop(len(self.grid[current_width][current_height]) - 1)
            current_height = current_height + 1
            self.grid[current_width][current_height].append(player)
            self.current_width = current_width
            self.current_height = current_height
            current_location = (self.current_width, self.current_height)
            print("Where you are: (%s, %s)" %current_location)
        else: 
            print("Stay in the neighborhood to save the world!")
    
    #moves the player right one spot in the grid
    def move_east(self, player, current_width, current_height):
        if current_width + 1 < self.neighborhood.width:
            self.grid[current_width][current_height].pop(len(self.grid[current_width][current_height]) - 1)
            current_width = current_width + 1
            self.grid[current_width][current_height].append(player)
            self.current_width = current_width
            self.current_height = current_height
            current_location = (self.current_width, self.current_height)
            print("Where you are: (%s, %s)" %current_location)
        else: 
            print("Stay in the neighborhood to save the world!")
    
    #moves the player left one spot in the grid
    def move_west(self, player, current_width, current_height):
        if current_width - 1 >= 0:
            self.grid[current_width][current_height].pop(len(self.grid[current_width][current_height]) - 1)
            current_width = current_width - 1
            self.grid[current_width][current_height].append(player)
            self.current_width = current_width
            self.current_height = current_height
            current_location = (self.current_width, self.current_height)
            print("Where you are: (%s, %s)" %current_location)
        else: 
            print("Stay in the neighborhood to save the world!")
    
    #allow the player to see the contents of the house
    def enter_house(self, player, current_width, current_height):
        self.in_house = True
        self.see_contents(player, current_width, current_height)
        print("You can either fight or leave the house")
    
    #remove the user from the house and allow for movement again
    def exit_house(self, player):
        self.in_house = False

    #handles the fight interaction between the player and the monsters
    def fight(self, player, current_width, current_height):
        current_weapons = self.see_weapons(player)
        self.choose_weapon()
        try:
            user_input = int(input("Enter which weapon:")) - 1
            if user_input > 9 or user_input < -1:
                self.enter_valid_value()
            else: 
                if user_input == -1:
                    user_input = 9
                if current_weapons[user_input].weapon_name == 'Hershey Kisses':
                    self.attack_hershey_kisses(player, current_width, current_height)
                elif current_weapons[user_input].weapon_name == 'Nerd Bombs':
                    if current_weapons[user_input].use_value > 0:
                        self.attack_nerd_bombs(player, current_width, current_height, current_weapons[user_input].attack)
                        current_weapons[user_input].use_value = current_weapons[user_input].use_value - 1
                    else:
                        self.choose_new_weapon() 
                elif current_weapons[user_input].weapon_name == 'Chocolate Bars':
                    if current_weapons[user_input].use_value > 0:
                        self.attack_chocolate_bars(player, current_width, current_height, current_weapons[user_input].attack)
                        current_weapons[user_input].use_value = current_weapons[user_input].use_value - 1
                    else:
                        self.choose_new_weapon() 
                elif current_weapons[user_input].weapon_name == 'Sour Straws':
                    if current_weapons[user_input].use_value > 0:
                        self.attack_sour_straws(player, current_width, current_height, current_weapons[user_input].attack)
                        current_weapons[user_input].use_value = current_weapons[user_input].use_value - 1
                    else:
                       self.choose_new_weapon() 
        except ValueError:
            self.enter_valid_value()
    
    #message to choose weapon, was written for readability
    def choose_weapon(self):
        print()
        print("Choose which weapon to fight with.")
        print()

    #message to choose new weapon, was written for readability
    def choose_new_weapon(self):
        print()
        print("Choose a different weapon")
        print()
    
    #message to user to enter a valid input, was written for readability
    def enter_valid_value(self):
        print()
        print("Enter a valid value from 0-9")
        print()

    #handles monster attack to the user
    def monster_attack(self, monster, player):
        player.hp = player.hp - monster.attack

    #specific attack for when the user selects to use hershey kisses        
    def attack_hershey_kisses(self, player, current_width, current_height):
        monsters_in_house = self.grid[current_width][current_height]
        for i, monster in enumerate(monsters_in_house):
            if type(monster) is not Person and type(monster) is not Player:
                monsters_in_house[i].health = monsters_in_house[i].health - player.base_attack
                if monsters_in_house[i].health <= 0:
                    monsters_in_house[i] = Person()
                else:    
                    self.monster_attack(monster, player)
            elif type(monster) is Person:
                player.hp = player.hp + 1
            else:
                print()
        if player.hp <= 0 :
            self.end_game()

    #specific attack for when the user selects to use nerd bombs           
    def attack_nerd_bombs(self, player, current_width, current_height, modifier):
        monsters_in_house = self.grid[current_width][current_height]
        for i, monster in enumerate(monsters_in_house):
            if type(monster) is not Person and type(monster) is not Player:
                if type(monster) is Ghoul:
                    monsters_in_house[i].health = monsters_in_house[i].health -  (5 * player.base_attack)
                else:
                    monsters_in_house[i].health = monsters_in_house[i].health - (modifier * player.base_attack)
                if monsters_in_house[i].health <= 0:
                    monsters_in_house[i] = Person()
                else:    
                    self.monster_attack(monster, player)
            elif type(monster) is Person:
                player.hp = player.hp + 1
            else:
                print("")
        if player.hp <= 0 :
            self.end_game()
    
    #specific attack for when the user selects to use chocolate bars
    def attack_chocolate_bars(self, player, current_width, current_height, modifier):
        print(modifier)
        monsters_in_house = self.grid[current_width][current_height]
        for i, monster in enumerate(monsters_in_house):
            if type(monster) is not Person and type(monster) is not Player:
                if type(monster) is Vampire or Werewolf:
                    monsters_in_house[i].health = monsters_in_house[i].health - player.base_attack
                else:
                    monsters_in_house[i].health = monsters_in_house[i].health - (modifier * player.base_attack)
                if monsters_in_house[i].health <= 0:
                    monsters_in_house[i] = Person()
                else:    
                    self.monster_attack(monster, player)
            elif type(monster) is Person:
                player.hp = player.hp + 1
            else:
                print("")
        if player.hp <= 0 :
            self.end_game()

    #specific attack for when the user selects to use sour straws 
    def attack_sour_straws(self, player, current_width, current_height, modifier):
        monsters_in_house = self.grid[current_width][current_height]
        for i, monster in enumerate(monsters_in_house):
            if type(monster) is not Person and type(monster) is not Player:
                if type(monster) is Zombie:
                    monsters_in_house[i].health = monsters_in_house[i].health -  (2 * (modifier * player.base_attack))
                elif type(Monster) is Werewolf:
                    monsters_in_house[i].health = monsters_in_house[i].health - player.base_attack
                else:
                    monsters_in_house[i].health = monsters_in_house[i].health - (modifier * player.base_attack)
                if monsters_in_house[i].health <= 0:
                    monsters_in_house[i] = Person()
                else:    
                    self.monster_attack(monster, player)
            elif type(monster) is Person:
                player.hp = player.hp + 1
            else:
                print("")
        if player.hp <= 0 :
            self.end_game()
    
    def end_game(self):
        self.game_over = True;
        print("You died!")

    #shows monsters in the house
    def see_contents(self, player, current_width, current_height):
        print("Contents of the house: ")
        for monster in self.grid[current_width][current_height]:
            if type(monster) is Ghoul:
                monster.attack = randint(15,30)
                attributes = (monster.health, monster.attack)
                print("Ghoul         Health: %d      Attack: %d" %attributes)    
            elif type(monster) is Vampire:
                monster.attack = randint(10,20)
                attributes = (monster.health, monster.attack)
                print("Vampire       Health: %d     Attack: %d" %attributes)
            elif type(monster) is Werewolf:
                monster.attack = randint(0,40)
                attributes = (monster.health, monster.attack)
                print("Werewolf      Health: %d     Attack: %d" %attributes)
            elif type(monster) is Zombie:
                monster.attack = randint(0,10)
                attributes = (monster.health, monster.attack)
                print("Zombie        Health: %d      Attack: %d" %attributes)
            elif type(monster) is Person:
                attack_this_turn = -1
                attributes = (monster.health, attack_this_turn)
                print("Person        Health: %d     Attack: %d" %attributes)
            else:
                player.base_attack = randint(10,20)
                attributes = (player.hp, player.base_attack)
                print()
                print("Yourself      Health: %d    Attack: %d" %attributes)
                print()
        return self.grid[current_width][current_height]

    #shows the current weapons the user has available
    def see_weapons(self, player):
        print("Current weapons: ")
        i = 1
        for weapon in player.weapons:
            if i == 10:
                i = 0
            attributes = (i, weapon.attack, weapon.use_value)
            if weapon.weapon_name == "Sour Straws":
                print("%d) Sour Straw          Modifier:%d        Uses Left:%d" %attributes) 
            elif weapon.weapon_name == "Chocolate Bars":
                print("%d) Chocolate Bar       Modifier:%d        Uses Left:%d" %attributes)
            elif weapon.weapon_name == "Nerd Bombs":
                print("%d) Nerd Bomb           Modifier:%d        Uses Left:%d" %attributes) 
            elif weapon.weapon_name == "Hershey Kisses":
                print("%d) Hershey Kiss        Modifier:%d        Uses Left:%d" %attributes)
            i = i + 1
        return player.weapons