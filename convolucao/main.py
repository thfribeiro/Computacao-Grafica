import cv2
import numpy as np
import math


def filterImage(image):
    kernel = np.ones((3, 3))
    kernel[1][1] = np.sum(kernel)
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


image = cv2.imread("macaco.jpg", 0)

filtered = filterImage(image)
cv2.imshow("Original", image)
cv2.imshow("Filtrada", filtered)
cv2.waitKey(0)
