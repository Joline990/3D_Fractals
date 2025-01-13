int minBranchLength = 8;
int maxBranchLength = 150;

float time = 0;

void setup() {
  size(600, 600);
  windowMove(800, 0);
  frameRate(5); //make changes every second
}

void draw() {
  background(255);
  translate(width/2, height);
  stroke(0);
  drawBranch(maxBranchLength);
}

void drawBranch(float branchLength) {
  float branchThickness = map(branchLength, minBranchLength, maxBranchLength, 1, 20);
  strokeWeight(branchThickness);
  strokeCap(SQUARE);
  //root
  line(0, 0, 0, -branchLength);
  translate(0, -branchLength);

  branchLength*= 0.67;

  if (branchLength > minBranchLength) {
    float noise = noise(time); //add perline noise for angle -> tree is animating
    float angle = map(noise, 0, 1, 0, PI/6);
    //left branch
    push();
    rotate(-angle);
    drawBranch(branchLength);
    pop();
    //right branch
    push();
    rotate(angle);
    drawBranch(branchLength);
    pop();
  }
  time +=0.01; //don't forget to add time

  //adding flowers
  if (branchLength < minBranchLength * 2) {
    fill(255, 34, 255, 160); //alpha channel (between 0 en 255)
    noStroke();
    push();
    circle(0, 0, 10);
    pop();
  }
  //}
}
