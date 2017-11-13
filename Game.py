from Neighborhood import *
from Player import * 
from random import randint

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

    #def get_game_state():

    def move_north(self, player, game):
        print("North")

    def move_south(self, player, game):
        print("South")

    def move_east(self, player, game):
        print("East")

    def move_west(self, player, game):
        print("West")

game = Game()
game.init_board()  
player = Player()
game.spawn_player(player, game)      



