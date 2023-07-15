# Basics of getting taichi up and running
# in your shell, run "pip install taichi"
import taichi as ti

# Initialise taichi, telling it to run on our GPU when possible
ti.init(arch=ti.gpu)

# We'll be rendering in a rectangle of size dim*2, dim
dim = 768

# A few basic parameters for the Julia calculation
# The number of iterations you can do will largely depends
# on the architecture Taichi can use behind the scenes.
# In other words, the capabilities of your graphics card
# I run on a GTX 4090 and have no issues at all, but adjust
# this to fit your setup. Lower is less detail but lighter on resources
max_iterations = 100 # increase for higher level of detail
timestep = 0.0075 # increase for faster animation

# Create an array to hold our pixels. We tell taichi to create it,
# as a taichi 'field'. Basically an array that can be accessed
# from both "python memory" and "taichi memory"
pixels = ti.field(dtype=float, shape=(dim*2, dim))

# Now we need the heart of it all, the calculation of the Julia set
# We define this as a ti function, as we want this function to 
# run on the GPU in parallel, on a per-pixel basis.
# I'll not cover in-depth here, how Julia is calculated. If
# you're curious; check https://www.karlsims.com/julia.html

# We instruct python and taichi about this, with the following decorator
@ti.func
def complex_sqr(z):
    return ti.Vector([z[0] ** 2 - z[1] ** 2, z[1] * z[0] * 2])

# And then we need the main loop, setting up taichi to loop
# over our array of pixels. Explaining taichi kernels in-depth
# will quickly break scope for this example. It helps to think
# of it as code that runs natively, fast, and possibly directly
# on the GPU when applicable.

# again, we need a decorator. This time we need the taichi kernel
@ti.kernel
def draw(t: float):
    # now we loop over our pixels/field. This is parallelized.
    for i, j in pixels:
        c = ti.Vector([-0.8, ti.cos(t) * 0.2])
        z = ti.Vector([i / dim - 1, j / dim - 0.5]) * 2
        iterations = 0
        while z.norm() < 20 and iterations < max_iterations:
            z = complex_sqr(z) + c
            iterations += 1
        pixels[i, j] = 1 - iterations * 0.02

def main():
    gui = ti.GUI("Fun with Julia", res=(dim*2, dim))
    t = 0.0

    while not gui.get_event(ti.GUI.ESCAPE, ti.GUI.EXIT):
        draw(t)
        t += timestep
        gui.set_image(pixels)
        gui.show()

if __name__ == "__main__":
    main()
