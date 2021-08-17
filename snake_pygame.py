import pygame, sys

class SNAKe:
    def __init__(self):
        pass




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
    pygame.display.update()
    clock.tick(60)

"""jhgygyg"""
 