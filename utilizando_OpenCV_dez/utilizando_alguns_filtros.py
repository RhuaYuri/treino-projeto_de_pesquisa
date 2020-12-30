import cv2
import numpy as np

img = cv2.imread("C:\\Users\\rhuan\\Desktop\\arquivos_da_bolsa\\Projeto\\python\\projeto_pesquisa01\\files\\utilizando_OpenCV_dez\\img2.png")

kernel = np.ones((6,6),np.float32)/30
GaussianBlur = cv2.GaussianBlur(img, (5 , 5),0)
blur = cv2.blur(img, (9, 9))
filtro2D = cv2.filter2D(img, -1, kernel)
median = cv2.medianBlur(img, 55)
bilateralFilter = cv2.bilateralFilter(img, 9, 100, 300)








juntar1 = np.concatenate((img, filtro2D, median), axis=1)
juntar2 = np.concatenate((GaussianBlur, blur, bilateralFilter), axis=1)
final = np.concatenate((juntar1, juntar2), axis=0)
cv2.imshow('Filtros', final)
cv2.waitKey(0)
cv2.destroyAllWindows()