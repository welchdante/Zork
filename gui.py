import pygame
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 70
HEIGHT = 70

MARGIN = 18

grid = []
for row in range(8):
    grid.append([])
    for column in range(10):
        grid[row].append(0)  
 
pygame.init()

WINDOW_SIZE = [900, 900]
display_width = 900
display_height = 720
screen = pygame.display.set_mode(WINDOW_SIZE)
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Array Backed Grid")
 
done = False

houseImg = pygame.image.load('house.png')
playerImg = pygame.image.load('lahey.png')

x =  (250)
y = (250)
x_change = 0


def house(x, y):
    gameDisplay.blit(houseImg, (x,y))

def player(x, y):
    gameDisplay.blit(playerImg, (x,y))

def place_player_x(x):
    start_x = randint(0, 9)

def place_player_y(y):
    start_y = randint(0,7)

clock = pygame.time.Clock()

while not done: 
    screen.fill(BLACK)
    
    for row in range(8):
        for column in range(10):
            color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            house((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            done = True  
        if event.type is pygame.KEYDOWN:
            print("hey")   
            if event.key is pygame.K_a:
                    x_change = -85
            elif event.key is pygame.K_d:
                    x_change = 85
        if event.type is pygame.KEYUP:
            print("keyup")
            if event.key is pygame.K_a or event.key is pygame.K_d:
                x_change = 0

    x += x_change
    player(x, y)     

    clock.tick(10)

    pygame.display.flip()

pygame.quit()