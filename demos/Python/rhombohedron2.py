# Step 1: install libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import math

plt.rcParams['toolbar'] = 'None'

# Step 4: create 3d plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

fig.canvas.manager.set_window_title('Rhombohedron on floor')
ax.set_axis_off()

# Step 5: set limits for the axes & show plot
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([0, 0.75])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_aspect('equal')

def draw_rhombohedron():
    # Step 2: define the vertices of the cube

    theta = math.pi/3 # acute angle

    # origin_vertices - the 3 vertices that start from the origin (0, 0, 0)
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

    # Step 3: define faces
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[0], vertices[3], vertices[7], vertices[4]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[0], vertices[1], vertices[5], vertices[4]]
    ]
    # Step 5: add rhombohedron to plot
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='b', alpha=.25))
    plt.show()

draw_rhombohedron()