import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import math
import numpy as np

MAX_LEVEL = 2 # >=3, computer will run slow
ANGLE = math.pi / 3
ORIGIN_VECTORS = np.array([
    [1, 0, 0],  # e1
    [math.cos(ANGLE), math.sin(ANGLE), 0],  # e2
    [math.cos(ANGLE), 
     (math.cos(ANGLE) - (math.cos(ANGLE) ** 2)) / math.sin(ANGLE), 
     (math.sqrt(1 - 3 * math.cos(ANGLE) ** 2 + 2 * math.cos(ANGLE) ** 3)) / math.sin(ANGLE)]  # e3
])
FACE_INDICES = np.array([
    [0, 1, 2, 3],
    [0, 3, 7, 4],
    [4, 5, 6, 7],
    [1, 2, 6, 5],
    [2, 3, 7, 6],
    [0, 1, 5, 4]
])
BACKGROUND_COLOR = '#2A5D57'

# Setup Plot
plt.rcParams['toolbar'] = 'None'
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_axis_off()
ax.set_facecolor(BACKGROUND_COLOR)
fig.patch.set_facecolor(BACKGROUND_COLOR)

precomputed_rhombohedrons = []
faces_to_draw = []

def setup():
    """Precombute rhombohedrons"""
    fig.canvas.manager.set_window_title('Rhombohedron Fractal')
    ax.set_xlim([0, 2])
    ax.set_ylim([0, 2])
    ax.set_zlim([0, 0.75])
    ax.set_aspect('equal')

    global precomputed_rhombohedrons
    precomputed_rhombohedrons = generate_rhombohedron(0, 0, 0, 1, MAX_LEVEL)
    
def draw_rhombohedron():
    """Draw rhombohedrons by looping over precomputed_rhombohedrons"""
    global precomputed_rhombohedrons

    for new_x, new_y, new_z, new_size in precomputed_rhombohedrons:
        base = np.array([new_x, new_y, new_z])
        vertices = np.array([
            base,
            base + new_size * ORIGIN_VECTORS[1],
            base + new_size * (ORIGIN_VECTORS[0] + ORIGIN_VECTORS[1]),
            base + new_size * ORIGIN_VECTORS[0],
            base + new_size * ORIGIN_VECTORS[2],
            base + new_size * (ORIGIN_VECTORS[1] + ORIGIN_VECTORS[2]),
            base + new_size * (ORIGIN_VECTORS[0] + ORIGIN_VECTORS[1] + ORIGIN_VECTORS[2]),
            base + new_size * (ORIGIN_VECTORS[0] + ORIGIN_VECTORS[2]),
        ])
        faces = vertices[FACE_INDICES]
        for face in faces:
            faces_to_draw.append(face)

def generate_rhombohedron(x, y, z, rhombohedron_size, MAX_LEVEL):
    """Recursive function to create a rhombohedron fractal"""
    if MAX_LEVEL == 0:
        return [(x, y, z, rhombohedron_size)]

    new_size = rhombohedron_size / 3
    rhombohedrons = np.empty((0, 4)) 

    for dimension_x in range(3):
        for dimension_y in range(3):
            for dimension_z in range(3):
                if (dimension_x == 1 and dimension_y == 1) or (dimension_y == 1 and dimension_z == 1) or (
                        dimension_x == 1 and dimension_z == 1):
                    continue
                
                new_pos = np.array([x, y, z]) + new_size * (
                    dimension_x * ORIGIN_VECTORS[0] +
                    dimension_y * ORIGIN_VECTORS[1] +
                    dimension_z * ORIGIN_VECTORS[2]
                )
                new_x, new_y, new_z = new_pos

                child_rhombohedrons = generate_rhombohedron(new_x, new_y, new_z, new_size, MAX_LEVEL - 1)
                rhombohedrons = np.vstack((rhombohedrons, child_rhombohedrons))
                
    return rhombohedrons


setup()
draw_rhombohedron()
ax.add_collection3d(Poly3DCollection(faces_to_draw, facecolors='#FFF', edgecolors='#2A5D57', alpha=.8))
plt.show()