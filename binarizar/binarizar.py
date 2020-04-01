import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Tatu.jpg')

h,w = img.shape[:2]
cv.imshow("Original", img)

limiar = 110

imgCinza = np.zeros((h,w), np.uint8)

imgCinza = (img[..., 0]*0.1 + img[..., 1] * 0.65 + img[..., 2] * 0.25).astype('uint8')
cv.imshow("Cinzado", imgCinza)

hist = cv.calcHist([imgCinza],[0], None, [256],[0,256])

max = np.argmax(hist)
print(max)

th, res = cv.threshold(img[...,1], 220,255, cv.THRESH_BINARY)
cv.imshow("Limiarizado", res)
plt.plot(hist,color = 'b')
plt.xlim([0,255])
plt.show()

cv.waitKey(0)