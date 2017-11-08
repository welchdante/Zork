from Home import *
from pprint import pprint

class Neighborhood:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def make_grid(self, rows, cols):
        grid = []
        for row in xrange(rows): grid += [[0]*cols]
        return grid

    #def print_board(self, board):
    #    for row in board:
    #        for i in row:
    #            print(i),
    #        print("")
    
    def fill_location(self, location):
        print("Fills a single location")

    def fill_neighborhood(self, grid):
        i=0
        j=0
        while (i < len(grid)):
            while(j < len(grid[i])):
                grid[i][j] = 4
                j = j + 1
            j = 0
            i = i + 1
        return grid
        
        #for row in range(len(grid)):
        #    pprint(row)
        #    for item in range(row):
        #        grid[row][item] = 8              
        #return grid

neighborhood = Neighborhood(4, 4)
grid = neighborhood.make_grid(neighborhood.height, neighborhood.width)
grid = neighborhood.fill_neighborhood(grid)
pprint(grid)

#board = neighborhood.generate_neighborhood(4,4)
#neighborhood.print_board(board)
#neighborhood.fill_neighborhood(board, neighborhood.width, neighborhood.height)
#neighborhood.fill_neighborhood(home, neighborhood, neighborhood.width, neighborhood.height)

#print()
#print()
#monsters = home.gen_monsters()
#board[0][0] = monsters


