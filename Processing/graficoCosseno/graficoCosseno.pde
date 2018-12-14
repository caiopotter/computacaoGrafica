float f(float x){
  return cos(x);
}

void setup(){
  size(800,600);
}

void draw() {
  noFill();
  
  float xo = -TWO_PI;
  float xf = TWO_PI;
  float dx = 0.001;
  float ymax = 1.0;
  float ymin = -1.0;
  int margem = 10;
  
  beginShape();
  for(float t = xo; t <= xf; t += dx){
    float x = map(t, xo, xf, margem, width-margem);
    float y = map(f(t), ymin, ymax, margem, height-margem);
    vertex(x,y);
  }
  endShape();
}
