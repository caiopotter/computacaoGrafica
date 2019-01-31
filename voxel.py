import sys
import png


def loadFile():
    arquivoFonte = None
    try:
        arquivoFonte = sys.argv[1]
    except IndexError:
        arquivoFonte = 'D:\\Users\\cpttr\\Downloads\\grafica\\caiomini.png'
    reader = png.Reader(filename=arquivoFonte)
    global listapixel, metadata, imagem_width, imagem_height
    imagem_width, imagem_height, pixels, metadata = reader.read_flat()
    listapixel = pixels.tolist()
    criar_indice_texturas()


def criar_indice_texturas():
    cont = 0
    index_file = open("D:\\gitCaio\\results\\index.txt", "w+")
    for z in range(0, imagem_height*2, 2):
        for i in range(0, imagem_width*2, 2):
            cor = pegarPixelAtual(cont)
            index_file.write('%s %s %s' % (str(cor[0]), str(cor[1]), str(cor[2])))
            cont = cont + 1

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


def DrawScene():
    cont = 0
    texturaAtual = [None, None, None, 0]
    obj_file = open("D:\\gitCaio\\results\\teste.obj", "w+")
    obj_file.write('mtllib teste.mtl\n\n')
    mtl_file = open("D:\\gitCaio\\results\\teste.mtl", "w+")
    for z in range(0, imagem_height*2, 2):
        for i in range(0, imagem_width*2, 2):
            cor = pegarPixelAtual(cont)
            cor = preencherComZeroAEsquerda(cor)
            y = int(str(cor[0]) + str(cor[1]) + str(cor[2])) / 100000000.0
            if((texturaAtual != None) and (texturas_identicas(texturaAtual, [float(cor[0])/255.0, float(cor[1]) / 255.0, float(cor[2]) / 255.0]))):
                draw_in_file(obj_file, i, y, z, cont, texturaAtual[3])
            else:
                texturaAtual = fill_mtl(mtl_file, cont, float(cor[0])/255.0, float(cor[1]) / 255.0, float(cor[2]) / 255.0)
                draw_in_file(obj_file, i, y, z, cont)
            
            cont = cont + 1

    mtl_file.close()
    obj_file.close()
    sys.exit()


def texturas_identicas(texturaAtual, proximaTextura):
    if((texturaAtual[0] == proximaTextura[0]) and (texturaAtual[1] == proximaTextura[1]) and (texturaAtual[2] == proximaTextura[2])):
        return True
    else:
        return False


def fill_mtl(m, cont, r, g, b):
    m.write('newmtl texture%s\n' % (str(cont)))
    m.write('Ka %s %s %s\n' % (str(r), str(g), str(b)))
    m.write('Kd %s %s %s\n' % (str(r), str(g), str(b)))
    m.write('illum 1\n\n')
    return [r, g, b, cont]


def draw_in_file(obj_file, x, y, z, i, texturaAnterior=None):

    obj_file.write('v %s 0.0 %s\n' % (str(x - 1), str(z + 1)))
    obj_file.write('v %s 0.0 %s\n' % (str(x + 1), str(z + 1)))
    obj_file.write('v %s %s %s\n' % (str(x + 1), str(y + 1), str(z + 1)))
    obj_file.write('v %s %s %s\n' % (str(x - 1), str(y + 1), str(z + 1)))

    obj_file.write('v %s 0.0 %s\n' % (str(x - 1), str(z - 1)))
    obj_file.write('v %s %s %s\n' % (str(x - 1), str(y + 1), str(z - 1)))
    obj_file.write('v %s %s %s\n' % (str(x + 1), str(y + 1), str(z - 1)))
    obj_file.write('v %s 0.0 %s\n\n' % (str(x + 1), str(z - 1)))

    obj_file.write('g face%s\n' % (str(i)))

    if(texturaAnterior != None):
        obj_file.write('usemtl texture%s\n' % (str(texturaAnterior)))
    else:
        obj_file.write('usemtl texture%s\n' % (str(i)))
    obj_file.write('f %s// %s// %s// %s//\n' % (str(1 + (8 * i)), str(2 + (8 * i)), str(3 + (8 * i)), str(4 + (8 * i))))
    obj_file.write('f %s// %s// %s// %s//\n' % (str(5 + (8 * i)), str(6 + (8 * i)), str(7 + (8 * i)), str(8 + (8 * i))))
    obj_file.write('f %s// %s// %s// %s//\n' % (str(1 + (8 * i)), str(2 + (8 * i)), str(8 + (8 * i)), str(5 + (8 * i))))
    obj_file.write('f %s// %s// %s// %s//\n' % (str(2 + (8 * i)), str(8 + (8 * i)), str(7 + (8 * i)), str(3 + (8 * i))))
    obj_file.write('f %s// %s// %s// %s//\n' % (str(3 + (8 * i)), str(7 + (8 * i)), str(6 + (8 * i)), str(4 + (8 * i))))
    obj_file.write('f %s// %s// %s// %s//\n' % (str(1 + (8 * i)), str(5 + (8 * i)), str(6 + (8 * i)), str(4 + (8 * i))))


def main():
    loadFile()
    DrawScene()


# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    main()