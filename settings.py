import pygame as pg
pg.mixer.init()

WIDTH, HEIGHT = 500, 600

# Colors
# Primary Colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
SAND = (255, 255, 100)

FPS = 120

GRAVITY = 0.22
SAND_HEIGHT = 50

JUMP_VELOCITY = -7
TUBE_VELOCITY = -1
TUBE_WIDTH = 100
SKY_WIDTH = 5
TUBE_GAP = 150

bird_img = pg.image.load("images/bird1.png")
BIRD_SIZE = bird_img.get_size()

POPULATION = 100

INPUT_LAYER = 5
HIDDEN_LAYER = 4
OUTPUT_LAYER = 1
TOTAL_WEIGHT = (INPUT_LAYER+1)*(HIDDEN_LAYER+1) + (HIDDEN_LAYER+1)*OUTPUT_LAYER

THRESHOLD = 0.5

FITNESS_RATE = 1

MUTATION_RATE = 0.7
CROSSOVER_RATE = 0.6
SELECTION_RATE = 0.15 #0.10

SELECTION_PERCENTAGE = 0.1
MUTATION_PERCENTAGE = 0.55 #0.60
CROSSOVER_PERCENTAGE = 0.15 #0.10
#RANDOM_RATE = 0.20

Background = pg.image.load("images/background.png")
StartScreen = pg.image.load("images/StartScreen.jpg")