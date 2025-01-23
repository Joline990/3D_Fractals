import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

pygame.display.set_caption("cube - face culling")
size = 1
def draw_cube(x,y,z, size):
    glBegin(GL_TRIANGLES)
    # Top face
    glColor3f(1,0,0) #red color
    # counter-clockwise: 6,7,3 | 3,2,6
    glVertex3f(x + size, y + size, z - size)
    glVertex3f(x - size, y + size, z - size)
    glVertex3f(x - size, y + size, z + size) 

    glVertex3f(x - size, y + size, z + size) 
    glVertex3f(x + size, y + size, z + size)
    glVertex3f(x + size, y + size, z - size)

    # Bottom face
    glColor3f(0,1,0) #green color
    # clockwise: 4, 5, 1 | 1, 0, 4
    glVertex3f(x - size, y - size, z - size)
    glVertex3f(x + size, y - size, z - size)
    glVertex3f(x + size, y - size, z + size) 

    glVertex3f(x + size, y - size, z + size) 
    glVertex3f(x - size, y - size, z + size)
    glVertex3f(x - size, y - size, z - size)

    # Left face
    glColor3f(0,0,1) #blue color
    # clockwise: 4, 0, 3 | 3, 7, 4
    glVertex3f(x - size, y - size, z - size)
    glVertex3f(x - size, y - size, z + size)
    glVertex3f(x - size, y + size, z + size) 

    glVertex3f(x - size, y + size, z + size) 
    glVertex3f(x - size, y + size, z - size)
    glVertex3f(x - size, y - size, z - size)
    # Right face
    glColor3f(1,1,0) #yellow color
    # counter-clockwise: 1, 5, 6 | 6, 2, 1
    glVertex3f(x + size, y - size, z + size)
    glVertex3f(x + size, y - size, z - size)
    glVertex3f(x + size, y + size, z - size) 

    glVertex3f(x + size, y + size, z - size) 
    glVertex3f(x + size, y + size, z + size)
    glVertex3f(x + size, y - size, z + size)

    # Front face
    glColor3f(1,1,1) # white color
    # counter-clockwise: 2, 3, 0 | 0, 1, 2
    glVertex3f(x + size, y + size, z + size)
    glVertex3f(x - size, y + size, z + size)
    glVertex3f(x - size, y - size, z + size) 

    glVertex3f(x - size, y - size, z + size) 
    glVertex3f(x + size, y - size, z + size)
    glVertex3f(x + size, y + size, z + size)

    # Back face
    glColor3f(1,0,1) #pink color
    # clockwise: 4, 7, 6 | 6, 5, 4
    glVertex3f(x - size, y - size, z - size)
    glVertex3f(x - size, y + size, z - size)
    glVertex3f(x + size, y + size, z - size) 

    glVertex3f(x + size, y + size, z - size) 
    glVertex3f(x + size, y - size, z - size)
    glVertex3f(x - size, y - size, z - size)
  
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
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glFrontFace(GL_CCW)
        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clear canvas 
        
        # draw stuff
        draw_cube(0,0,0, size)

        pygame.display.flip() #show visual
        pygame.time.wait(20) #speed of rotating cube

init()