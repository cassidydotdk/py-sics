#version 430

out vec4 fragColour; // glsl doesn't care what this is called, it just expects a vec4 output argument

void main() {
    vec3 col = vec3(1.0, 1.0, 0.0);

    fragColour = vec4(col, 1.0);
}