import pygame
from os import path
import bird

class Pipe:
    """Representation of a pipe."""

    GAP = 200
    VEL = 5
    PIPE_IMG = pygame.transform.scale2x(pygame.image.load(path.join("imgs", "pipe.png")))

    def __init__(self, x: int) -> None:
        """Initialize pipe's attributes."""
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.set_height()

    def set_height(self) -> None:
        """Set a randomly generated position for a set of pipes."""
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self) -> None:
        """Make the pipes go to the left, creating the illusion of bird flying
        to the right all the time."""
        self.x -= self.VEL

    def draw(self, win) -> None:
        """Draw pipes to the screen."""
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird: Bird) -> bool:
        """Handle collisions pixel-perfectly instead of naively with rects."""
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True

        return False
