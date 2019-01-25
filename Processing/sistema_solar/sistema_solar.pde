float angulo = 0;
float incremento = 0.1;

void setup() 
{
  size(500,500);
  textAlign(CENTER,CENTER);
  textSize(36);
  stroke(0);
}

void draw()
{
  background(200);
  float x, y, solX, solY, terraX, terraY;
  float solR = min(width,height)*0.11;
  solX = width/2;
  solY = height/2;
  translate(solX,solY);
  ellipse(0,0,2*solR,2*solR);
  
  terraX = width/4;
  terraY = height/4;
  
  float dt = min(width,height)*0.35;
  float dl = min(terraX,terraY)*0.30;
  
  float terraR = min(width,height)*0.04;
    
  float alpha = angulo*PI/30-HALF_PI;
  x = cos(alpha);
  y = sin(alpha);
    
  translate(x*dt, y*dt);
    
  ellipse(0,0,2*terraR,2*terraR);   

  float luaR = min(width,height)*0.015;
      
  alpha = 2*angulo*PI/30-HALF_PI;
  x = cos(-alpha);
  y = sin(-alpha);
      
  translate(x*dl, y*dl);
      
  ellipse(0,0,2*luaR,2*luaR);
      
  angulo += incremento;
}
