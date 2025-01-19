import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
plt.rcParams['toolbar'] = 'None' 

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
fig.canvas.manager.set_window_title('Menger sponge')
ax.set_axis_off()

def draw_menger_sponge():
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.set_aspect('equal') # equal aspect-ratio size for whole cube

    cubes = generate_menger_sponge(0, 0, 0, 1, 1) # when current_level 3: program is very slow, so use value smaller than 3.
    for cube in cubes:
        new_x, new_y, new_z, new_size = cube
        vertices = [
            [new_x, new_y, new_z],
            [new_x, new_y + new_size, new_z], 
            [new_x + new_size, new_y + new_size, new_z],
            [new_x + new_size, new_y, new_z],
            [new_x, new_y, new_z + new_size],
            [new_x, new_y + new_size, new_z + new_size],
            [new_x + new_size, new_y + new_size, new_z + new_size],
            [new_x + new_size, new_y, new_z + new_size],
        ]
        faces = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[4], vertices[7], vertices[3]],
            [vertices[0], vertices[4], vertices[5], vertices[1]],
            [vertices[1], vertices[5], vertices[6], vertices[2]],
            [vertices[2], vertices[3], vertices[7], vertices[6]]
        ]
        ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', edgecolors='black', alpha=.9))

    plt.show()


def generate_menger_sponge(x, y, z, cube_size, current_level):
    if current_level == 0:
        return[(x, y, z, cube_size)]
    
    new_size = cube_size/3
    cubes = []
    
    for dimension_x in range(3):
        for dimension_y in range(3):
            for dimension_z in range(3):
                if (dimension_x == 1 and dimension_y == 1) or (dimension_y == 1 and dimension_z == 1) or (dimension_x == 1 and dimension_z == 1):
                    continue

                cubes.extend(generate_menger_sponge(x + dimension_x * new_size, y + dimension_y * new_size, z + dimension_z * new_size, new_size, current_level - 1))
    
    return cubes

draw_menger_sponge()