void setup() 
{
  size(500,500);
  textAlign(CENTER,CENTER);
  textSize(36);
  stroke(0);
}

void draw()
{
  float segundos = map(second(), 0, 60, 0, TWO_PI) - HALF_PI;
  float fracaoSegundos = map(second(), 0, 60, 0, HALF_PI/15);
  float minutos = map(minute(), 0, 60, 0, TWO_PI) - HALF_PI;
  float fracaoMinutos = map(minute(), 0, 60, 0, HALF_PI/3); 
  float horas = map(hour()+(minute()/60), 0, 12, 0, TWO_PI) - HALF_PI;
  
  
  background(200);
  float x, y;
  float raioTotal = min(width,height)*0.45;
  float raioSegundos = min(width,height)*0.40;
  float raioMinutos = min(width,height)*0.38;
  float raioHoras = min(width,height)*0.30;
  float cx = width/2;
  float cy = height/2;
  translate(cx,cy);
  fill(255);
  ellipse(0,0,2*raioTotal,2*raioTotal);
  float tamanhoTracoHoras = 20;
  float tamanhoTracoMinutos = 10;
  float posicaoNumeros = 35;
  for(int i=0; i<60; i++)
  {
    float alpha = i*PI/30-HALF_PI;
    x = cos(alpha);
    y = sin(alpha);
    stroke(0);
    strokeWeight(1);
    if(i % 5 != 0)
    { 
      line(x*(raioTotal-tamanhoTracoMinutos),y*(raioTotal-tamanhoTracoMinutos),x*raioTotal,y*raioTotal);
    }
    else
    {
      fill(0);
      if(i == 0)
      {
       text("12",x*(raioTotal-posicaoNumeros), y*(raioTotal-posicaoNumeros));
      }
      else
      {
         text((i/5)+"",x*(raioTotal-posicaoNumeros), y*(raioTotal-posicaoNumeros));
      }
      line(x*(raioTotal-tamanhoTracoHoras),y*(raioTotal-tamanhoTracoHoras),x*raioTotal,y*raioTotal);
    }
  }

  stroke(255, 0, 0);
  line(0, 0, cos(segundos) * raioSegundos, sin(segundos) * raioSegundos);
  stroke(0);
  strokeWeight(2);
  line(0, 0, cos(minutos+fracaoSegundos) * raioMinutos, sin(minutos+fracaoSegundos) * raioMinutos);
  strokeWeight(4);
  line(0, 0, cos(horas+fracaoMinutos) * raioHoras, sin(horas+fracaoMinutos) * raioHoras);
  
}
