import cv2
import numpy as np
import math


def filterImage1(image):
    kernel = np.ones((3, 3))
    kernel[0][0] = 0
    kernel[0][2] = 0
    kernel[2][0] = 0
    kernel[2][2] = 0
    h, w = image.shape[:2]
    filtro = np.zeros((h, w))

    for i in range(h-1):
        for j in range(w-1):
            #print(int(image[i][j] * kernel[1][1]) / 17)
            filtro[i][j] = (image[i-1][j-1] * kernel[0][0] + image[i-1][j] * kernel[0][1] + image[i-1][j+1] * kernel[0][2] +\
                              image[i][j-1] * kernel[1][0] + image[i][j] * kernel[1][1] + image[i][j+1] * kernel[1][2] +\
                              image[i+1][j-1] * kernel[2][0] + image[i+1][j] * kernel[2][1] + image[i+1][j+1] * kernel[2][2]) / 17
            #print(filtro[i][j][0])

    return filtro.astype("uint8")

def filterImage2(image):
    kernel = np.ones((3, 3))
    h, w = image.shape[:2]
    filtro = np.zeros((h, w))

    for i in range(h-1):
        for j in range(w-1):
            #print(int(image[i][j] * kernel[1][1]) / 17)
            filtro[i][j] = (image[i-1][j-1] * kernel[0][0] + image[i-1][j] * kernel[0][1] + image[i-1][j+1] * kernel[0][2] +\
                              image[i][j-1] * kernel[1][0] + image[i][j] * kernel[1][1] + image[i][j+1] * kernel[1][2] +\
                              image[i+1][j-1] * kernel[2][0] + image[i+1][j] * kernel[2][1] + image[i+1][j+1] * kernel[2][2]) / 17
            #print(filtro[i][j][0])

    return filtro.astype("uint8")

def filterImage3(image):
    kernel = np.ones((3, 3))
    kernel[1][1] = 2
    h, w = image.shape[:2]
    filtro = np.zeros((h, w))

    for i in range(h-1):
        for j in range(w-1):
            #print(int(image[i][j] * kernel[1][1]) / 17)
            filtro[i][j] = (image[i-1][j-1] * kernel[0][0] + image[i-1][j] * kernel[0][1] + image[i-1][j+1] * kernel[0][2] +\
                              image[i][j-1] * kernel[1][0] + image[i][j] * kernel[1][1] + image[i][j+1] * kernel[1][2] +\
                              image[i+1][j-1] * kernel[2][0] + image[i+1][j] * kernel[2][1] + image[i+1][j+1] * kernel[2][2]) / 17
            #print(filtro[i][j][0])

    return filtro.astype("uint8")

def filterImage4(image):
    kernel = np.ones((3, 3))
    kernel[1][1] = 4
    kernel[0][1] = 2
    kernel[1][0] = 2
    kernel[1][2] = 2
    kernel[0][1] = 2

    h, w = image.shape[:2]
    filtro = np.zeros((h, w))

    for i in range(h-1):
        for j in range(w-1):
            #print(int(image[i][j] * kernel[1][1]) / 17)
            filtro[i][j] = (image[i-1][j-1] * kernel[0][0] + image[i-1][j] * kernel[0][1] + image[i-1][j+1] * kernel[0][2] +\
                              image[i][j-1] * kernel[1][0] + image[i][j] * kernel[1][1] + image[i][j+1] * kernel[1][2] +\
                              image[i+1][j-1] * kernel[2][0] + image[i+1][j] * kernel[2][1] + image[i+1][j+1] * kernel[2][2]) / 17
            #print(filtro[i][j][0])

    return filtro.astype("uint8")

image = cv2.imread("Tatu.jpg", 0)

filtered1 = filterImage1(image)
filtered2 = filterImage2(image)
filtered3 = filterImage3(image)
filtered4 = filterImage4(image)

cv2.imshow("Original", image)
cv2.imshow("Filtrada1", filtered1)
cv2.imshow("Filtrada2", filtered2)
cv2.imshow("Filtrada3", filtered3)
cv2.imshow("Filtrada4", filtered4)
cv2.waitKey(0)
