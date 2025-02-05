import sys
import pygame
from constants import *
from bullet import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

# Initialize the pygame module so that all its modules work

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    # Create a new display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game clock for FPS
    game_clock = pygame.time.Clock()

    # Creating 2 groups for updating and drawing
    # and one asteroids group for spawning them
    # and one for all the bullets
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # static or class variables, which are useful when adding property
    # to the class dynamically
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    # asteroid field object
    ast_fld = AsteroidField()

    Player.containers = (updatable, drawable)
    # player object
    plr = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    # asteroid object
    # atr = Asteroid(SCREEN_HEIGHT/3, SCREEN_WIDTH/4, 4)

    # delta
    dt = 0

    # Game loop (which should run so that each frame is calculated and displayed)
    while True:
        for event in pygame.event.get():
           if event.type == pygame.QUIT: return  # make close button work

        # update all the objects present in the group
        updatable.update(dt)

        for astrd in asteroids:
            if astrd.collides_with(plr):
                print("Game over!")
                sys.exit()
            for bt in shots:
                if bt.collides_with(astrd):
                    bt.kill()
                    astrd.split()

        screen.fill((0, 0, 0))

        # draw all the objects present in the group
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()  # screen refresh
        # set frame rate to 60 and return time passed since last call in seconds
        dt =  game_clock.tick(60)/1000


if __name__ == "__main__":
    main()
