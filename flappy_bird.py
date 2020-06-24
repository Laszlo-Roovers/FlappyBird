"""Program that uses machine learning to play the popular game Flappy Bird.

Author: Lászlo Roovers
Date: 24-06-2020

This project was made out of personal interest and has been developed as a way
for me to learn ML. It may be very inefficient and full of bad practices as a
result.
"""

import pygame
import neat
import time
import os
import random

from bird import Bird
from pipe import Pipe

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIN_WIDTH = 500
WIN_HEIGHT = 800

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

def draw_window(win, bird) -> None:
    """Draw the current window to the screen."""
    win.blit(BG_IMG, (0,0))
    bird.draw(win)
    pygame.display.update()

def main() -> None:
    """Run main game loop."""
    bird = Bird(200, 200)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    # Control variable for main loop.
    run = True

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        bird.move()
        draw_window(win, bird)

    pygame.quit()
    quit()


# Call main game loop to be start
main()
