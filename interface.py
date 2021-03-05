import pygame    #importing pygame package
import sys       #module helps to manipulate different parts (functions variables)

pygame.init()   #initialize all imported pygame modules

#main interface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
FPS = 20  # frames per second
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ADD_NEW_FLAME_RATE = 25
cactus_img = pygame.image.load('mario/cactus_bricks.png') #load new image from a file
cactus_img_rect = cactus_img.get_rect()  #rect->objects to store and manipulate rectangular areas
cactus_img_rect.left = 0
fire_img = pygame.image.load('mario/fire_bricks.png') ##load new image from a file
fire_img_rect = fire_img.get_rect()  #rect->objects to store and manipulate rectangular areas
fire_img_rect.left = 0
CLOCK = pygame.time.Clock()  #create an object to help track time
font = pygame.font.SysFont('forte', 20)  #return a new font object that is loaded from the system fonts

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  #It actually creates an instance of the pygame
pygame.display.set_caption('Mini-Mario') #get the current window caption

# creating Topscore class
class TopScore:
    def __init__(self):
        self.h_score = 0  # initially high score=0

    def top_score(self, score):
        if score > self.h_score: #check the condition
            self.h_score = score
        return self.h_score
    