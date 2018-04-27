import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

program = 0

VERTEX_SHADER_CODE = """
    #version 120
    
    void main(){
        gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    }
"""
FRAGMENT_SHADER_CODE = """
    #version 120
    
    const float height = 720, width = 1280;
    const int max_iteration = 1000;
    uniform float theta;
    
    void main(){
        //LENS FLARE
        
        float t = theta;
        vec2 r = vec2(width, height);

        vec3 c;
        float l, z = t;
        for(int i = 0; i < 3 ; i++) {
            vec2 uv, p = gl_FragCoord.xy/r - 0.5;
            uv = p;
            p.x *= r.x/r.y;
            z += .07;
            l = length(p);
            uv += p/l * (sin(z) + 1) * abs(sin(9*l - 2*z));
            c[i] = 0.01/length( abs( mod(uv, 1) - 0.5));
        }
        gl_FragColor = vec4(c/l,1);
        
    }
"""

def render():
    glColor3fv((1, 1, 1))
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_QUADS)
    glVertex3fv(( 1, -1, 0))
    glVertex3fv(( 1,  1, 0))
    glVertex3fv((-1,  1, 0))
    glVertex3fv((-1, -1, 0))
    glEnd()
    
def shade(const, program, code):
    shader = glCreateShader(const)
    glShaderSource(shader, code)
    glCompileShader(shader)
    print(glGetShaderInfoLog(shader))
    glAttachShader(program, shader)

def main():
    display = (1280, 720)
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    program = glCreateProgram()
    shade(GL_VERTEX_SHADER, program, VERTEX_SHADER_CODE)
    shade(GL_FRAGMENT_SHADER, program, FRAGMENT_SHADER_CODE)
    glLinkProgram(program)
    glUseProgram(program)
    
    theta = 4.3;
        
    print("Done")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        theta += 0.01;
        glUniform1f(glGetUniformLocation(program, "theta"), theta);
        render()
        pygame.display.flip()
        pygame.time.wait(13)
    
main()
