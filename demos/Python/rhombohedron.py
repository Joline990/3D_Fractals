# Step 1: install libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams['toolbar'] = 'None' #delete remove before create a figure

# Step 2: define the vertices of the cube
vertices = [
    [0, 1, 0],
    [0, 0, -1],
    [-1, -1, -1],
    [-1, 0, 0],
    [1, 1, 1],
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]
]
# Step 3: define the faces of the cube
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [vertices[0], vertices[3], vertices[7], vertices[4]],
    [vertices[4], vertices[5], vertices[6], vertices[7]],
    [vertices[1], vertices[2], vertices[6], vertices[5]],
    [vertices[2], vertices[3], vertices[7], vertices[6]],
    [vertices[0], vertices[1], vertices[5], vertices[4]]
]
# Step 4: create a 3d plot & generate the cube
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

fig.canvas.manager.set_window_title('rhombohedron') # change window title
ax.set_axis_off() # delete axis 

# change bg color
ax.set_facecolor('#E7FCF8') #inside plot
fig.patch.set_facecolor('#E7FCF8') #outside plot

ax.add_collection3d(Poly3DCollection(faces, 
 facecolors='#7BBAA9', linewidths=2, edgecolors='#2A5D57', alpha=.85))

# Step 5: set limits for the axes & show plot
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_aspect('equal') # equal aspect-ratio size for whole cube

plt.show()