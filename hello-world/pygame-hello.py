# Basic 101 of setting up an empty pygame project
import pygame as pg

RESOLUTION = W, H = 1280, 1024
FPS = 60

pg.init()
surface = pg.display.set_mode(RESOLUTION)
clock = pg.time.Clock()
pg.display.set_caption('Hello World!')

never_gonna_give_you_up = True

while never_gonna_give_you_up:
    # Draw whatever
    surface.fill(pg.Color('black'))

    # Listen for events (keyb, mouse, etc)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            never_gonna_give_you_up = False

    # flip the buffers. We're always drawing to the off-screen buffer.
    pg.display.flip()
    clock.tick(FPS)
