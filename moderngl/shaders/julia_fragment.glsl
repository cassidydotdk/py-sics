#version 430

out vec4 fragColour; // glsl doesn't care what this is called, it just expects a vec4 output argument

uniform vec2 c;
uniform vec2 resolution;
uniform int max_iterations = 100;

void main() {
    // calculate UV coordinates, normalised to the current window resolution
    vec2 uv = (gl_FragCoord.xy - 0.5 * resolution.xy) /  resolution.y;

    vec2 z;
    z.x = 3.0 * uv.x;
    z.y = 3.0 * uv.y;

    int i;
    for (i=0; i < max_iterations; i++) 
    {
        float x = (z.x * z.x - z.y * z.y) + c.x;
        float y = (z.x * z.y + z.x * z.y) + c.y;

        if ((x * x + y * y) > 20.0) break;
        z.x = x;
        z.y = y;
    }

    float val = float(i) * 0.05;
    fragColour = vec4(1. - val, 1. - val, 1. - val, 1);
}