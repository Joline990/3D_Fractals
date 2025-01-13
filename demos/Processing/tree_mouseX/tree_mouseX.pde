int minBranchLength = 8;
int maxBranchLength = 150;

void setup() {
  size(600, 600);
  windowMove(800, 0);
}

void draw() {
  background(255);
  translate(width/2, height);
  stroke(0);
  drawBranch(maxBranchLength, map(mouseX, 0, width, PI/2, PI/60));
}

void drawBranch(float branchLength, float angle) {
  float branchThickness = map(branchLength, minBranchLength, maxBranchLength, 2, 20);
  strokeWeight(branchThickness);
  strokeCap(SQUARE);
  if(branchLength < minBranchLength * 2){
    stroke(255,34,255);
  }
  //root
  line(0, 0, 0, -branchLength);
  //go to endpoint of root
  translate(0, -branchLength);

  branchLength*= 0.67; //make branchLength smaller
  
  if(branchLength > minBranchLength){
   //left branch
  push();
  rotate(-angle);
  drawBranch(branchLength, angle); //recall function
  pop();
  //right branch
  push();
  rotate(angle);
  drawBranch(branchLength, angle); //recall function
  pop();
  }
}
