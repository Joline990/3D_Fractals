int maxIterations = 5;

void setup() {
  size (500, 500);
  windowMove(700, 0);
  background(255);
  drawRhombus(width/2, height/2, 400, 320, 1);
}

void drawRhombus(float x, float y, float D, float d, int iteration) {
  if (iteration == maxIterations) {
    draw1Rhombus(x, y, D, d);
  } else {
    float newD = D/3;
    float newd = d/3;
    //Draw all rhombuses, without middle one
    drawRhombus(x, y - D / 3, newD, newd, iteration + 1); // A
    drawRhombus(x + d / 6, y - D / 6, newD, newd, iteration + 1); // B
    drawRhombus(x + d / 3, y, newD, newd, iteration + 1); // C
    drawRhombus(x + d / 6, y + D / 6, newD, newd, iteration + 1); // D
    drawRhombus(x, y + D / 3, newD, newd, iteration + 1); // E
    drawRhombus(x - d / 6, y + D / 6, newD, newd, iteration + 1); // F
    drawRhombus(x - d / 3, y, newD, newd, iteration + 1); // G
    drawRhombus(x - d / 6, y - D / 6, newD, newd, iteration + 1); // H
  }
}
void draw1Rhombus(float x, float y, float D, float d) {
  fill(0, 0, 255);
  noStroke();
  pushMatrix();
  translate(x, y);
  quad(0, -D/2, d/2, 0, 0, D/2, -d/2, 0);
  popMatrix();
}
