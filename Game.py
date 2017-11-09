from Neighborhood import *
from Player import * 

class Game:

    def __init__(self):
        self.x = 0

    def init_board(self):
        neighborhood = Neighborhood(4, 4)
        grid = neighborhood.make_grid(neighborhood.height, neighborhood.width)
        grid = neighborhood.fill_neighborhood(grid)
        pprint(grid)
    

game = Game()
game.init_board()  
#player = Player()      
