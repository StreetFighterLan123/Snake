import pygame, time, os, sys, random, math

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake")

# Clock
clock = pygame.time.Clock()

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
CREAM = (239,235,216)
RED = (255,0,0) # Make the apple red.

orig_headImg = pygame.image.load('head.png').convert()
#The image is 30 by 30, keep that in mind.
headImg = pygame.transform.scale(orig_headImg, (25,25)) #Now it's 25 by 25

def head(x,y):
        screen.blit(headImg, (x,y))

headX = 400
headY = 300
headX_change = 20
headY_change = 0
head_direction = "Right"

score = 0
font = pygame.font.Font('freesansbold.ttf', 36)

def disp_score():
    score_text = font.render(f'Score: {score}', True, (82,163,99))
    screen.blit(score_text, (345, 10))


def colorize(image, new_color):
    image = image.copy()
    image.fill((0,0,0,255), None, pygame.BLEND_RGBA_MULT)
    image.fill(new_color[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
    return image


original_appleImg = colorize(pygame.image.load('head.png').convert(), RED)
appleImg = pygame.transform.scale(original_appleImg, (20,20))

def apple(x,y):
    screen.blit(appleImg, (x,y))

appleX = random.randint(0,750)
appleY = random.randint(350,550)


def collision():
    global headX
    global headY
    global appleX
    global appleY
    distance = math.sqrt((math.pow(appleX-headX,2)) + (math.pow(appleY-headY,2)))
    if distance < 15:
        return True
    return False

col_sound = pygame.mixer.Sound("apple.wav")
running = True
while running:
        # A white screen is what I'm going to use for now.
        screen.fill((CREAM))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            headX_change = -20
            headY_change = 0
            head_direction = "left"
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            headX_change = 20
            headY_change = 0
            head_direction = "right"
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            headY_change = -20
            headX_change = 0
            head_direction = "up"
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            headY_change = 20
            headX_change = 0
            head_direction = "down"

        # Change the X and Y by their velocities.
        headX += headX_change
        headY += headY_change
        
        # Boundaries.
        if headX > 775:
            headX = 770
        if headX <= 0:
            headX = 5
        if headY >= 575:
            headY = 570
        if headY <= 0:
            headY = 5

        if collision(): # Checks for a collision.
            appleX, appleY = random.randint(0, 790), random.randint(0,590)
            pygame.mixer.Sound.play(col_sound)
            score += 1

        disp_score()
        apple(appleX, appleY)
        head(headX, headY)
        clock.tick(10) # The reason it's 10 FPS is because the original snake game was choppy as the software back then didn't allow for high-fps gaming.
        pygame.display.update()

