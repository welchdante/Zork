from Neighborhood import *

def setup():
    neighborhood = Neighborhood(4, 4)
    grid = neighborhood.make_grid(neighborhood.height, neighborhood.width)
    grid = neighborhood.fill_neighborhood(grid)
    pprint(grid)


def main():
    setup()

if __name__ == "__main__":
    main()