int maxIterations = 3;

void setup() {
  windowMove(800, 0);
  size(600, 600);
  background(255, 255, 255);
  removeTriangle(width/2, height/2, 500, 1);
}

void removeTriangle(float x, float y, float side, int iteration) {
  //print('iteration') - maybe saving as array and do something with it?
  if ( iteration == maxIterations) {
    drawTriangle(x, y, side);
  } else {
    //draw 3 new triangles inside the original triangle
    float halfHeightTriangle = sin(PI/3) * side/2; 
    removeTriangle(x, y - halfHeightTriangle/2, side/2, iteration + 1);
    removeTriangle(x + side/4, y + halfHeightTriangle/2, side/2, iteration + 1);
    removeTriangle(x - side/4, y + halfHeightTriangle/2, side/2, iteration + 1);
  }
}
void drawTriangle(float x, float y, float side) {
  float halfHeightTriangle = sin(PI/3) * side/2; 
  //height triangle; divide by 2 = half height; sine of an acute angle in a right-angled triangle.
  
  pushMatrix(); 
  translate(x, y); 
  fill(0,0,255);
  noStroke();
  triangle(0, -halfHeightTriangle, side/2, halfHeightTriangle, -side/2, halfHeightTriangle);
  popMatrix();

  strokeWeight(20);
  stroke(0,255,255);
  point(width/2, height/2);
}
