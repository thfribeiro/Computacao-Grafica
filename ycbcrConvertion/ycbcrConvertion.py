import cv2
import numpy as np
import math

#HSI e YCBCR

img = cv2.imread('Tatu.jpg')
img2 = np.float32(cv2.imread("tatu.jpg"))/255
h, w = img.shape[:2]  # Slicing

imgCopy = img.copy()

imgCopy = imgCopy / 255

imgYcBcR = np.zeros((h, w, 3), np.float)

# 0 Y
# 1 cB
# 2 cR

imgYcBcR[:, :, 0] = (0.2568 * img[:, :, 2]) + (0.5041 * img[:, :, 1]) + (0.097 * img[:, :, 0]) + 16
imgYcBcR[:, :, 1] = (-0.1482 * img[:, :, 2]) - (0.2910 * img[:, :, 1]) + (0.4392 * img[:, :, 0]) + 128
imgYcBcR[:, :, 2] = (0.4392 * img[:, :, 2]) - (0.3678 * img[:, :, 1]) - (0.0714 * img[:, :, 0]) + 128

Ymax = np.max(imgYcBcR[:, :, 0])
Ymin = np.min(imgYcBcR[:, :, 0])

# normalizando Y entre 0 e 1
imgYcBcR[:, :, 0] = (imgYcBcR[:, :, 0] - Ymin) / (Ymax - Ymin)

# normalizando cB entre 0 e 1
cBMax = np.max(imgYcBcR[:, :, 1])
cBMin = np.min(imgYcBcR[:, :, 1])

imgYcBcR[:, :, 1] = (imgYcBcR[:, :, 1] - cBMin) / (cBMax - cBMin)

# normalizando cR entre 0 e 1
cRMax = np.max(imgYcBcR[:, :, 2])
cRMin = np.min(imgYcBcR[:, :, 2])

imgYcBcR[:, :, 2] = (imgYcBcR[:, :, 2] - cRMin) / (cRMax - cRMin)

ycBcR = np.zeros((h, w, 3), np.uint8)
ycBcR = (imgYcBcR * 255).astype('uint8')

cv2.imshow("Y - Luminancia", ycBcR[:, :, 0])
cv2.imshow("cB - blue", ycBcR[:, :, 1])
cv2.imshow("cR - red", ycBcR[:, :, 2])

novaImg = np.zeros((h, w, 3), np.uint8)
novaImg[:, :, 0] = ycBcR[:, :, 1]  # B
novaImg[:, :, 1] = ycBcR[:, :, 0]  # G
novaImg[:, :, 2] = ycBcR[:, :, 2]  # R
cv2.imshow("Imagem YCbCr - G B R", novaImg)

cv2.imshow("RGB", img)

blue = img2[:, :, 0]
green = img2[:, :, 1]
red = img2[:, :, 2]

intensidade = ((red + green + blue) / 3)

minimo = np.minimum(np.minimum(red, green), blue)
saturacao = 1 - (3 / (red + green + blue + 0.001) * minimo)
with np.errstate(divide='ignore', invalid='ignore'):
    matriz = np.copy(red)
    for i in range(0, blue.shape[0]):
        for j in range(0, blue.shape[1]):
            matriz[i][j] = 0.5 * ((red[i][j] - green[i][j]) + (red[i][j] - blue[i][j])) / \
                           math.sqrt((red[i][j] - green[i][j]) ** 2 +
                                     ((red[i][j] - blue[i][j]) * (green[i][j] - blue[i][j])))
            matriz[i][j] = math.acos(matriz[i][j])
            if blue[i][j] <= green[i][j]:
                matriz[i][j] = matriz[i][j]
            else:
                matriz[i][j] = ((360 * math.pi) / 180.0) - matriz[i][j]
img2[:, :, 0] = matriz
img2[:, :, 1] = saturacao
img2[:, :, 2] = intensidade
cv2.imshow("hsi", img2)
cv2.waitKey(0)
