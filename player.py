import pygame
from constants import *
from bullet import Shot
from circleshape import CircleShape

"""
Even though the player is supposed to look like a triangle,
the code for collision between a triangle and a circle is too
complex to be taught in this course, so the actual player shape
is a circle itself, but the image that we will be displaying
on the screen is a triangle. (We are cheating!)
"""

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]  # triangle positions for drawing the triangle

    def draw(self, screen):
        # draws the shapes, here we are drawing the triangle having no fill, white color, width = 2, on the screen
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, delta):
        self.rotation += PLAYER_TURN_SPEED * delta

    def update(self, delta):
        self.shoot_timer -= delta
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            # this condition is to turn the ship left
            self.rotate(-delta)
        if keys[pygame.K_RIGHT]:
            # this condition is to turn the ship right
            self.rotate(delta)

        if keys[pygame.K_UP]:
            # this codition is to move forward
            self.move(delta)
        if keys[pygame.K_DOWN]:
            # this condition is to move backward
            self.move(-delta)

        if keys[pygame.K_SPACE]:
            # this condition is to shoot bullets
            self.shoot()

    def move(self, delta):
        # Note: delta is actually the amount of time between 2 clock calls
        # and this is used to update the position of all the sprite objects
        # so that they appear smoothly
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta

    def shoot(self):
        if self.shoot_timer > 0: return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

