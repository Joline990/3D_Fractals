import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math 

theta = math.pi/3
origin_vertices = [
    [1, 0, 0], # e1
    [math.cos(theta), math.sin(theta), 0], # e2
    [math.cos(theta), (math.cos(theta) - (math.cos(theta) ** 2))/math.sin(theta), (math.sqrt(1 - 3 * math.cos(theta) ** 2 + 2 * math.cos(theta)**3))/math.sin(theta)] # e3
]
vertices = [
    [0,0,0], 
    origin_vertices[1],
    [origin_vertices[0][0] + origin_vertices[1][0], origin_vertices[0][1] + origin_vertices[1][1], origin_vertices[0][2] + origin_vertices[1][2]],
    origin_vertices[0],
    origin_vertices[2], 
    [origin_vertices[1][0] + origin_vertices[2][0], origin_vertices[1][1] + origin_vertices[2][1], origin_vertices[1][2] + origin_vertices[2][2]],
    [origin_vertices[0][0] + origin_vertices[1][0] + origin_vertices[2][0], origin_vertices[0][1] + origin_vertices[1][1] + origin_vertices[2][1], origin_vertices[0][2] + origin_vertices[1][2] + origin_vertices[2][2]],
    [origin_vertices[0][0] + origin_vertices[2][0], origin_vertices[0][1] + origin_vertices[2][1], origin_vertices[0][2] + origin_vertices[2][2]]
]
FACES = [
    (0, 1, 2, 3),
    (0, 3, 7, 4),
    (4, 5, 6, 7),
    (1, 2, 6, 5),
    (2, 3, 7, 6),
    (0, 1, 5, 4),
]

def setup():
    pygame.init()
    pygame.display.set_caption("Rhombohedron fractal")
    screen = pygame.display.set_mode((0, 0), FULLSCREEN | DOUBLEBUF | OPENGL) 
    #screen = pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    screen_width, screen_height = screen.get_size()
    
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (screen_width/screen_height), 1.0, 10.0)
    glTranslatef(-3,-2,-10)
    glScale(3, 3, 3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # update stuff
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear canvas 

        # draw stuff
        draw_rhombohedron()

        pygame.display.flip() # show visual
        pygame.time.wait(20) # speed, reduce CPU usage

def draw_rhombohedron():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    for face in FACES:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

setup()