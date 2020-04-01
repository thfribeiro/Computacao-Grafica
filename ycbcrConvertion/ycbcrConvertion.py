import cv2
import numpy as np

img = cv2.imread('Tatu.jpg')

h,w = img.shape[:2] #Slicing

imgCopy = img.copy()

imgCopy = imgCopy/255

imgYcBcR = np.zeros((h, w, 3), np.float)

# 0 Y
# 1 cB
# 2 cR

imgYcBcR[:, :, 0] = (0.2568 * img[:, :, 2]) + (0.5041 * img[:, :, 1]) + (0.097 * img[:, :, 0]) + 16
imgYcBcR[:, :, 1] = (-0.1482 * img[:, :, 2]) - (0.2910 * img[:, :, 1]) + (0.4392 * img[:, :, 0]) + 128
imgYcBcR[:, :, 2] = (0.4392 * img[:, :, 2]) - (0.3678 * img[:, :, 1]) - (0.0714 * img[:, :, 0]) + 128

Ymax = np.max(imgYcBcR[:, :, 0])
Ymin = np.min(imgYcBcR[:, :, 0])

#normalizando Y entre 0 e 1
imgYcBcR[:, :, 0] = (imgYcBcR[:, :, 0] - Ymin)/(Ymax - Ymin)

#normalizando cB entre 0 e 1
cBMax = np.max(imgYcBcR[:, :, 1])
cBMin = np.min(imgYcBcR[:, :, 1])

imgYcBcR[:, :, 1] = (imgYcBcR[:, :, 1] - cBMin) / (cBMax - cBMin)

#normalizando cR entre 0 e 1
cRMax = np.max(imgYcBcR[:, :, 2])
cRMin = np.min(imgYcBcR[:, :, 2])

imgYcBcR[:, :, 2] = (imgYcBcR[:, :, 2] - cRMin) / (cRMax - cRMin)

ycBcR = np.zeros((h, w, 3), np.uint8)
ycBcR = (imgYcBcR * 255).astype('uint8')

cv2.imshow("Y - Luminancia", ycBcR[:, :, 0])
cv2.imshow("cB - Azul", ycBcR[:, :, 1])
cv2.imshow("cR - Vermelho", ycBcR[:, :, 2])

novaImg = np.zeros((h, w, 3), np.uint8)
novaImg[:, :, 0] = ycBcR[:, :, 1] #B
novaImg[:, :, 1] = ycBcR[:, :, 0] #G
novaImg[:, :, 2] = ycBcR[:, :, 2] #R
cv2.imshow("Imagem YCbCr - G B R", novaImg)

cv2.imshow("RGB", img)

cv2.waitKey(0)

