from Home import *
from pprint import pprint

class Neighborhood:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    #creates the grid
    def make_grid(self, rows, cols):
        grid = []
        for row in range(rows): grid += [[0]*cols]
        return grid

    #fills the location with a home
    def fill_location(self, location):
        home = Home()
        monsters = home.gen_monsters()
        return monsters
    
    #fills each location with a home
    def fill_neighborhood(self, grid):
        i=0
        j=0
        while (i < len(grid)):
            while(j < len(grid[i])):
                grid[i][j] = self.fill_location(grid[i][j])
                j = j + 1
            j = 0
            i = i + 1
        return grid

