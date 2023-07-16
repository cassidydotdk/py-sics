import moderngl_window as mglw

# Create our main class that will interact with ModernGL
class Main(mglw.WindowConfig):
    gl_version = 4, 3
    window_size = 1920, 1080
    resource_dir = 'shaders'
    title = "Hello World from ModernGL_Window!"
    resizable = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Now we need a quad. It will be a basic rectangle covering
        # our entire screen/display area
        self.quad = mglw.geometry.quad_fs()

        # And hen we load our shaders
        self.prog = self.load_program(vertex_shader='hello_vertex.glsl',
                                      fragment_shader='hello_fragment.glsl')
        
    # render will be called on each frame
    def render(self, time, frame_time):
        # Clear framebuffer
        self.ctx.clear()

        # Then we render our quad using the shaders we have loaded
        self.quad.render(self.prog)

if __name__ == '__main__':
    mglw.run_window_config(Main)
