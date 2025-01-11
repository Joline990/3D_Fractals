void setup() {
  size(600, 600);
  background(255);
  windowMove(800, 0);
}

void draw() {
  translate(width/2, height);
   strokeWeight(5);
   stroke(0);
  drawBranch(150);
}

void drawBranch(float branchLength) {
  //root
  line(0, 0, 0, -branchLength);
  //go to endpoint of root
  translate(0, -branchLength);

  branchLength*= 0.67; //make branchLength smaller
  
  if(branchLength > 20){
   //left branch
  push();
  rotate(-PI/6);
  drawBranch(branchLength); //recall function
  pop();
  //right branch
  push();
  rotate(PI/6);
  drawBranch(branchLength); //recall function
  pop();
  }
}
