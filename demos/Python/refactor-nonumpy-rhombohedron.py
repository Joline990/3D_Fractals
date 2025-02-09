import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import math
plt.rcParams['toolbar'] = 'None'

MAX_LEVEL = 2 # >=3, computer will run slow
THETA = math.pi/3
ORIGIN_VECTORS = [
    [1, 0, 0], # e1
    [math.cos(THETA), math.sin(THETA), 0], # e2
    [math.cos(THETA), (math.cos(THETA) - (math.cos(THETA) ** 2))/math.sin(THETA), (math.sqrt(1 - 3 * math.cos(THETA) ** 2 + 2 * math.cos(THETA)**3))/math.sin(THETA)] # e3
]
FACES = [
    [0, 1, 2, 3],
    [0, 3, 7, 4],
    [4, 5, 6, 7],
    [1, 2, 6, 5],
    [2, 3, 7, 6],
    [0, 1, 5, 4]
]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def setup():
    fig.canvas.manager.set_window_title('Rhombohedron fractal')
    ax.set_axis_off()
    ax.set_facecolor('#2A5D57') 
    fig.patch.set_facecolor('#2A5D57')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.set_xlim([0, 2])
    ax.set_ylim([0, 2])
    ax.set_zlim([0, 0.75])
    ax.set_aspect('equal')

def draw_rhombohedron():
    for x, y, z, size in generate_rhombohedron(0, 0, 0, 1, MAX_LEVEL):
        add_rhombohedron(x, y, z, size)
    plt.show()

def add_rhombohedron(new_x, new_y, new_z, new_size):
        vertices = [
            [new_x, new_y, new_z], 
            [new_x + new_size * ORIGIN_VECTORS[1][0], new_y + new_size * ORIGIN_VECTORS[1][1], new_z + new_size * ORIGIN_VECTORS[1][2]],
            [new_x + new_size * (ORIGIN_VECTORS[0][0] + ORIGIN_VECTORS[1][0]), new_y + new_size * (ORIGIN_VECTORS[0][1] + ORIGIN_VECTORS[1][1]), new_z + new_size * (ORIGIN_VECTORS[0][2] + ORIGIN_VECTORS[1][2])],
            [new_x + new_size * ORIGIN_VECTORS[0][0], new_y + new_size * ORIGIN_VECTORS[0][1], new_z + new_size * ORIGIN_VECTORS[0][2]],
            [new_x + new_size * ORIGIN_VECTORS[2][0], new_y + new_size * ORIGIN_VECTORS[2][1], new_z + new_size * ORIGIN_VECTORS[2][2]],
            [new_x + new_size * (ORIGIN_VECTORS[1][0] + ORIGIN_VECTORS[2][0]), new_y + new_size * (ORIGIN_VECTORS[1][1] + ORIGIN_VECTORS[2][1]), new_z + new_size * (ORIGIN_VECTORS[1][2] + ORIGIN_VECTORS[2][2])],
            [new_x + new_size * (ORIGIN_VECTORS[0][0] + ORIGIN_VECTORS[1][0] + ORIGIN_VECTORS[2][0]), new_y + new_size * (ORIGIN_VECTORS[0][1] + ORIGIN_VECTORS[1][1] + ORIGIN_VECTORS[2][1]), new_z + new_size * (ORIGIN_VECTORS[0][2] + ORIGIN_VECTORS[1][2] + ORIGIN_VECTORS[2][2])],
            [new_x + new_size * (ORIGIN_VECTORS[0][0] + ORIGIN_VECTORS[2][0]), new_y + new_size * (ORIGIN_VECTORS[0][1] + ORIGIN_VECTORS[2][1]), new_z + new_size * (ORIGIN_VECTORS[0][2] + ORIGIN_VECTORS[2][2])]
        ]
        faces = []
        for face in FACES:
            face_vertices = []
            for i in face:
                face_vertices.append(vertices[i])
            faces.append(face_vertices)

        ax.add_collection3d(Poly3DCollection(faces, facecolors='#FFF', edgecolors='#2A5D57', alpha=.8))

def generate_rhombohedron(x, y, z, rhombohedron_size, MAX_LEVEL):
    if MAX_LEVEL == 0:
        return[(x, y, z, rhombohedron_size)]
    
    new_size = rhombohedron_size/3
    rhombohedrons = []
    
    for dimension_x in range(3):
        for dimension_y in range(3):
            for dimension_z in range(3):
                if (dimension_x == 1 and dimension_y == 1) or (dimension_y == 1 and dimension_z == 1) or (dimension_x == 1 and dimension_z == 1):
                    continue

                new_x = x + new_size * (dimension_x * ORIGIN_VECTORS[0][0] + dimension_y * ORIGIN_VECTORS[1][0] + dimension_z * ORIGIN_VECTORS[2][0])
                new_y = y + new_size * (dimension_x * ORIGIN_VECTORS[0][1] + dimension_y * ORIGIN_VECTORS[1][1] + dimension_z * ORIGIN_VECTORS[2][1])
                new_z = z + new_size * (dimension_x * ORIGIN_VECTORS[0][2] + dimension_y * ORIGIN_VECTORS[1][2] + dimension_z * ORIGIN_VECTORS[2][2])
                
                rhombohedrons.extend(generate_rhombohedron(new_x, new_y, new_z, new_size, MAX_LEVEL - 1))

    return rhombohedrons

setup()
draw_rhombohedron()