# This file was created by: Chris Cozort
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# Game # game settings 
WIDTH = 360
HEIGHT = 480
FPS = 60
SCORE = 0

# player settings
PLAYER_JUMP = 20
PLAYER_GRAV = 1.5
global PLAYER_FRIC
PLAYER_FRIC = 0.3

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, " "),
                 (130, HEIGHT/10, 100, 20, " "),
                 (0 - 50, HEIGHT * 3/4, 100, 20, "moving"), 
                 (125, HEIGHT - 200, 75, 20, "moving"),
                 (175, 100, 25, 20, "moving"),
                 (25, 175, 50, 20, "moving")]