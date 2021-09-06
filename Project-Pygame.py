import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# For background image
background = pygame.image.load('5525305.jpg')
background = pygame.transform.scale(background, (800, 600))

# Background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and icon
pygame.display.set_caption("Just a game")
icon = pygame.image.load('arcade-game.png')
pygame.display.set_icon(icon)

# Adding player
playerImg = pygame.image.load("space-invaders.png")
playerx = 370
playery = 480
playerx_change = 0

# Adding enemy / multiple enemies
enemyImg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ghost.png'))
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))

    # increase the speed based upon your needs
    enemyx_change.append(1)
    enemyy_change.append(40)

# Adding bullet
bulletImg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 5

# Ready state - you can't see bullet on screen
# Fire state - bullet moving currently
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textx = 10
texty = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 68)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200,250))

# x and y coordinate for score
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))


def player(x, y):
    # blt == draw
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))


def isCollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
    if distance < 27:
        return True
    else:
        return False


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
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    # Get the current x coordinate of the spaceship
                    bulletx = playerx
                    fire_bullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    playerx += playerx_change

    # Enemy movement
    for i in range(num_of_enemies):
        # Game Over
        if enemyy[i]> 440:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 1
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -1
            enemyy[i] += enemyy_change[i]

        # Collision
        collision = isCollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            # Reset the bullet
            bulletY = 480
            bullet_state = "ready"
            score_value += 1

            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)
        enemy(enemyx[i], enemyy[i], i)

    # Bullet movement
    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change

    # Creating boundries for player
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    player(playerx, playery)
    show_score(textx, texty)

    pygame.display.update()
