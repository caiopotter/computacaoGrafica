from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# Rotations for cube.
xrot = yrot = zrot = 0.0
dx = 0.0
dy = 0.0
dz = 0.0
tx = 0.0
ty = 0.0
translador = 0.0
zoom = -50.0


def loadFile():
    reader = png.Reader(filename='caiomini.png')
    global listapixel, metadata, imagem_width, imagem_height
    imagem_width, imagem_height, pixels, metadata = reader.read_flat()
    listapixel = pixels.tolist()


def InitGL(Width, Height):
    loadFile()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)


def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), .1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def pegarPixelAtual(index):
    if metadata['alpha']:
        rgbCount = 4
    else:
        rgbCount = 3
    return [listapixel[index*rgbCount], listapixel[(index*rgbCount)+1], listapixel[(index*rgbCount)+2]]


def preencherComZeroAEsquerda(cor):
    cor[0] = str(cor[0]).zfill(3)
    cor[1] = str(cor[1]).zfill(3)
    cor[2] = str(cor[2]).zfill(3)

    return cor


def DrawGLScene():
    global xrot, yrot, zrot, texture, tx, ty, zoom

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glClearColor(0.5, 0.5, 0.5, 1.0)

    # glTranslatef(0.0, 0.0, -50.0)
    glTranslatef(tx, ty, zoom)

    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(zrot, 0.0, 0.0, 1.0)

    glBegin(GL_QUADS)
    cont = 0
    obj_file = open("C:\\Downloads\\teste.obj", "w+")
    obj_file.write('mtllib teste.mtl\n\n')
    mtl_file = open("C:\\Downloads\\teste.mtl", "w+")
    for z in range(0, imagem_height*2, 2):
        for i in range(0, imagem_width*2, 2):
            cor = pegarPixelAtual(cont)
            cor = preencherComZeroAEsquerda(cor)

            y = int(str(cor[0]) + str(cor[1]) + str(cor[2])) / 100000000.0
            glColor(float(cor[0])/255.0, float(cor[1]) / 255.0, float(cor[2]) / 255.0, 1.0)
            # front
            glVertex3f(i-1, 0, z+1)
            glVertex3f(i+1, 0, z+1)
            glVertex3f(i+1, y+1, z+1)
            glVertex3f(i-1, y+1, z+1)

            # back
            glVertex3f(i-1, 0, z-1)
            glVertex3f(i-1, y+1, z-1)
            glVertex3f(i+1, y+1, z-1)
            glVertex3f(i+1, 0, z-1)

            # Top
            glVertex3f(i-1, y+1, z-1)
            glVertex3f(i-1, y+1, z+1)
            glVertex3f(i+1, y+1, z+1)
            glVertex3f(i+1, y+1, z-1)

            # Bottom
            glVertex3f(i-1, 0, z-1)
            glVertex3f(i+1, 0, z-1)
            glVertex3f(i+1, 0, z+1)
            glVertex3f(i-1, 0, z+1)

            # Right
            glVertex3f(i+1, 0, z-1)
            glVertex3f(i+1, y+1, z-1)
            glVertex3f(i+1, y+1, z+1)
            glVertex3f(i+1, 0, z+1)

            # Left
            glVertex3f(i-1, 0, z-1)
            glVertex3f(i-1, 0, z+1)
            glVertex3f(i-1, y+1, z+1)
            glVertex3f(i-1, y+1, z-1)

            draw_in_file(obj_file, i, y, z, cont)
            fill_mtl(mtl_file, cont, float(cor[0])/255.0, float(cor[1]) / 255.0, float(cor[2]) / 255.0)

            cont = cont + 1

    glEnd()  # Done Drawing The Cube
    mtl_file.close()
    obj_file.close()
    sys.exit()

    # glutSwapBuffers()


def fill_mtl(m, cont, r, g, b):
    m.write('newmtl texture%s\n' % (str(cont)))
    m.write('Ka %s %s %s\n' % (str(r), str(g), str(b)))
    m.write('Kd %s %s %s\n' % (str(r), str(g), str(b)))
    m.write('illum 1\n\n')


def draw_in_file(obj_file, x, y, z, i):

    obj_file.write('v %s 0.0 %s\n' % (str(x - 1), str(z + 1)))
    obj_file.write('v %s 0.0 %s\n' % (str(x + 1), str(z + 1)))
    obj_file.write('v %s %s %s\n' % (str(x + 1), str(y + 1), str(z + 1)))
    obj_file.write('v %s %s %s\n' % (str(x - 1), str(y + 1), str(z + 1)))

    obj_file.write('v %s 0.0 %s\n' % (str(x - 1), str(z - 1)))
    obj_file.write('v %s %s %s\n' % (str(x - 1), str(y + 1), str(z - 1)))
    obj_file.write('v %s %s %s\n' % (str(x + 1), str(y + 1), str(z - 1)))
    obj_file.write('v %s 0.0 %s\n\n' % (str(x + 1), str(z - 1)))

    obj_file.write('g face%s\n' % (str(i)))
    obj_file.write('usemtl texture%s\n' % (str(i)))
    obj_file.write('f %s// %s// %s// %s//\n' % (str(1 + (8 * i)), str(2 + (8 * i)), str(3 + (8 * i)), str(4 + (8 * i))))
    obj_file.write('f %s// %s// %s// %s//\n' % (str(5 + (8 * i)), str(6 + (8 * i)), str(7 + (8 * i)), str(8 + (8 * i))))
    obj_file.write('f %s// %s// %s// %s//\n' % (str(1 + (8 * i)), str(2 + (8 * i)), str(8 + (8 * i)), str(5 + (8 * i))))
    obj_file.write('f %s// %s// %s// %s//\n' % (str(2 + (8 * i)), str(8 + (8 * i)), str(7 + (8 * i)), str(3 + (8 * i))))
    obj_file.write('f %s// %s// %s// %s//\n' % (str(3 + (8 * i)), str(7 + (8 * i)), str(6 + (8 * i)), str(4 + (8 * i))))
    obj_file.write('f %s// %s// %s// %s//\n' % (str(1 + (8 * i)), str(5 + (8 * i)), str(6 + (8 * i)), str(4 + (8 * i))))


def keyPressed(tecla, x, y):
    global dx, dy, dz, tx, ty, translador
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == 'x' or tecla == 'X':
        dx = 1.0
        dy = 0
        dz = 0
        translador = 0
    elif tecla == 'y' or tecla == 'Y':
        dx = 0
        dy = 1.0
        dz = 0
        translador = 0
    elif tecla == 'z' or tecla == 'Z':
        dx = 0
        dy = 0
        dz = 1.0
        translador = 0
    elif tecla == 'm' or tecla == 'M':
        dx = 0
        dy = 0
        dz = 0
        translador = 1


def mouseClicked(botao, estado_botao, x, y):
    global zoom
    if botao == 3 and estado_botao == 0:
        zoom = zoom + 1.0
    if botao == 4 and estado_botao == 0:
        zoom = zoom - 1.0


def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz, tx, ty, translador
    if tecla == GLUT_KEY_LEFT:
        print "ESQUERDA"
        xrot -= dx  # X rotation
        yrot -= dy  # Y rotation
        zrot -= dz
        tx -= translador
    elif tecla == GLUT_KEY_RIGHT:
        print "DIREITA"
        xrot += dx  # X rotation
        yrot += dy  # Y rotation
        zrot += dz
        tx += translador
    elif tecla == GLUT_KEY_UP:
        print "CIMA"
        ty += translador
    elif tecla == GLUT_KEY_DOWN:
        print "BAIXO"
        ty -= translador


def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    # get a 1024 x 768 window
    glutInitWindowSize(1024, 768)

    # the window starts at the upper left corner of the screen
    glutInitWindowPosition(0, 0)

    window = glutCreateWindow("Textura")

    glutDisplayFunc(DrawGLScene)

    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)

    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)

    # Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keyPressed)

    glutMouseFunc(mouseClicked)

    glutSpecialFunc(teclaEspecialPressionada)

    # Initialize our window.
    InitGL(1024, 768)

    # Start Event Processing Engine
    glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print "Hit ESC key to quit."
    main()