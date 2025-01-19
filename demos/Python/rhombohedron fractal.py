import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import math

plt.rcParams['toolbar'] = 'None'

max_level = 2  # >=3, computer will run slow
theta = math.pi/3 # acute angle in radians
origin_vertices = [
    [1, 0, 0], # e1
    [math.cos(theta), math.sin(theta), 0], # e2
    [math.cos(theta), (math.cos(theta) - (math.cos(theta) ** 2))/math.sin(theta), (math.sqrt(1 - 3 * math.cos(theta) ** 2 + 2 * math.cos(theta)**3))/math.sin(theta)] # e3
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

    draw_rhombohedron()

def draw_rhombohedron():
    rhombohedrons = generate_rhombohedron(0, 0, 0, 1, max_level)
    for rhombohedron in rhombohedrons:
        new_x, new_y, new_z, new_size = rhombohedron

        vertices = [
            [new_x, new_y, new_z], 
            [new_x + new_size * origin_vertices[1][0], new_y + new_size * origin_vertices[1][1], new_z + new_size * origin_vertices[1][2]],
            [new_x + new_size * (origin_vertices[0][0] + origin_vertices[1][0]), new_y + new_size * (origin_vertices[0][1] + origin_vertices[1][1]), new_z + new_size * (origin_vertices[0][2] + origin_vertices[1][2])],
            [new_x + new_size * origin_vertices[0][0], new_y + new_size * origin_vertices[0][1], new_z + new_size * origin_vertices[0][2]],
            [new_x + new_size * origin_vertices[2][0], new_y + new_size * origin_vertices[2][1], new_z + new_size * origin_vertices[2][2]],
            [new_x + new_size * (origin_vertices[1][0] + origin_vertices[2][0]), new_y + new_size * (origin_vertices[1][1] + origin_vertices[2][1]), new_z + new_size * (origin_vertices[1][2] + origin_vertices[2][2])],
            [new_x + new_size * (origin_vertices[0][0] + origin_vertices[1][0] + origin_vertices[2][0]), new_y + new_size * (origin_vertices[0][1] + origin_vertices[1][1] + origin_vertices[2][1]), new_z + new_size * (origin_vertices[0][2] + origin_vertices[1][2] + origin_vertices[2][2])],
            [new_x + new_size * (origin_vertices[0][0] + origin_vertices[2][0]), new_y + new_size * (origin_vertices[0][1] + origin_vertices[2][1]), new_z + new_size * (origin_vertices[0][2] + origin_vertices[2][2])]
        ]
        faces = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[0], vertices[3], vertices[7], vertices[4]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[1], vertices[2], vertices[6], vertices[5]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[0], vertices[1], vertices[5], vertices[4]]
        ]
        ax.add_collection3d(Poly3DCollection(faces, facecolors='#FFF', edgecolors='#2A5D57', alpha=.8))
    plt.show()

def generate_rhombohedron(x, y, z, rhombohedron_size, max_level):
    if max_level == 0:
        return[(x, y, z, rhombohedron_size)]
    
    new_size = rhombohedron_size/3
    rhombohedrons = []
    
    for dimension_x in range(3):
        for dimension_y in range(3):
            for dimension_z in range(3):
                if (dimension_x == 1 and dimension_y == 1) or (dimension_y == 1 and dimension_z == 1) or (dimension_x == 1 and dimension_z == 1):
                    continue

                new_x = x + dimension_x * new_size * origin_vertices[0][0] + dimension_y * new_size * origin_vertices[1][0] + dimension_z * new_size * origin_vertices[2][0]
                new_y = y + dimension_x * new_size * origin_vertices[0][1] + dimension_y * new_size * origin_vertices[1][1] + dimension_z * new_size * origin_vertices[2][1]
                new_z = z + dimension_x * new_size * origin_vertices[0][2] + dimension_y * new_size * origin_vertices[1][2] + dimension_z * new_size * origin_vertices[2][2]
                
                rhombohedrons.extend(generate_rhombohedron(new_x, new_y, new_z, new_size, max_level - 1))

    return rhombohedrons

setup()