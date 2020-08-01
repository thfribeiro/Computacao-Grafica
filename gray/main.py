import cv2
import numpy as np

path = "Tatu.jpg"

img = cv2.imread(path)
print(img.shape)

h, w = img.shape[:2]
print("Tamanho da Imagem \n Largura: " + str(w) + " Altura: " + str(h))
hnew = int(h / 4)
wnew = int(w / 4)

resized2 = cv2.resize(img, (wnew, hnew), interpolation=cv2.INTER_AREA)

imgR = resized2[:, :, 2]

imgG = resized2[:, :, 1]

imgB = resized2[:, :, 0]

gray = np.zeros((hnew, wnew))
for i in range(hnew - 1):
    for j in range(wnew - 1):
        media = int(resized2[i, j, 2] + resized2[i, j, 1] + resized2[i, j, 0]) / 3
        print(media)
        gray[i][j] = media
gray = gray.astype("uint8")

cv2.imshow("Imagem2", resized2)
cv2.imshow("gray", gray)
cv2.waitKey(0)
