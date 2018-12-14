float[] roda(float cx, float cy, float px, float py, float a )
{
  float _px = ((px-cx)*cos(a)-(py-cy)*sin(a))+cx;
  float _py = ((px-cx)*sin(a)+(py-cy)*cos(a))+cy;
  return new float[] { _px, _py };
}

void setup(){
 size(800,600); 
}

void draw(){
  background(128);
 koch(10, 300, 790, 300, 8*mouseX/width); 
}

void koch(float ax, float ay, float bx, float by, int n){
  if(n == 0){
    line(ax, ay, bx, by);
  }
  else{
    float cx = ax + (bx-ax)/3;
    float cy = ay + (by-ay)/3;
    float dx = ax + (bx-ax)*2/3;
    float dy = ay + (by-ay)*2/3;
    float e[] = roda(cx, cy, dx, dy, -PI/3);
    koch(ax, ay, cx, cy, n-1);
    koch(cx, cy, e[0], e[1], n-1);
    koch(e[0], e[1], dx, dy, n-1);
    koch(dx, dy, bx, by, n-1);
  }
}
