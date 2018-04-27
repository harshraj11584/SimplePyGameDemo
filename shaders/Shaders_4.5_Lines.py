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
        float x = 2 * gl_FragCoord.x / width - 1, y = 2 * gl_FragCoord.y / height - 1;
        
        vec3 color = vec3(0.2, 1, 0);
        vec3 color2 = vec3(1, 0.2, 0);
        vec3 color3 = vec3(0, 0.2, 1);
        vec3 color4 = vec3(0.7, 0.1, 1);
        
        color  *= abs(0.0025 / sin(x*2 + 0.5  +    sin(y + 2*theta)));
        color2 *= abs(0.005 / sin(x  +            sin(y + 4*theta)));
        color3 *= abs(0.01 / sin(x + 0.66 +    0.3*sin(y + 5*theta)));
        color4 *= abs(0.01 / sin(2*x - 0.66 +    0.5*sin(y + 7*theta)));
        
        gl_FragColor = vec4(color + color2 + color3 + color4, 1);
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
