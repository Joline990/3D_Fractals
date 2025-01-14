function setup() {
  createCanvas(320, 320);
  background(255);
  drawCircles(width/2, height/2, width/6);
}

function draw() {
  // No need to loop
  noLoop();
}

function drawCircles(x, y, radius) {
    strokeWeight(2);
    stroke(0);
    noFill();
    circle(x, y, radius * 2);

   if (radius > 4) {
    let distance = radius + radius/2;
     
    drawCircles(x, y - distance, radius/2);
    //drawCircles(x, y + distance, radius/2);
    drawCircles(x - distance, y, radius/2);
    drawCircles(x + distance, y, radius/2);
  }
}
   