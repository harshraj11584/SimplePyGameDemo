
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

colors = (
    (0, 0, 0),
    (1, 1, 1),
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 0)
)

quads = (
    (0, 1, 2, 3),
    (4, 5, 7, 6),
    (0, 1, 5, 4),
    (2, 1, 5, 7),
    (6, 7, 2, 3),
    (0, 4, 6, 3)
    )

def Cube():
    #Declares the mdoe of drawing. Try GL_LINES instead of GL_QUADS
    glBegin(GL_QUADS)
    for i in range(6):
        #Each Eaud has a different Color
        glColor3fv(colors[i])
        for vertex in quads[i]:
            #draw the four vertices of the Quad
            glVertex3fv(verticies[vertex])
    #End the batch
    glEnd()

def main():
    display = (800, 600)
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glEnable(GL_DEPTH_TEST)
    #Takes a color, (r, g, b, a)
    glClearColor(0.2, 0.2, 0.2, 1)
    #Translates objects to be drawn to a given (x, y, z) position
    glTranslatef(0.0, 0.0, -5)
    
    while True:
        #Get all events and scan for close events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        glRotatef(1, 1, 1, 0)
    
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        
        #Swap display buffers
        pygame.display.flip()
        pygame.time.wait(10)


main()

