import numpy as np
import cv2
imagem = cv2.imread("C:\\Users\\rhuan\\Desktop\\arquivos_da_bolsa\\Projeto\\python\\projeto_pesquisa01\\files\\utilizando_OpenCV_dez\\img.jpg")
img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

ret, imgB = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
pintado = 5
cont = 0
for y in range(0, len(imgB)):
    for x in range(0, len(imgB[y])):
        cor = imgB[y][x]
        if cor == 255 and cor != pintado:
            cont += 1
        pintado += 5
print(cont)
cv2.imshow('teste', imgB)
cv2.waitKey(0)
cv2.destroyAllWindows()
