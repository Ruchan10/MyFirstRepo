import pygame
import random

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# For background image
background = pygame.image.load('5525305.jpg')
background = pygame.transform.scale(background, (800, 600))


# Title and icon
pygame.display.set_caption("Just a game")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# Adding player
playerImg = pygame.image.load("snakeplayer.png")
playerx = 370
playery = 480
playerx_change = 0

# Adding enemy
enemyImg = pygame.image.load('ghost.png')
enemyx = random.randint(0, 800)
enemyy = random.randint(50, 150)

# Speed of enemy
enemyx_change = 0.2
enemyy_change = 40

# Adding bullet
bulletImg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 3

bullet_state = "ready"


def player(x, y):
    # blt == draw
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

# Game loop
running = True

while running:
    # Color for background window
    screen.fill('grey67')

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed whether its right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                # Increase to 0.3 if u want to increase the speed
                playerx_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
            if event.key == pygame.K_SPACE:
                fire_bullet(playerx, bullety)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    playerx += playerx_change

    # Enemy movement
    enemyx += enemyx_change

    # Bullet movement
    if bullet_state is "fire":
        fire_bullet(playerx, bullety)
        bullety -= bullety_change

    # Creating boundries for enemy
    if enemyx <= 0:
        enemyx_change = 0.2
        enemyy += enemyy_change
    elif enemyx >= 736:
        enemyx_change = -0.2
        enemyy += enemyy_change


    # Creating boundries for player
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    player(playerx, playery)

    enemy(enemyx, enemyy)

    pygame.display.update()
