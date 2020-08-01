import cv2
import numpy as np


def filterImage1(image):
    h, w = image.shape[:2]
    filtro = np.zeros((h, w))
    lista = []
    hnew = int(h / 4)
    wnew = int(w / 4)

    resized2 = cv2.resize(image, (wnew, hnew), interpolation=cv2.INTER_AREA)
    h, w = resized2.shape[:2]
    for i in range(h-1):
        for j in range(w-1):
            lista.append(resized2[i-1][j-1])
            lista.append(resized2[i-1][j])
            lista.append(resized2[i-1][j+1])
            lista.append(resized2[i][j-1])
            lista.append(resized2[i][j])
            lista.append(resized2[i][j+1])
            lista.append(resized2[i+1][j-1])
            lista.append(resized2[i+1][j])
            lista.append(resized2[i+1][j+1])
            filtro[i][j] = (sorted(lista)[4])
    return filtro.astype("uint8")



def filterImage2(image):
    h, w = image.shape[:2]
    filtro = np.zeros((h, w))
    lista = []
    hnew = int(h / 4)
    wnew = int(w / 4)

    resized2 = cv2.resize(image, (wnew, hnew), interpolation=cv2.INTER_AREA)
    h, w = resized2.shape[:2]

    for i in range(h-1):
        for j in range(w-1):
            lista.append(resized2[i-2][j-2])
            lista.append(resized2[i - 2][j-1])
            lista.append(resized2[i-2][j])
            lista.append(resized2[i-1][j+1])
            lista.append(resized2[i][j-2])
            lista.append(resized2[i][j-1])

            lista.append(resized2[i-1][j-1])
            lista.append(resized2[i-1][j])
            lista.append(resized2[i-1][j+1])
            lista.append(resized2[i][j-1])

            lista.append(resized2[i][j])

            lista.append(resized2[i][j+1])
            lista.append(resized2[i+1][j-1])
            lista.append(resized2[i+1][j])
            lista.append(resized2[i+1][j+1])

            lista.append(resized2[i+2][j+2])
            lista.append(resized2[i+2][j+1])
            lista.append(resized2[i+2][j])
            lista.append(resized2[i+1][j-1])
            lista.append(resized2[i][j+2])
            lista.append(resized2[i][j+1])

            filtro[i][j] = (sorted(lista)[12])
    return filtro.astype("uint8")


def filterImage3(image):
    h, w = image.shape[:2]
    filtro = np.zeros((h, w))
    lista = []
    hnew = int(h / 4)
    wnew = int(w / 4)

    resized2 = cv2.resize(image, (wnew, hnew), interpolation=cv2.INTER_AREA)
    h, w = resized2.shape[:2]
    for i in range(h-1):
        for j in range(w-1):
            lista.append(resized2[i-3][j-3])
            lista.append(resized2[i - 2][j - 3])
            lista.append(resized2[i - 1][j - 3])
            lista.append(resized2[i][j - 3])
            lista.append(resized2[i - 3][j-2])
            lista.append(resized2[i - 3][j-1])
            lista.append(resized2[i - 3][j])

            lista.append(resized2[i-2][j-2])
            lista.append(resized2[i - 2][j-1])
            lista.append(resized2[i-2][j])
            lista.append(resized2[i-1][j+1])
            lista.append(resized2[i][j-2])
            lista.append(resized2[i][j-1])

            lista.append(resized2[i-1][j-1])
            lista.append(resized2[i-1][j])
            lista.append(resized2[i-1][j+1])
            lista.append(resized2[i][j-1])

            lista.append(resized2[i][j])

            lista.append(resized2[i][j+1])
            lista.append(resized2[i+1][j-1])
            lista.append(resized2[i+1][j])
            lista.append(resized2[i+1][j+1])

            lista.append(resized2[i+2][j+2])
            lista.append(resized2[i+2][j+1])
            lista.append(resized2[i+2][j])
            lista.append(resized2[i+1][j-1])
            lista.append(resized2[i][j+2])
            lista.append(resized2[i][j+1])

            lista.append(resized2[i+3][j+3])
            lista.append(resized2[i + 2][j + 3])
            lista.append(resized2[i + 1][j + 3])
            lista.append(resized2[i][j + 3])
            lista.append(resized2[i + 3][j+2])
            lista.append(resized2[i + 3][j+1])
            lista.append(resized2[i + 3][j])

            filtro[i][j] = (sorted(lista)[24])
    return filtro.astype("uint8")

image = cv2.imread("macaco.png", 0)

filtered1 = filterImage1(image)
filtered2 = filterImage2(image)
filtered3 = filterImage3(image)


cv2.imshow("Original", image)
cv2.imshow("Filtrada1", filtered1)
cv2.imshow("Filtrada2", filtered2)
cv2.imshow("Filtrada3", filtered3)

cv2.waitKey(0)