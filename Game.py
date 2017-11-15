from Neighborhood import *
from Player import * 
from random import randint
#from six.moves import input

class Game:

    def __init__(self):
        self.game_won = False
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
                            'e': 'Enter', 'E': 'Enter'}
        move = input("What would you like to do?")
        if move in possible_moves:
            the_move = possible_moves[move]
            self.movement(player, game, the_move)
        else:
            print("Silly person, that's not a direction")

    def movement(self, player, game, the_move):
        if the_move == 'North' and not self.in_house:
            self.move_north(player, game, self.current_width, self.current_height)
        elif the_move == 'South':
            self.move_south(player, game, self.current_width, self.current_height)
        elif the_move == 'East':
            self.move_east(player, game, self.current_width, self.current_height)
        elif the_move == 'West':
            self.move_west(player, game, self.current_width, self.current_height)
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

game = Game()
game.init_board()  
player = Player()
game.spawn_player(player, game)
while not game.game_won:
    game.get_user_move(player, game)
    



#print(game.grid[current_width][current_height])
#print(len(game.grid[current_width][current_height]))

