# Now let's try and bring together what we've learned and have a bit of fun
import pygame as pg
import pymunk.pygame_util
# We're going to need some random numbers
from random import randrange

pymunk.pygame_util.positive_y_is_up = False

RESOLUTION = W, H = 1280, 1024
FPS = 60

# pygame
pg.init()
surface = pg.display.set_mode(RESOLUTION)
clock = pg.time.Clock()
pg.display.set_caption('Fun with pygame and pymonk!')

#pymunk
draw_options = pymunk.pygame_util.DrawOptions(surface)
space = pymunk.Space()
space.gravity = 0, 2000

segment_shape = pymunk.Segment(space.static_body, (0, H), (W, H), 20) 
segment_shape.elasticity = 0.8
segment_shape.friction = 0.5    # surface friction. A value of 0 means, objects will interact without influencing eachother at all
space.add(segment_shape)

# Moved the ball creation into a method of its own. So we can easily make many more.
def create_ball(space, pos, radius=60):
    ball_mass, ball_radius = radius/5, radius
    ball_momentum = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_momentum)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.8
    ball_shape.friction = 0.5
    ball_shape.color = (randrange(0,255), randrange(0,255), randrange(0,255), 255)
    space.add(ball_body, ball_shape)

# Main Loop

never_gonna_give_you_up = True

while never_gonna_give_you_up:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            never_gonna_give_you_up = False

        # When user clicks left mouse button, a ball of random size and color is spawned on the location
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1: # button 1?  (left)
                create_ball(space, i.pos, randrange(10, 80))

    space.step(1/FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(FPS)
