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
    
    void main(){        
        float x0 = 3.5 * gl_FragCoord.x/width - 2.5, y0 = 2*gl_FragCoord.y/height - 1;
        int iteration = 0;
        
        //JULIA FRACTAL
        float x = x0, y = y0;
        while (x*x + y*y < 4  && iteration < max_iteration) {
            float xtemp = x*x - y*y;
            y = 2*x*y + 0.7885 * cos(4.2);
            x = xtemp + 0.7885 * sin(4.2);
            iteration++;
        }
        
        int i = max_iteration/4, j = max_iteration/2;
        gl_FragColor = 20*vec4(float(mod(iteration, i))/i , float(mod(iteration, j))/j, float(iteration)/max_iteration, 1);
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
