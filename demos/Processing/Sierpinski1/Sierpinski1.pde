void setup(){
  windowMove(800,0);
  size(600, 600);
  background(255,255,255);
  strokeWeight(10);
  stroke(255, 0, 0);
  point(width/2, height/2);
  stroke(255,0,255);
  int side = 200;
  point(width/2, height/2 - (sin(PI/3) * side)/2);
  point(width/2 + side/2, height/2 + (sin(PI/3) * side)/2);
  point(width/2 - side/2, height/2 + (sin(PI/3) * side)/2);
}
void draw(){
  drawTriangle(width/2, height/2, 200);
}

void drawTriangle(float x, float y, float side){
  float length = sin(PI/3) * side/2; 
  translate(x,y);
  stroke(0,0,255);
  strokeWeight(1);
  noFill();
  triangle(0, -length, side/2, length, -side/2, length);
}
