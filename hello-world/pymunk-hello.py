# Extending the base pygame project with pymunk physics engine
# Since we're not actually DOING anything with the physics engine yet, this will be relatively underwhelming
import pygame as pg
import pymunk.pygame_util

# Pygame by default uses a screen oriented coordinate system, where 0,0 is the top left corner and increasing
# Y moves you down the screen

# Pymonk uses a natural coordinate system, where 0,0 is at the bottom left and increasing
# Y moves you up the screen

# We need to tell pymonk, literally, what's considered "up" in our world
pymunk.pygame_util.positive_y_is_up = False

RESOLUTION = W, H = 1280, 1024
FPS = 60

pg.init()
surface = pg.display.set_mode(RESOLUTION)
clock = pg.time.Clock()
pg.display.set_caption('Hello World with pymunk physics!')

# We need to tell pymonk what surface we're rendering to
draw_options = pymunk.pygame_util.DrawOptions(surface)

# Now to configure basic pymonk settings. All physics happen inside pymonk "Space"
space = pymunk.Space()
# pymunk is unit-less. Don't worry too much about these values for now
space.gravity = 0, 2000

never_gonna_give_you_up = True

while never_gonna_give_you_up:
    # Draw whatever
    surface.fill(pg.Color('black'))

    # Listen for events (keyb, mouse, etc)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            never_gonna_give_you_up = False

    # Now we advance the physics engine
    space.step(1/FPS)
    # And let's take a look at the calculated result
    space.debug_draw(draw_options)

    # flip the buffers. We're always drawing to the off-screen buffer.
    pg.display.flip()
    clock.tick(FPS)
