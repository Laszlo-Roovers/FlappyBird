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

from bird import Bird
from pipe import Pipe
from base import Base

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIN_WIDTH = 500
WIN_HEIGHT = 800

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

def draw_window(win, bird, pipes, base) -> None:
    """Draw the current window to the screen."""
    win.blit(BG_IMG, (0,0))
    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)

    bird.draw(win)
    pygame.display.update()

def main() -> None:
    """Run main game loop."""
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    score = 0

    # Control variable for main loop.
    run = True

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        bird.move()
        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(bird):
                pass

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()

        if add_pipe:
            score += 1
            pipes.append(Pipe(700))

        for r in rem:
            pipes.remove(r)

        base.move()
        draw_window(win, bird, pipes, base)

    pygame.quit()
    quit()


# Call main game loop to be start
main()
