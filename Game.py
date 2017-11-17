from Neighborhood import *
from Player import * 
from random import randint

class Game:

    def __init__(self):
        self.game_over = False
        self.in_house = False

    def init_board(self):
        self.neighborhood = Neighborhood(4, 4)
        self.grid = self.neighborhood.make_grid(self.neighborhood.height, self.neighborhood.width)
        self.grid = self.neighborhood.fill_neighborhood(self.grid)
        #pprint(self.grid)

    def spawn_player(self, player, game):
        rand_width = randint(0, game.neighborhood.width - 1)
        rand_height = randint(0, game.neighborhood.height - 1)
        #pprint("Contents in the home")
        game.grid[rand_width][rand_height].append(player)
        self.current_width = rand_width
        self.current_height = rand_height
        #pprint(game.grid[rand_width][rand_height])

    def get_user_move(self, player, game):
        possible_moves = {'w': 'North', 's': 'South', 'd': 'East', 'a': 'West', 
                            'W': 'North', 'S': 'South', 'D': 'East', 'A': 'West',
                            'e': 'Enter', 'E': 'Enter', 'q': 'Exit', 'f': 'Fight',
							'F': 'Fight', 'Q': 'Exit'}
        move = input("What would you like to do?")
        if move in possible_moves:
            the_move = possible_moves[move]
            self.movement(player, game, the_move)
        else:
            print("Silly person, that's not a direction")

    def movement(self, player, game, the_move):
        if the_move == 'North' and not self.in_house:
            self.move_north(player, game, self.current_width, self.current_height)
        elif the_move == 'South' and not self.in_house:
            self.move_south(player, game, self.current_width, self.current_height)
        elif the_move == 'East' and not self.in_house:
            self.move_east(player, game, self.current_width, self.current_height)
        elif the_move == 'West' and not self.in_house:
            self.move_west(player, game, self.current_width, self.current_height)
        elif the_move == 'Enter' and not self.in_house:
            self.enter_house(player, game, self.current_width, self.current_height)
        elif the_move == 'Exit' and self.in_house:
            self.exit_house(player, game)
		elif the_move == 'Fight' and self.in_house:
			self.fight(self, player, game)
        else:
            print("Invalid move")

    def move_north(self, player, game, current_width, current_height):
        print("Move north")
        if current_height - 1 >= 0:
            game.grid[current_width][current_height].pop(len(game.grid[current_width][current_height]) - 1)
            current_height = current_height - 1
            game.grid[current_width][current_height].append(player)
            self.current_width = current_width
            self.current_height = current_height
        else: 
            print("Stay in the neighborhood to save the world!")

    def move_south(self, player, game, current_width, current_height):
        print("Move south")
        if current_height + 1 < self.neighborhood.height:
            game.grid[current_width][current_height].pop(len(game.grid[current_width][current_height]) - 1)
            current_height = current_height + 1
            game.grid[current_width][current_height].append(player)
            self.current_width = current_width
            self.current_height = current_height
        else: 
            print("Stay in the neighborhood to save the world!")
    
    def move_east(self, player, game, current_width, current_height):
        print("Move east")
        if current_width + 1 < self.neighborhood.width:
            game.grid[current_width][current_height].pop(len(game.grid[current_width][current_height]) - 1)
            current_width = current_width + 1
            game.grid[current_width][current_height].append(player)
            self.current_width = current_width
            self.current_height = current_height
        else: 
            print("Stay in the neighborhood to save the world!")
    
    def move_west(self, player, game, current_width, current_height):
        print("Move west")
        if current_width - 1 >= 0:
            game.grid[current_width][current_height].pop(len(game.grid[current_width][current_height]) - 1)
            current_width = current_width - 1
            game.grid[current_width][current_height].append(player)
            self.current_width = current_width
            self.current_height = current_height
        else: 
            print("Stay in the neighborhood to save the world!")
    
    def enter_house(self, player, game, current_width, current_height):
        self.in_house = True
        self.see_contents(game, current_width, current_height)
        print("You can either fight or leave the house")
    
    def exit_house(self, player, game):
        self.in_house = False
		
	def fight(player, game, current_width, current_height):
		weapon_input = 'a'
		print("Current monsters in this house are: " + self.see_contents)
		print("Current weapons are: " + self.weapons)
		print("Choose which weapon to fight with.")
		
		while(weapon_input.type != int)
			weapon_input = input("Enter a value 0-9: ")
		
		if self.weapons[weapon_input] == 'Hershey Kisses' :
			fight_hersheyKisses(player, game, current_width, current_height)
		elif self.weapons[weapon_input] == 'Nerd Bombs' :
			fight_nerdBombs(player, game, current_width, current_height, weapon_input)
		elif self.weapons[weapon_input] == 'Chocolate Bars' :
			fight_chocolateBars(player, game, current_width, current_height, weapon_input)
		elif self.weapons[weapon_input] == 'Sour Straws' :
			fight_sourStraws(player, game, current_width, current_height, weapon_input)
			
		
	def fight_hersheyKisses(player, game, current_width, current_height):
		y = self.monsters_in_house.length
		for x in range(y)
			if type(monster) is not Person:
                self.monsters_in_house[y].health = self.monsters_in_house[y].health - (self.base_attack + 1)
				if self.monsters_in_house[y].health <= 0 :
					self.monsters_in_house[y] = person(self)
				else:	
					self.health = self.health - self.monsters_in_house[y].attack
			else:
				self.health = self.health + 1	
		if self.health <= 0 :
			self.game_over = True;
			print("You died!")
				

	def fight_nerdBombs(player, game, current_width, current_height, input):
		y = self.monsters_in_house.length
		for x in range(y)
			if type(monster) is not Person:
				self.monsters_in_house[y].health = self.monsters_in_house[y].health - (self.base_attack + self.weapons[input].attack)
				if self.monsters_in_house[y].health <= 0 :
					self.monsters_in_house[y] = person(self)
				else:
					else:	
					self.health = self.health - self.monsters_in_house[y].attack
			else: 
				self.health = self.health + 1	
		if self.health <= 0 :
			self.game_over = True;
			print("You died!")

	
	def fight_chocolateBars(player, game, current_width, current_height):
		y = self.monsters_in_house.length
		for x in range(y)
			if type(monster) is not Person:
				self.monsters_in_house[y].health = self.monsters_in_house[y].health - (self.base_attack + self.weapons[input].attack)
				if self.monsters_in_house[y].health <= 0 :
					self.monsters_in_house[y] = person(self)
				else:	
					self.health = self.health - self.monsters_in_house[y].attack
			else:
				self.health = self.health + 1	
		if self.health <= 0 :
			self.game_over = True;
			print("You died!")
			
	def fight_sourStraws(player, game, current_width, current_height):
		y = self.monsters_in_house.length
		for x in range(y)
			if type(monster) is not Person:
				self.monsters_in_house[y].health = self.monsters_in_house[y].health - (self.base_attack + self.weapons[input].attack)
				if self.monsters_in_house[y].health <= 0 :
					self.monsters_in_house[y] = person(self)
				else:	
					self.health = self.health - self.monsters_in_house[y].attack
			else: 
				self.health = self.health + 1
		if self.health <= 0 :
			self.game_over = True;
			print("You died!")
		
		
    def see_contents(self, game, current_width, current_height):
        print("Contents of the house: ")
        for monster in game.grid[current_width][current_height]:
            if type(monster) is Ghoul:
                print("Ghoul")
            elif type(monster) is Vampire:
                print("Vampire")
            elif type(monster) is Werewolf:
                print("Werewolf")
            elif type(monster) is Zombie:
                print("Zombie")
            elif type(monster) is Person:
                print("Person")
            else:
                print("Yourself")

game = Game()
game.init_board()  
player = Player()
game.spawn_player(player, game)
while not game.game_over:
    game.get_user_move(player, game)


#print(game.grid[current_width][current_height])
#print(len(game.grid[current_width][current_height]))

