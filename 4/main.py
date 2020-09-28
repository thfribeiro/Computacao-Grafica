import cv2
import numpy as np

image = cv2.imread("image.png", 0)
filter_size = (3, 3)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, filter_size)

erode = cv2.erode(image, np.ones((3, 3)), iterations=1)
# closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, np.ones((3, 3)))
# dilatation = cv2.dilate(image, np.ones((2, 2)), iterations=1)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, np.ones((2, 2)), iterations=2)
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel, iterations=5)

cv2.imshow("original", image)
cv2.imshow("tophat", tophat)
imagem = cv2.bitwise_not(tophat)
cv2.imshow("imagem", imagem)
cv2.waitKey(0)

