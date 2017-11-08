from Home import *
from pprint import pprint

class Neighborhood:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        #self.generate_neighborhood(height, width)

    def generate_neighborhood(self, width, height):
        board = [["*" for i in range(width)] for i in range(height)]
        return board

    def print_board(self, board):
        for row in board:
            for i in row:
                print(i),
            print("")
    
    def fill_home():
        print("call fill home in a for loop") 

    def fill_neighborhood(self, home, board, width, height):
        print("don't know yet")

neighborhood = Neighborhood(4, 4)
board = neighborhood.generate_neighborhood(4,4)
neighborhood.print_board(board)
home = Home()
neighborhood.fill_neighborhood(home, neighborhood , neighborhood.width, neighborhood.height)
#print()
#print()
#monsters = home.gen_monsters()
#board[0][0] = monsters


