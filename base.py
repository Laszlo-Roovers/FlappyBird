import pygame
from os import path

class Base:
    """Model of the ground-base of the game."""

    BASE_IMG = pygame.transform.scale2x(pygame.image.load(path.join("imgs", "base.png")))
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG
    VEL = 5

    def __init__(self, y):
        """Initialize base's attributes."""
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        """Make base move left, creating illusion of bird flying to the right."""
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        """Draw the base to the screen."""
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
