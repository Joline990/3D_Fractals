import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import rtmidi
import time

pygame.display.set_caption("Menger Sponge")
max_level = 2  # not bigger than 3, or it will run slow.
inverse_fractal = False
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
    # draw first shapes, then the edges
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

def generate_menger_sponge(x, y, z, cube_size, current_level):
    if current_level == 0:
        glPushMatrix()
        glTranslatef(x, y, z)
        glScalef(cube_size, cube_size, cube_size)
        draw_cube()
        glPopMatrix()
        return # add exit condition!!!

    global inverse_fractal
    new_size = cube_size/3

    for dimension_x in range(3):
        for dimension_y in range(3):
            for dimension_z in range(3):
                middle_shape_condition = (dimension_x == 1 and dimension_y == 1) or (dimension_y == 1 and dimension_z == 1) or (dimension_x == 1 and dimension_z == 1)
                if not inverse_fractal:
                    if middle_shape_condition:
                        continue
                    generate_menger_sponge(x + dimension_x * new_size, y + dimension_y * new_size, z + dimension_z * new_size, new_size, current_level - 1)
                else: 
                    if middle_shape_condition:
                        generate_menger_sponge(x + dimension_x * new_size, y + dimension_y * new_size, z + dimension_z * new_size, new_size, current_level - 1)

def init():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    
    midi_in = init_midi()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                midi_in.close_port()
                quit()

        process_midi_message(midi_in)
        #update stuff
        glClearColor(0.0, 0.0, 0.0, 1.0) # bg color
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # clear canvas
        glRotatef(1,1,1,1)

        # draw stuff
        glPushMatrix()
        generate_menger_sponge(0, 0, 0, 1, max_level)
        glPopMatrix()

        pygame.display.flip() #show visual

def init_midi():
    midi_in = rtmidi.MidiIn()
    ports_dictionary = {k: v for (v, k) in enumerate(midi_in.get_ports())}
    midi_in.open_port(ports_dictionary["LPD8 mk2"]) 

    return midi_in

def process_midi_message(midi_in):
    global inverse_fractal
    message_and_dt = midi_in.get_message()

    if message_and_dt:
        (message, dt) = message_and_dt
        command = hex(message[0])
        channel = message[1]
       
        if channel == 40: 
            if command == "0x90":
                inverse_fractal = True
            elif command == "0x80":
                
                inverse_fractal = False
    else:
        time.sleep(0.001)

init()