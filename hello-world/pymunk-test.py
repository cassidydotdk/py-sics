# Let's run some basic testing of our pymunk base
# Generally speaking, there are 3 types of objects when using pymunk
# - Dynamic: collusions, forces, gravity, finite mass, interacts with all other types
# - Kinematic: Managed in code, no gravity, infinite mass
# - Static: Environment objects, not mobile

import pygame as pg
import pymunk.pygame_util

pymunk.pygame_util.positive_y_is_up = False

RESOLUTION = W, H = 1280, 1024
FPS = 60

pg.init()
surface = pg.display.set_mode(RESOLUTION)
clock = pg.time.Clock()
pg.display.set_caption('Hello World with pymunk physics!')
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = 0, 2000

# Let's drop a ball into our space. This is throwaway code just for testing, don't worry too much right now
ball_mass, ball_radius = 1, 60
ball_momentum = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
ball_body = pymunk.Body(ball_mass, ball_momentum)
ball_body.position = W // 2, 0 # Place ball at the center/top of our space
ball_shape = pymunk.Circle(ball_body, ball_radius)
space.add(ball_body, ball_shape) # Now add it to our physics space
# If you run the code now, you'll see the ball appearing, then dropping off the bottom of our surface
# We need to create a "floor" to catch it

# Create floor to prevent the ball from dropping down and out
# For this we need a static object, with a basic shape
segment_shape = pymunk.Segment(space.static_body, (0, H), (W, H), 20) 
# Shape is a line (segment) starting at 0, H (0,1024) ending at W, H (1280, 1024) with a thickness of 20
space.add(segment_shape)
# If you run the code now, the ball will drop to our new floor and abrubtly stop. CLONK.
# In the real world, all objects would have a certain elasticity to them. Let's add that in

# Add elasticity to ball and floor. Normally I would do this above where the shapes were defined, but 
# doing it here makes it easier for you to introduce the new concepts step by step
segment_shape.elasticity = 0.8
ball_shape.elasticity = 0.8

# Rest of the code is unchanged from previous examples

never_gonna_give_you_up = True

while never_gonna_give_you_up:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            never_gonna_give_you_up = False

    space.step(1/FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(FPS)
