from Neighborhood import *
from Player import * 

class Game:

    def __init__(self):
        self.game_won = False


    def init_board(self):
        neighborhood = Neighborhood(2, 2)
        grid = neighborhood.make_grid(neighborhood.height, neighborhood.width)
        grid = neighborhood.fill_neighborhood(grid)
        pprint(grid)

    #def get_game_state():


game = Game()
game.init_board()  
player = Player()      



