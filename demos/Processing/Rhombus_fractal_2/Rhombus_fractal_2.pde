int maxLevel = 3;

void setup() {
  size (500, 500);
  windowMove(700, 0);
  background(255);
  generateRhombus(width/2, height/2, 400, 320, maxLevel);
}

void generateRhombus(float x, float y, float D, float d, int maxLevel) {
  if (maxLevel == 0) {
    drawRhombus(x, y, D, d);
  } else {
    float newD = D/3;
    float newd = d/3;
    //Draw all rhombuses, without middle one
    generateRhombus(x, y - D / 3, newD, newd, maxLevel - 1); // A
    generateRhombus(x + d / 6, y - D / 6, newD, newd, maxLevel - 1); // B
    generateRhombus(x + d / 3, y, newD, newd, maxLevel - 1); // C
    generateRhombus(x + d / 6, y + D / 6, newD, newd, maxLevel - 1); // D
    generateRhombus(x, y + D / 3, newD, newd, maxLevel - 1); // E
    generateRhombus(x - d / 6, y + D / 6, newD, newd, maxLevel - 1); // F
    generateRhombus(x - d / 3, y, newD, newd, maxLevel - 1); // G
    generateRhombus(x - d / 6, y - D / 6, newD, newd, maxLevel - 1); // H
  }
}
void drawRhombus(float x, float y, float D, float d) {
  fill(0, 0, 255);
  stroke(0, 0, 255);
  pushMatrix();
  translate(x, y);
  quad(0, -D/2, d/2, 0, 0, D/2, -d/2, 0);
  popMatrix();
}
