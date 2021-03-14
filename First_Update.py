import pygame
import sys

pygame.init()

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

class TopScore_Count:
    def __init__(self):
        self.high_score = 0  # high score

    def top_score_count(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score


topscore = TopScore_Count()

class Dragon_the_Monster:
    velocity_of_dragon = 10

    def __init__(self):
        self.IMAGE_OF_DRAGON = pygame.image.load('mario/dragon.png')  # insert dragon image
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
                self.IMAGE_OF_DRAGON_rect.top -= self.velocity_of_dragon
            elif self.down:
                self.IMAGE_OF_DRAGON_rect.top += self.velocity_of_dragon

#CLASS OF FLAME --->


class Mini_Mario:
    velocity = 10

    def __init__(self):
        self.IMAGE_OF_MARIO = pygame.image.load('mario/maryo.png')
        self.IMAGE_OF_MARIO_rect = self.IMAGE_OF_MARIO.get_rect()
        self.IMAGE_OF_MARIO_rect.left = 20
        self.IMAGE_OF_MARIO_rect.top = INTERFACE_WINDOW_HEIGHT / 2 - 100
        self.down = True
        self.up = False

    def update(self):
        WHOLE_CANVAS.blit(self.IMAGE_OF_MARIO, self.IMAGE_OF_MARIO_rect)
        if self.IMAGE_OF_MARIO_rect.top == IMAGE_OF_CACTUS_rect.bottom:
            game_over()
            if SCORE > self.MARIO_SCORE:
                self.MARIO_SCORE = SCORE
        if self.IMAGE_OF_MARIO_rect.bottom >= IMAGE_OF_FIRE_rect.top:
            game_over()
            if SCORE > self.MARIO_SCORE:
                self.MARIO_SCORE = SCORE
        if self.up:
            self.IMAGE_OF_MARIO_rect.top -= 10
        if self.down:
            self.IMAGE_OF_MARIO_rect.bottom += 10

def game_over():
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
                # music.stop()
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


def check_the_level(SCORE):
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
    elif SCORE > 30:
        IMAGE_OF_CACTUS_rect.bottom = 200
        IMAGE_OF_FIRE_rect.top = INTERFACE_WINDOW_HEIGHT - 200
        LEVEL = 4

def game_loop():
    while True:
        global DRAGON
        DRAGON = Dragon_the_Monster()

        MARIO = Mini_Mario()
        FLAME_COUNTER = 0
        global SCORE
        SCORE = 0
        global HIGH_SCORE
        FLAME_LIST = []

        while True:
            WHOLE_CANVAS.fill(BLACK_INTERFACE)
            check_the_level(SCORE)
            DRAGON.update()
            FLAME_COUNTER += 1

            if FLAME_COUNTER == FLAME_RATE:
                FLAME_COUNTER = 0

            for fl in FLAME_LIST:
                if fl.IMAGE_OF_FLAME_rect.left <= 0:
                    FLAME_LIST.remove(fl)
                    SCORE += 1
                fl.update()

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

                    #---------->

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