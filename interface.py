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


# class for hero Mario
class Mini_Mario:
    velocity = 10       #library function

    def __init__(self):
        self.mario_img = pygame.image.load('mario/maryo.png') #load new image from a file of mario
        self.mario_img_rect = self.mario_img.get_rect()  #rect->objects to store and manipulate rectangular areas
        self.mario_img_rect.left = 20
        self.mario_img_rect.top = WINDOW_HEIGHT / 2 - 100 #set the window hight
        self.down = True
        self.up = False

    #update fuction for checking mario
    def update(self):
        #set different conditions
        canvas.blit(self.mario_img, self.mario_img_rect)
        if self.mario_img_rect.top == cactus_img_rect.bottom: #check condition
            game_over() #call game_over function
            if SCORE > self.mario_score:  #check condition
                self.mario_score = SCORE
        if self.mario_img_rect.bottom >= fire_img_rect.top:  #check condition
            game_over()   #call game_over function
            if SCORE > self.mario_score:  #check condition
                self.mario_score = SCORE
        if self.up:
            self.mario_img_rect.top -= 10
        if self.down:
            self.mario_img_rect.bottom += 10

class Dragon:
    velocity_of_dragon = 10  # movement velocity

    # variables for Dragon
    def __init__(self):
        self.img_of_dragon = pygame.image.load('mario/dragon.png')  # insert dragon image
        self.dragon_img_rect = self.img_of_dragon.get_rect()
        self.dragon_img_rect.width -= 10
        self.dragon_img_rect.height -= 10
        self.dragon_img_rect.top = WINDOW_HEIGHT / 2
        self.dragon_img_rect.right = WINDOW_WIDTH
        self.up = True
        self.down = False

    # set the movement conditions of dragon
    def update(self):
        canvas.blit(self.img_of_dragon, self.dragon_img_rect)
        if self.dragon_img_rect.top == cactus_img_rect.bottom:
            self.up = False
            self.down = True
        elif self.dragon_img_rect.bottom >= fire_img_rect.top:
            self.up = True
            self.down = False

        if self.up:
            self.dragon_img_rect.top -= self. velocity_of_dragon
        elif self.down:
            self.dragon_img_rect.top += self. velocity_of_dragon
