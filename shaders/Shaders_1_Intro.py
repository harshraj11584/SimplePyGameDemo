import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_QUADS)
    glColor3fv((1, 0, 0))
    glVertex3fv(( 1, -1, 0))
    glColor3fv((0, 0, 1))
    glVertex3fv(( 1,  1, 0))
    glColor3fv((1, 1, 0))
    glVertex3fv((-1,  1, 0))
    glColor3fv((0, 0, 0))
    glVertex3fv((-1, -1, 0))
    glEnd()

def main():
    display = (1280, 720)
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        render()
        pygame.display.flip()
        pygame.time.wait(13)
    
main()
