"""

This is my first pygame project from book 'Making Games with Python & Pygame'
Enjoiy!

"""

#   Import block

import pygame
import numpy as np


#   Initializing important hyperparameters

FPS = 30                                        # frames per second, the general speed of program
WINDOWWIDTH, WINDOWHEIGHT = 640, 480            # game space params
REVEALSPEED = 8                                 # speed boxes' sliding reveals and covers
BOXSIZE = 40                                    # size of box height & width in pixels
GAPSIZE = 10                                    # size of gap between boxes in pixels
BOARDWIDTH = 10                                 # number of columns of icons
BOARDHEIGHT = 7                                 # number of rows of icons

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)       # abscissa axis border margin width
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)     # ordinate axis border margin width


#   Initializing colors variables

GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BGCOLOR = NAVYBLUE      # background color
LIGHTBGCOLOR = GRAY     # light color
BOXCOLOR = WHITE        # box color
HIGHLIGHTCOLOR = BLUE   # highlight color


#   Initializing string path / description for figures

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'


#   Collecting objects together

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)


#   Okay, let's rock

def main():

    """

    Main function to call

    :return:
    """

    global FPSCLOCK, DISPLAYSURF                                        # initializing  global variables

    pygame.init()

    FPSCLOCK = pygame.time.Clock()                                      # creating a clock object to operate fewer
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))  # creating a display object

    mainBoard = getRandomizedBoard()                                    # generating distribution of objects
    revealedBoxes = generateRevealedBoxesData(False)                    # set object's visibility status


def getRandomizedBoard():

    """

    Description
    ____


    Creates a NxM matrix filled with object to interact with during the game – colored squares with different figures


    Return
    ____

    * result: array-like | NxM matrix with game objects

    """

    n_unique_combinations = int(BOARDHEIGHT * BOARDWIDTH / 2)

    combinations_array = np.vstack(np.transpose(np.meshgrid(ALLCOLORS, ALLSHAPES)))
    np.random.shuffle(combinations_array)
    combinations_array = combinations_array[: n_unique_combinations]
    combinations_array = np.vstack((combinations_array, combinations_array))
    np.random.shuffle(combinations_array)

    result_matrix = np.split(combinations_array, BOARDWIDTH)

    return result_matrix


def generateRevealedBoxesData(bool_val):

    """

    Description
    ____


    Generate an array represents which blocks are covered


    Return
    ____

    * result: array-like | NxM matrix

    """

    return np.full((BOARDWIDTH, BOARDHEIGHT), bool_val)

