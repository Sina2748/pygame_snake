import pygame, sys, random
from pygame.math import Vector2

### Making classes
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,9), Vector2(4,9), Vector2(3,9)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
                       
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (255,255,255), block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, 1200 - 1)
        self.y = random.randint(0, 800 - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x, self.pos.y, cell_size, cell_size)
        pygame.draw.rect(screen, (255,255,255), fruit_rect)

### makeing of the objects
snake = SNAKE()
fruit = FRUIT()

### Makeing the screen
pygame.init() 
cell_number = 10
cell_size = 20
screen =pygame.display.set_mode((cell_number*cell_size*6, cell_number*cell_size*4))

### Events
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

### Main Loop of the game
while True:

    #Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                 snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                 snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                 snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                 snake.direction = Vector2(1,0)

    #Show screen  
    screen.fill((75, 15, 70))

    #Show snake
    snake.draw_snake()

    #Show fruit
    fruit.draw_fruit()

    #STUFF
    pygame.display.update()
    clock.tick(60)

 