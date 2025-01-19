# Install libraries
import pygame
import numpy as np
from math import * 

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Projection Cube")

scale = 100
circle_pos = [WIDTH/2, HEIGHT/2]
angle = 0

vertices = [
    np.matrix([-1, -1, 1]),
    np.matrix([1, -1, 1]),
    np.matrix([1, 1, 1]),
    np.matrix([-1, 1, 1]),
    np.matrix([-1,-1,-1]),
    np.matrix([1,-1,-1]),
    np.matrix([1,1,-1]),
    np.matrix([-1,1,-1])
]

clock = pygame.time.Clock() # change framerate

while True:
    clock.tick(60) # 60fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))
    

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
        ]
    )

    rotation_y = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
        ]
    )

    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
        ]
    )

    angle += 0.01

    for vertex in vertices:
        projection_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0] # not necessary to add this last line with zeros
        ])
        rotated2d = np.dot(rotation_z, vertex.reshape((3, 1))) # multiple matrices from numpy we use the special function dot; use reshape to make everything in different [] like [-1], [1], [1] instead of (-1,1,1)
        newrotated2d = np.dot(rotation_y, rotated2d)
        newnewrotated2d = np.dot(rotation_x, newrotated2d)

        projected2d = np.dot(projection_matrix, newnewrotated2d)
        
        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]
        pygame.draw.circle(screen,(0,0,0), (x, y), 5) # circle(position on screen, color, 2d-position, radius)

    pygame.display.update()