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
    
    const float width = 1280, height = 720;
    
    void main(){
        float x = gl_FragCoord.x / width, y = gl_FragCoord.y / height;
        float color;
        color = step(0.5, x); //STEP
        //color = x; //LINEAR
        //color = x * x; //QUADRATIC
        //color = 1 - pow(x * x + y * y, 0.5); //RADIAL
        //color = pow(x, 5); //EXPONENTIAL
        //color = 9 * x * exp(1 - 9 * x); //IMPULSE
        
        gl_FragColor = vec4(color, color, color, 1);
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
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        render()
        pygame.display.flip()
        pygame.time.wait(13)
    
main()
