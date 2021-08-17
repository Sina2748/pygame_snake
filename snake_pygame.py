import pygame, sys
from pygame.math import Vector2
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,9), Vector2(4,9), Vector2(3,9)]
        self.direction = Vector2(-1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
                       
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (255,255,255), block_rect)

snake = SNAKE()
  
pygame.init() 
cell_number = 10
cell_size = 20

screen =pygame.display.set_mode((cell_number*cell_size*6, cell_number*cell_size*4))
clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill((75, 15, 70))
    snake.draw_snake()


    pygame.display.update()
    clock.tick(60)

 