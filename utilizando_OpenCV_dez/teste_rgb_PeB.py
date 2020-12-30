import cv2
import numpy as np

img = cv2.imread("C:\\Users\\rhuan\\Desktop\\arquivos_da_bolsa\\Projeto\\python\\projeto_pesquisa01\\files\\utilizando_OpenCV_dez\\imagem_teste.jpeg")

hight   = img.shape[0]
wight   = img.shape[1]
channes = img.shape[2]


print(f'Largura: {hight} \nAltura: {wight} \nCanais: {channes}')

imagem = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

blur = cv2.medianBlur(imagem, 7)

minx = np.array([129, 200, 0])
maxx = np.array([160, 255, 255])
mascara = cv2.inRange(blur, minx, maxx) #procurar na imagem os pixels que estão com as cores entre o maxx e o minxx


res = cv2.bitwise_and(img, img, mask=mascara)#junutando a imagem original com a máscara

#Convertendo para Preto e Branco
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filtro = cv2.blur(img2, (7, 7))

ret, thresh = cv2.threshold(filtro,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

juntar1 = np.concatenate((img, imagem), axis=1)
juntar2 = np.concatenate((img2, filtro), axis=1)
cv2.imshow("Quantidade de objetos", juntar1)
cv2.imshow("Quantidade de", juntar2)
cv2.imshow("outro", thresh)
cv2.waitKey(0)

cv2.destroyAllWindows()
