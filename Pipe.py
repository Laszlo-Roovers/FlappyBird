import pygame

class Pipe:
    """Representation of a pipe."""
    GAP = 200
    VEL = 5
    PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
    

    def __init__(self, x):
        """Initialize pipe's attributes."""
        self.x = x
        self.height = 0
        self.gap = 100

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG)
