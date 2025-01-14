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