from state_file import state_file

# Module for the CONSTANTS

##### PROGRAM CONSTANTS #####
WIDTH = 1280
HEIGHT = 720

FPS = 60
#############################

##### PLAYER CONSTANTS #####
MAX_SPEED_X = 6
ACCELERATION = 0.5
DECELERATION = 0.5

MAX_SPEED_Y = 12
GRAVITY = 0.75

JUMP_FORCE = 1.7
############################

##### CROCODILE CONSTANTS #####
VELOCITY_X = -5
############################

##### LEVELS TILE MAPS #####
TILE_SIZE = 80
######## MAIN MENU #########
BACKGROUND = state_file("menu_scenario.txt")
######### LEVEL 1 ##########
LEVEL1_S1 = state_file("lvl1 - state1.txt")
LEVEL1_S2 = state_file("lvl1 - state2.txt")

LEVEL1 = [LEVEL1_S1, LEVEL1_S2]
############################
