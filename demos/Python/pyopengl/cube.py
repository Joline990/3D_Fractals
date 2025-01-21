import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

pygame.display.set_caption("Menger Sponge")

vertices = [
    (-1,-1,-1),
    (-1,1,-1),
    (1,1,-1),
    (1,-1,-1),
    (-1,-1,1),
    (-1,1,1),
    (1,1,1),
    (1,-1,1),
]
edges = [
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    (4,5),
    (5,6),
    (6,7),
    (7,4),
    (0,4),
    (1,5),
    (2,6),
    (3,7),
]
faces = [
    (0,1,2,3),
    (4,5,6,7),
    (0,4,5,1),
    (1,5,6,2),
    (2,6,7,3),
    (0,4,7,3),
]

def draw_cube():
    #draw first shapes, then the edges
    glColor3ub(255,255,0)
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glColor3ub(0,0,0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def init():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #update stuff
        glClearColor(1.0, 0.0, 0.0, 1.0) #bg color
        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clear canvas 
        
        # draw stuff
        draw_cube()

        pygame.display.flip() #show visual
        pygame.time.wait(20) #speed of rotating cube

init()