# Demos
## p5js
- Fractals recursion: simple try of creating a 2d fractal
## Processing
### Mandelbulb
- <a href="./Processing/Mandelbulb/Mandelbulb.pde">Mandelbulb: </a>created by following this tutorial: https://www.youtube.com/watch?v=NJCiUVGiNyA&t=319s
### Sierpinski
#### Creating a Sierpinski triangle
- Step 1 (<a href="./Processing/Sierpinski1/Sierpinski1.pde">Sierpinski1</a>): Draw one triangle in the center of our canvas.
- Step 2 (<a href="./Processing/Sierpinski2/Sierpinski2.pde">Sierpinski2</a>): Create a function that will loop to make smaller triangles. I called it the `removeTriangle()` function, we don't actually delete the middle triangle, we draw three triangles (or one when only one iteration).
#### Adding interactivity
- Based on mouseX, you see other iterations: <a href="./Processing/Sierpinski_mouseX/Sierpinski_mouseX.pde">Sierpinski_mouseX</a>. This was based on the tutorial: https://www.youtube.com/watch?v=fwDkUxrFb0s&t=458s
#### Other cool things
- Make the triangles rotate with rotate(framecount), remember to call the loop function in draw() after adding a background, otherwise it won't rotate. https://www.youtube.com/watch?v=7AvyvJnkdjE&t=990s
- Animating the Arrowhead Curve: https://www.youtube.com/watch?v=ackDGIKx1cw
### Trees
- Created basic tree using steps on the Nature of Code website: <a href="./Processing/tree1/tree1.pde">Tree 1</a>
- Fractal tree where the angle changes based on mouseX: <a href="./Processing/tree_mouseX/tree_mouseX.pde">tree_mousX</a>
- Kind of animation where Perlin noise has been used to move the tree over time: <a href="./Processing/tree_animating_noise/tree_animating_noise.pde">tree_animating_noise</a>
### Sierpinski Rhombus fractal
- 2D: <a href="./Processing/sketch__Rhombus__fractal__2d_/sketch__Rhombus__fractal__2d_.pde">Sierpinski Rhombus fractal</a> -> Looks very similar to <a href="./Processing/Sierpinski2/Sierpinski2.pde">Sierpinski2</a>, the only difference is that Sierpinski2 used triangles and now it uses rhombuses.
## Python
### Cube
- First I followed tutorials where people make 3d cubes in Python. The <a href="./Python/3d projection cube.py">3d projection cube</a> was one I made. This was based on the tutorial: https://www.youtube.com/watch?v=qw0oY6Ld-L0.
- Next I created my 3d cube using different tutorials & sources I found: <a href="./Python/cube.py">Cube</a>
### Rhombohedron
- Method 1: positioning rhombohedron inside a cube with minimum = -1 and maximum = 1. <a href="./Python/rhombohedron.py">Rhombohedron</a> 
- Method 2: positioning rhombohedron with formulas<a href="./Python/rhombohedron2.py">Rhombohedron 2</a> 
### Menger sponge
- <a href="./Python/menger sponge.py">Menger Sponge</a>. This was based on this paper: https://www.researchgate.net/publication/381418345_Representing_the_Menger_Sponge_Using_Tuples_A_Computational_and_Educational_Approach and the menger sponge fractal by Daniel Shiffman: https://editor.p5js.org/codingtrain/sketches/5kcBUriAy 
- Difference between append() and extend(): <a href="./Python/append() vs extend().py">append() vs extend()</a>.
### Rhombohedron fractal
- <a href="./Python/rhombohedron fractal.py">Rhombohedron fractal</a>: Started from menger sponge & rhombohedron2 code.
### PyOpenGl
- <a href="./Python/pyopengl/cube.py">Cube</a>: Based on https://www.tutorialspoint.com/pygame/pygame_pyopengl.htm, https://medium.com/@aleksej.gudkov/best-python-libraries-for-3d-game-development-c302f65bc10b
- <a href="./Python/pyopengl/mengersponge.py">Menger sponge</a>
- Face culling cube: <a href="./Python/pyopengl/cube2.py">Cube 2</a>. Based on https://learnopengl.com/Advanced-OpenGL/Face-culling#:~:text=To%20enable%20face%20culling%20we,inner%20faces%20are%20indeed%20discarded, https://stackoverflow.com/questions/54067690/how-to-use-face-culling-and-depth-test-in-pyopengl