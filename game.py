# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Loading assets
pipe = pygame.image.load("pipe.png").convert
bg = pygame.image.load("bg.jpg").convert()
bg = pygame.transform.scale(bg, (1280, 720))

# Setting the original positions of the backgrounds
bgX = 0
bgX2 = bg.get_width()

# Starting constants for bird (position, speed and gravity)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0.3
gravity = 5

# This redraws the background based on the variable bgX values
def redrawWindow():
    screen.blit(bg, (bgX, 0))
    screen.blit(bg, (bgX2, 0))
    # Draw the player
    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.display.update()

# Start the game loop
running = True

while running:

    # poll for events
    # Quit if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Redraw the window and change the position of the background for the next iteration
    redrawWindow()
    bgX -= 1.4
    bgX2 -= 1.4

    # If our bg is at the -width then reset its position
    if bgX < bg.get_width() * -1: 
        bgX = bg.get_width()
    
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()


    # Make the player fall due to gravity
    player_pos.y += gravity

    #screen.blit(pygame.transform.scale(pipe, (64, 64)), pygame.Vector2(100, 656))

    # If space is pressed, make the bird fly
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_pos.y -= 75 * dt

    # flip() the display to put the work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)  
    

pygame.quit()
