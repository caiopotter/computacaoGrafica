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


def loadFile():
    reader = png.Reader(filename='dado.png')
    global listapixel, metadata
    w, h, pixels, metadata = reader.read_flat()
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
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glClearColor(0.5, 0.5, 0.5, 1.0)

    glTranslatef(0.0, 0.0, -50.0)

    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(zrot, 0.0, 0.0, 1.0)

    glBegin(GL_QUADS)
    cont = 0
    for i in range(0, 240, 2):
        for z in range(0, 20, 2):
            cor = pegarPixelAtual(cont)
            cor = preencherComZeroAEsquerda(cor)
            cont = cont + 1

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

    glEnd()  # Done Drawing The Cube

    glutSwapBuffers()


def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == 'x' or tecla == 'X':
        dx = 1.0
        dy = 0
        dz = 0
    elif tecla == 'y' or tecla == 'Y':
        dx = 0
        dy = 1.0
        dz = 0
    elif tecla == 'z' or tecla == 'Z':
        dx = 0
        dy = 0
        dz = 1.0


def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print "ESQUERDA"
        xrot -= dx  # X rotation
        yrot -= dy  # Y rotation
        zrot -= dz
    elif tecla == GLUT_KEY_RIGHT:
        print "DIREITA"
        xrot += dx  # X rotation
        yrot += dy  # Y rotation
        zrot += dz
    elif tecla == GLUT_KEY_UP:
        print "CIMA"
        glutPostRedisplay()
    elif tecla == GLUT_KEY_DOWN:
        print "BAIXO"


def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    # get a 640 x 480 window
    glutInitWindowSize(800, 600)

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

    glutSpecialFunc(teclaEspecialPressionada)

    # Initialize our window.
    InitGL(800, 600)

    # Start Event Processing Engine
    glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print "Hit ESC key to quit."
    main()