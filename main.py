import pygame, time, os, sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake")

# Clock
clock = pygame.time.Clock()

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

headImg = pygame.image.load('head.png').convert()
def head(x,y):
        screen.blit(headImg, (x,y))

headX = 400
headY = 300
headX_change = 0
headY_change = 0

running = True
while running:
        # A white screen is what I'm going to use for now.
        screen.fill((WHITE))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            headX_change = -20
            headY_change = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            headX_change = 20
            headY_change = 0
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            headY_change = -20
            headX_change = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            headY_change = 20
            headX_change = 0

        # Change the X and Y by their velocities.
        headX += headX_change
        headY += headY_change
        
        #Boundaries.
        if headX > 770:
            headX = 765
        if headX <= 0:
            headX = 5
        if headY >= 570:
            headY = 565
        if headY <= 0:
            headY = 5

        head(headX, headY)
        clock.tick(10) # The reason it's 10 FPS is because the original snake game was choppy as the software back then didn't allow for high-fps gaming.
        pygame.display.update()

