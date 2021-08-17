import pygame, sys, random
from pygame.math import Vector2

### Making classes
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,9), Vector2(4,9), Vector2(3,9)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
                       
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (255,255,255), block_rect)

    def move_snake(self):
        if self.new_block == False: 
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
        else:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False

    def add_block(self):
        self.new_block = True
     


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (255,255,255), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, 20 - 1)
        self.y = random.randint(0, 20 - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        #making objects
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.snake.add_block()
            self.fruit.randomize()


main = MAIN()
### Makeing the screen
pygame.init() 
cell_number = 20
cell_size = 40
screen =pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))

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
            main.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                 main.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                 main.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                 main.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                 main.snake.direction = Vector2(1,0)

    #Show screen  
    screen.fill((75, 15, 70))

    #Show 
    main.draw_elements()

    #STUFF
    pygame.display.update()
    clock.tick(60)

 