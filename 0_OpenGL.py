
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1)
    )

colors = (1, 1, 0)

def main():
    display = (800, 600)
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    
    #Translates objects to be drawn to a given (x, y, z) position
    glTranslatef(0.0, 0.0, -5)
    
    while True:
        #Get all events and scan for close events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        glColor3fv(colors)
    
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glBegin(GL_POINTS)
        #Try LINES, LINE_STRIP here.
    
        for i in range(4):
            glVertex3fv(verticies[i])
        glEnd()
        
        #Swap display buffers
        pygame.display.flip()
        pygame.time.wait(10)


main()

