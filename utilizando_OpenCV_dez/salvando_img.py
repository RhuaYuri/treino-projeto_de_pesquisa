import cv2

img = cv2.imread("C:\\Users\\rhuan\\Desktop\\arquivos_da_bolsa\\Projeto\\python\\projeto_pesquisa01\\files\\utilizando_OpenCV_dez\\img2.png")
cv2.imshow("Salvar Imagem", img)

k = cv2.waitKey(0) #tecla para fechar a janela

if k == 27: #equivalente a tecla "K" no teclado
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('salvarImagem.png', img) #salvando a imagem com outra extenção
    cv2.destroyAllWindows()