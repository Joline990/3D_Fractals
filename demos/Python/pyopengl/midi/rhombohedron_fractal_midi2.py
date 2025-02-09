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
FACE_COLORS = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
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

        glClearColor(0.0, 0.0, 0.0, 1.0) 
        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        generate_fractal(0, 0, 0, 1, 1)

        pygame.display.flip() 
        pygame.time.wait(20)

def generate_fractal(x, y, z, rhombohedron_size, max_level):
    if max_level == 0:
        glPushMatrix()
        glTranslatef(x, y, z)
        glScalef(rhombohedron_size, rhombohedron_size, rhombohedron_size)
        draw_rhombohedron()
        glPopMatrix()
        return
        
    new_size = rhombohedron_size/3

    for dimension_x in range(3):
        for dimension_y in range(3):
            for dimension_z in range(3):
                if (dimension_x == 1 and dimension_y == 1) or (dimension_y == 1 and dimension_z == 1) or (dimension_x == 1 and dimension_z == 1):
                    continue

                new_x = x + new_size * (dimension_x * origin_vertices[0][0] + dimension_y * origin_vertices[1][0] + dimension_z * origin_vertices[2][0])
                new_y = y + new_size * (dimension_x * origin_vertices[0][1] + dimension_y * origin_vertices[1][1] + dimension_z * origin_vertices[2][1])
                new_z = z + new_size * (dimension_x * origin_vertices[0][2] + dimension_y * origin_vertices[1][2] + dimension_z * origin_vertices[2][2])
                
                generate_fractal(new_x, new_y, new_z, new_size, max_level - 1)

def draw_rhombohedron():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    for i, face in enumerate(FACES):
        glColor3fv(FACE_COLORS[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

setup()