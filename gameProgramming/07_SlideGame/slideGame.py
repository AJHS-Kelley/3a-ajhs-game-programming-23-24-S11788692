Number Slide Game, Ryan Kelley, based on project by Al Sweigart, v0.0

# GAME SETUP / STEPS 
# Function to layout / setup the grid. 
# Create the tiles and add to board.  
# Check for Valid Movements 
# Animate movement of tile 
# Allow for user input to select tile (mouse click)
# Identify location coordinates of mouse click, determine tile selected
# Check for Win -- All numbers in correct order. 

# DIVIDE AND CONQUER METHOD -- Break down a larger problem into smaller problems, then solve those. 

# MODULE IMPORTS -- import entire module! 
import pygame, sys, random, time 
# sys module gives access to system level functions including open/close programs, etc.

# MODULE IMPORTS -- specific functions!  
from pygame.locals import * 
# This line allows us to call functions directly instead of pygame.function()
# we can just write function() 
# * in this line is a WILDCARD and means any or all.  
# Example: delete myGameFiles* 


# BOARD SETUP DATA
BOARDWIDTH = 4 # COLUMNS
BOARDHEIGHT = 4 # ROWS

# TILE DATA
TILESIZE = 80 # MEASURED IN PIXELS 

# WINDOW SIZE 
WINDOWWIDTH = 640 # MEASURED IN PIXELS 
WINDOWHEIGHT = 480 # MEASURED IN PIXELS 

# FRAMES PER SECOND 
FPS = 30 # SETS MAXIMUM, DOES NOT 'IMPROVE PERFORMANCE' ON A POTATO 

# BLANK TILE VALUE 
BLANK = None 


# COLOR VALUES = (R, G, B)
# Min. Value = 0, Max. Value = 255, think of drops of food coloring. 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

# ASSIGN COLORS TO GAME OBJECTS
BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE 
BORDERCOLOR = BRIGHTBLUE 

# FONT SIZE
BASICFONTSIZE = 20 # MEASURED IN PIXELS 

# BUTTONS AND MESSAGES
BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK 
MESSAGECOLOR = WHITE

# MARGINS FOR WINDOW 
XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH -1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT -1))) / 2)

# DIRECTIONAL ASSIGNMENTS 
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Main Game Loop 
def main(): 
    # global keyword makes Python use the same variable in entire program.
    global FPSCLOCK, DISPLAYSURF, BASIC_FONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT
    # SURF IS THE ABBREVIATION FOR 'SURFACE' 
    # A 'SURFACE' IN PYGAME CAN BE USED TO DRAW GRAPHICS, TEXT, OR SIMPLE COLORS.  
    # THE EASY WAY TO THINK OF THE 'SURFACE' IS A WHITEBOARD.  

    # RECT IS THE ABBREVIATION FOR RECTANGLE 

    # START THE PYGAME MODULE ITSELF! THIS LINE OF CODE IS REQUIRED FOR PYGAME TO WORK! 

    pygame.init() # Start the PyGame Module
    FPSCLOCK = pygame.time.Clock() # Establish the 'start' to track FPS
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))  # Create the game window.
    pygame.display.set_caption('Ryan\'s Slider Puzzle Game')
    time.sleep(5)


main()

def checkforquit() -> None:
    for event in pygame.event.get(quit):
        terminate()
    For event in pygame.event.get(keyup)
    if event.key == K_ESCAPE:
        terminate()
        pygame.event.post(event)

def getlefttopoftile (tileX: int, tileY: int) -> tuple 
    left = XMARGIN + (tileX * Tilesize) + (tileX - 1)
    top = YMARGIN + (TileY * TILESIZE) + (tileY - 1 )
    return (top,left)

def getspotClick(Board: list, x: int, y: int) -> tuple:
    for tileY in range(len(board[0])):
        left, top + getlefttopoftile(tileX, Tilesize,Tilesize) 
        tilerect =pygame. Rect(left, top, Tilesize, Tilesize)

        if tilerect. collidrpoint(x,y): 
            return (tileX, tileY)
    return (None, None)                                                                                                 