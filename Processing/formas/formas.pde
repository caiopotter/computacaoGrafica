void setup() 
{
  size(500,500);
  textAlign(CENTER,CENTER);
  textSize(36);
  stroke(0);
  background(155);
  int raio = 100;
  int numeroLados = 3;
  int x = width/2;
  int y = height/2;
  translate(x, y);
  desenharForma(numeroLados, raio);
  
}

void draw()
{
  int x = width/2;
  int y = height/2;
  translate(x, y);
  int raio = 100;
  int numeroLados = 3;
  if(keyPressed){
    numeroLados = key-48;
    if(numeroLados > 2 && numeroLados <= 9){
      background(155);
      desenharForma(numeroLados, raio);
    }
  }

 
 
  
}

void desenharForma(int numeroLados, int raio){
print(numeroLados);
  rotate(HALF_PI*3);
  float angulo = TWO_PI/numeroLados;
  beginShape();
  for(float a = 0; a <= TWO_PI; a += angulo){
     float caminhoX = cos(a)* raio;
     float caminhoY = sin(a)* raio;
     vertex(caminhoX, caminhoY);
    
  }
  endShape(CLOSE);
  
}
