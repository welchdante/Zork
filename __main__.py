from Neighborhood import *
from Game import *

def main():
    game = Game()
    game.init_board()  
    player = Player()
    player.gen_weapons(player.weapons)
    game.spawn_player(player)
    game.instructions()

    while not game.game_over:
        game.get_user_move(player)


if __name__ == "__main__":
    main()
