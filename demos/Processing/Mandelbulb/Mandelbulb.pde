import peasy.*; //first install: sketch > import library > manage libraries; spin & rotate cube

int dimension = 64;
PeasyCam cam;
//get all points in an array, so you can do something with it, we call the array mandelbulb
ArrayList<PVector> mandelbulb = new ArrayList<PVector>();

void setup() {
  size(600, 600, P3D); //window size; P3D: telling processing you want a 3D space
  cam = new PeasyCam(this, 500); //500: camera position

  //DO THE MATH CALCULATION FOR OUR MANDELBULB, IN THE DRAW FUNCTION WE DRAW OUR MANDELBULB
  // translate(width/2, height/2); //unnecessary as PeasyCam centered everything
  for (int i = 0; i < dimension; i++) {
    for (int j = 0; j < dimension; j++) {
      for (int k = 0; k < dimension; k++) {
        //map() function: scale i from 0 (min) to dimension (max) to a range between -1 & 1
        float x = map(i, 0, dimension, -1, 1);
        float y = map(j, 0, dimension, -1, 1);
        float z = map(k, 0, dimension, -1, 1);
        //PVector(x,y,z) -> c in formula
        PVector zvector = new PVector(0, 0, 0); //first iteration

        int n = 8;
        int maxiterations = 10;
        int currentiteration = 0;
        while (true) {

          //PVector c = new PVector(r, theta, phi); //this is in cartesian, but we need spherical coordinate
          //transform cartesian coordinate of zvector to spherical coordinate
          Spherical sphericalZVector = spherical(zvector.x, zvector.y, zvector.z); //when we create a spherical coordinate, we return r, theta & phi, but when we want to call it, we have to use c.x, c.y... this is quite confusing, so let's create a class for it.

          //multiply r^n and each coordinate inside to have the new x.
          //our first iteration of z is zero (z=0). so it is a coordinate in 3d, we split it up and further we do it to the "n"th power
          float newx = pow(sphericalZVector.r, n) * sin(sphericalZVector.theta*n) * cos(sphericalZVector.phi*n);
          float newy = pow(sphericalZVector.r, n) * sin(sphericalZVector.theta*n) * sin(sphericalZVector.phi*n);
          float newz = pow(sphericalZVector.r, n) * cos(sphericalZVector.theta*n);

          //zvector = pow(zvector, n) + c; -> this won't work as pow expects two floats, so we split our code.
          zvector.x = newx + x;
          zvector.y = newy + y;
          zvector.z = newz + z;
          //x,y,z is the vector C in formula of the mandelbulb
          
          currentiteration++;

           if (sphericalZVector.r > 2) { //distance from center is bigger than 2, we do a break, so we stop our code there. and we will not add those large numbers.
            break;
          }
          
          //add the new points to the mandelblub array
          //place it inside the while loop, so it will only be added if the pixel is bounded.
          if(currentiteration < maxiterations){
          mandelbulb.add(new PVector(x*100, y*100, z*100));
          }
        }
      }
    }
  }
}
class Spherical {
  float r, theta, phi;
  Spherical(float r, float theta, float phi) {
    this.r = r;
    this.theta = theta;
    this.phi = phi;
  }
}
Spherical spherical(float x, float y, float z) {
  //{x,y,z}^n = r^n { sin(theta*n) * cos(phi*n) , sin(theta*n) * sin(phi*n) , cos(theta*n) }
  float r = sqrt(x*x + y*y + z*z);
  float theta = atan2(sqrt(x*x + y*y), z);
  float phi = atan2(y, x);
  // return new PVector(r,theta,phi);
  return new Spherical(r, theta, phi);
}

void draw() {
  background(255, 255, 255); //white background
  for (PVector v : mandelbulb) {
    strokeWeight(1); //making pixels bigger
    stroke(0); //color stroke
    point(v.x, v.y, v.z); //for every point create a 3d point cloud
  }
}
