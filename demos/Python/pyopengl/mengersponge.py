import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

pygame.display.set_caption("Menger Sponge")
max_level = 2  #not bigger than 3, or it will run slow.
vertices = [
    [-1,-1,-1],
    [-1,1,-1],
    [1,1,-1],
    [1,-1,-1],
    [-1,-1,1],
    [-1,1,1],
    [1,1,1],
    [1,-1,1],
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

    # glColor3ub(0,0,0)
    # glBegin(GL_LINES)
    # for edge in edges:
    #     for vertex in edge:
    #         glVertex3fv(vertices[vertex])
    # glEnd()

def generate_menger_sponge(x, y, z, cube_size, current_level):
    if current_level == 0:
        glPushMatrix()
        glTranslatef(x, y, z)
        glScalef(cube_size, cube_size, cube_size)
        draw_cube()
        glPopMatrix()
        return #add exit condition!!!

    new_size = cube_size/3
    for dimension_x in range(3):
        for dimension_y in range(3):
            for dimension_z in range(3):
                if (dimension_x == 1 and dimension_y == 1) or (dimension_y == 1 and dimension_z == 1) or (dimension_x == 1 and dimension_z == 1):
                    continue
                generate_menger_sponge(x + dimension_x * new_size, y + dimension_y * new_size, z + dimension_z * new_size, new_size, current_level - 1)

def init():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #update stuff
        glClearColor(1.0, 0.0, 0.0, 1.0) #bg color
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clear canvas
        glRotatef(1,1,1,1)

        # draw stuff
        glPushMatrix()
        generate_menger_sponge(0, 0, 0, 1, max_level)
        glPopMatrix()
        pygame.display.flip() #show visual


init()