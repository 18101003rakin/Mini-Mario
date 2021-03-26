# import pygame
import pygame
# provides functions and variables which are used to manipulate different parts of the Python Runtime Environment
import sys

pygame.init()

# making the main window of the game
INTERFACE_WINDOW_WIDTH = 1200
INTERFACE_WINDOW_HEIGHT = 700
FRAME_PER_SECOND = 20
BLACK_INTERFACE = (0, 0, 0)
GREEN_INTERFACE = (0, 255, 0)
FLAME_RATE = 25
IMAGE_OF_CACTUS = pygame.image.load('mario/cactus_bricks.png')
IMAGE_OF_CACTUS_rect = IMAGE_OF_CACTUS.get_rect()
IMAGE_OF_CACTUS_rect.left = 0
IMAGE_OF_FIRE = pygame.image.load('mario/fire_bricks.png')
IMAGE_OF_FIRE_rect = IMAGE_OF_FIRE.get_rect()
IMAGE_OF_FIRE_rect.left = 0
CLOCK_RATE = pygame.time.Clock()
FONT_STYLE = pygame.font.SysFont('forte', 20)

WHOLE_CANVAS = pygame.display.set_mode((INTERFACE_WINDOW_WIDTH, INTERFACE_WINDOW_HEIGHT))
pygame.display.set_caption('Mini-Mario vs. Dragon')


# class for Topscore
class TopScore_Count:
    def __init__(self):
        self.high_score = 0  # high score

    def top_score_count(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score


topscore = TopScore_Count()



# class for the villain
class Dragon_the_Monster:
    velocity_of_dragon = 10 #movement velocity

    def __init__(self):
        self.IMAGE_OF_DRAGON = pygame.image.load('mario/dragon.png')
        self.IMAGE_OF_DRAGON_rect = self.IMAGE_OF_DRAGON.get_rect()
        self.IMAGE_OF_DRAGON_rect.width -= 10
        self.IMAGE_OF_DRAGON_rect.height -= 10
        self.IMAGE_OF_DRAGON_rect.top = INTERFACE_WINDOW_HEIGHT / 2
        self.IMAGE_OF_DRAGON_rect.right = INTERFACE_WINDOW_WIDTH
        self.up = True
        self.down = False

    def update(self):
        WHOLE_CANVAS.blit(self.IMAGE_OF_DRAGON, self.IMAGE_OF_DRAGON_rect)
        if self.IMAGE_OF_DRAGON_rect.top == IMAGE_OF_CACTUS_rect.bottom:
            self.up = False
            self.down = True
        elif self.IMAGE_OF_DRAGON_rect.bottom >= IMAGE_OF_FIRE_rect.top:
            self.up = True
            self.down = False

        if self.up:
            self.IMAGE_OF_DRAGON_rect.top -= self. velocity_of_dragon
        elif self.down:
            self.IMAGE_OF_DRAGON_rect.top += self. velocity_of_dragon


# class for the dragon flame
class Flames_Of_Dragon:
    velocity_of_flames = 20 # flame velocity

    #flame variable
    def __init__(self):
        self.DRAGON_FLAMES = pygame.image.load('mario/fire2.png') # insert flame image
        self.IMAGE_OF_FLAME = pygame.transform.scale(self.DRAGON_FLAMES, (20, 20))
        self.IMAGE_OF_FLAME_rect = self.IMAGE_OF_FLAME.get_rect()
        self.IMAGE_OF_FLAME_rect.right = DRAGON.IMAGE_OF_DRAGON_rect.left
        self.IMAGE_OF_FLAME_rect.top = DRAGON.IMAGE_OF_DRAGON_rect.top + 30

    def update(self):
        WHOLE_CANVAS.blit(self.IMAGE_OF_FLAME, self.IMAGE_OF_FLAME_rect)

        if self.IMAGE_OF_FLAME_rect.left > 0:
            self.IMAGE_OF_FLAME_rect.left -= self.velocity_of_flames


# class for hero Mario
class Mini_Mario:
    velocity = 10       #library function

    def __init__(self):
        self.IMAGE_OF_MARIO = pygame.image.load('mario/maryo.png') #load new image from a file of mario
        self.IMAGE_OF_MARIO_rect = self.IMAGE_OF_MARIO.get_rect()  #rect->objects to store and manipulate rectangular areas
        self.IMAGE_OF_MARIO_rect.left = 20
        self.IMAGE_OF_MARIO_rect.top = INTERFACE_WINDOW_HEIGHT / 2 - 100 #set the window hight
        self.down = True
        self.up = False

    def update(self):
        #set different conditions
        WHOLE_CANVAS.blit(self.IMAGE_OF_MARIO, self.IMAGE_OF_MARIO_rect)
        if self.IMAGE_OF_MARIO_rect.top == IMAGE_OF_CACTUS_rect.bottom:
            game_over()
            if SCORE > self.mario_score:
                self.mario_score = SCORE
        if self.IMAGE_OF_MARIO_rect.bottom >= IMAGE_OF_FIRE_rect.top:
            game_over()
            if SCORE > self.MARIO_SCORE:
                self.MARIO_SCORE = SCORE
        if self.up:
            self.IMAGE_OF_MARIO_rect.top -= 10
        if self.down:
            self.IMAGE_OF_MARIO_rect.bottom += 10

# Mredul
def game_over():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('mario/mario_dies.wav')
    music.play()
    topscore.top_score_count(SCORE)
    IMAGE_OF_GAMEOVER = pygame.image.load('mario/end.png')
    IMAGE_OF_GAMEOVER_rect = IMAGE_OF_GAMEOVER.get_rect()
    IMAGE_OF_GAMEOVER_rect.center = (INTERFACE_WINDOW_WIDTH / 2, INTERFACE_WINDOW_HEIGHT / 2)
    WHOLE_CANVAS.blit(IMAGE_OF_GAMEOVER, IMAGE_OF_GAMEOVER_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                music.stop()
                game_loop()
        pygame.display.update()


def start_the_game():
    WHOLE_CANVAS.fill(BLACK_INTERFACE)
    IMAGE_OF_START_GAME = pygame.image.load('mario/start.png')
    IMAGE_OF_START_GAME_rect = IMAGE_OF_START_GAME.get_rect()
    IMAGE_OF_START_GAME_rect.center = (INTERFACE_WINDOW_WIDTH / 2, INTERFACE_WINDOW_HEIGHT / 2)
    WHOLE_CANVAS.blit(IMAGE_OF_START_GAME, IMAGE_OF_START_GAME_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()


def check_level(SCORE):
    global LEVEL
    if SCORE in range(0, 10):
        IMAGE_OF_CACTUS_rect.bottom = 50
        IMAGE_OF_FIRE_rect.top = INTERFACE_WINDOW_HEIGHT - 50
        LEVEL = 1
    elif SCORE in range(10, 20):
        IMAGE_OF_CACTUS_rect.bottom = 100
        IMAGE_OF_FIRE_rect.top = INTERFACE_WINDOW_HEIGHT - 100
        LEVEL = 2
    elif SCORE in range(20, 30):
        IMAGE_OF_CACTUS_rect.bottom = 150
        IMAGE_OF_FIRE_rect.top = INTERFACE_WINDOW_HEIGHT - 150
        LEVEL = 3
    elif SCORE is 30:
        IMAGE_OF_CACTUS_rect.bottom = 200
        IMAGE_OF_FIRE_rect.top = INTERFACE_WINDOW_HEIGHT - 200
        LEVEL = 4


# Ayesha
def game_loop():
    while True:
        global DRAGON
        DRAGON = Dragon_the_Monster()
        FLAMES = Flames_Of_Dragon()
        MARIO = Mini_Mario()
        FLAME_COUNTER = 0
        global SCORE
        SCORE = 0
        global HIGH_SCORE
        FLAME_LIST = []
        pygame.mixer.music.load('mario/mario_theme.wav')
        pygame.mixer.music.play(-1, 0.0)
        while True:
            WHOLE_CANVAS.fill(BLACK_INTERFACE)
            check_level(SCORE)
            DRAGON.update()
            FLAME_COUNTER += 1

            if FLAME_COUNTER == FLAME_RATE:
                FLAME_COUNTER = 0
                new_flame = Flames_Of_Dragon()
                FLAME_LIST.append(new_flame)
            for f in FLAME_LIST:
                if f.IMAGE_OF_FLAME_rect.left <= 0:
                    FLAME_LIST.remove(f)
                    SCORE += 1
                f.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        MARIO.up = True
                        MARIO.down = False
                    elif event.key == pygame.K_DOWN:
                        MARIO.down = True
                        MARIO.up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        MARIO.up = False
                        MARIO.down = True
                    elif event.key == pygame.K_DOWN:
                        MARIO.down = True
                        MARIO.up = False

            FONT_OF_SCORE = FONT_STYLE.render('Score:' + str(SCORE), True, GREEN_INTERFACE)
            FONT_OF_SCORE_rect = FONT_OF_SCORE.get_rect()
            FONT_OF_SCORE_rect.center = (200, IMAGE_OF_CACTUS_rect.bottom + FONT_OF_SCORE_rect.height / 2)
            WHOLE_CANVAS.blit(FONT_OF_SCORE, FONT_OF_SCORE_rect)

            FONT_OF_LEVEL = FONT_STYLE.render('Level:' + str(LEVEL), True, GREEN_INTERFACE)
            FONT_OF_LEVEL_rect = FONT_OF_LEVEL.get_rect()
            FONT_OF_LEVEL_rect.center = (500, IMAGE_OF_CACTUS_rect.bottom + FONT_OF_SCORE_rect.height / 2)
            WHOLE_CANVAS.blit(FONT_OF_LEVEL, FONT_OF_LEVEL_rect)

            FONT_OF_TOPSCORE = FONT_STYLE.render('Top Score:' + str(topscore.high_score), True, GREEN_INTERFACE)
            FONT_OF_TOPSCORE_rect = FONT_OF_TOPSCORE.get_rect()
            FONT_OF_TOPSCORE_rect.center = (800, IMAGE_OF_CACTUS_rect.bottom + FONT_OF_SCORE_rect.height / 2)
            WHOLE_CANVAS.blit(FONT_OF_TOPSCORE, FONT_OF_TOPSCORE_rect)

            WHOLE_CANVAS.blit(IMAGE_OF_CACTUS, IMAGE_OF_CACTUS_rect)
            WHOLE_CANVAS.blit(IMAGE_OF_FIRE, IMAGE_OF_FIRE_rect)
            MARIO.update()
            for f in FLAME_LIST:
                if f.IMAGE_OF_FLAME_rect.colliderect(MARIO.IMAGE_OF_MARIO_rect):
                    game_over()
                    if SCORE > MARIO.mario_score:
                        MARIO.mario_score = SCORE
            pygame.display.update()
            CLOCK_RATE.tick(FRAME_PER_SECOND)


start_the_game()