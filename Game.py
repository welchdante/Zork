from Neighborhood import *
from Player import * 
from random import randint
#from six.moves import input

class Game:

    def __init__(self):
        self.game_won = False

    def init_board(self):
        self.neighborhood = Neighborhood(2, 2)
        self.grid = self.neighborhood.make_grid(self.neighborhood.height, self.neighborhood.width)
        self.grid = self.neighborhood.fill_neighborhood(self.grid)
        #pprint(self.grid)

    def spawn_player(self, player, game):
        rand_width = randint(0, game.neighborhood.width - 1)
        rand_height = randint(0, game.neighborhood.height - 1)
        pprint("Contents in the home")
        game.grid[rand_width][rand_height].append(player)
        pprint(game.grid[rand_width][rand_height])

    def get_user_move(self, player, game):
        
        possible_moves = {'w': 'North', 's': 'South', 'd': 'East', 'a': 'West', 
                            'W': 'North', 'S': 'South', 'D': 'East', 'A': 'West'}
        move = input("Which way?")
        print(move)
        if move in possible_moves:
            the_move = possible_moves[move]
            self.movement(player, game, the_move)
        else:
            print("Silly person, that's not a direction")

    def movement(self, player, game, the_move):
        if the_move == 'North':
            print("Moving north")
        elif the_move == 'South':
            print("Moving south")
        elif the_move == 'East':
            print("Moving east")
        elif the_move == 'West':
            print("Moving west")
        else:
            print("Invalid move")

    #def get_current_tile(self, player, game):
    #    pprint(game.grid[current_width][current_height])

game = Game()
game.init_board()  
player = Player()
game.spawn_player(player, game)
game.get_user_move(player, game)


