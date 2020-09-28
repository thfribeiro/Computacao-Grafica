import cv2
import numpy as np
import argparse
import os

# 3) Construa um algoritmo que seja capaz de realizar as seguintes operações
# morfológicas em imagens de escala de cinza, para elementos estruturantes do
# tipo Cruz ou Quadrado de tamanho 3x3:

# Criando um parser para entrada de parâmetros via console
parser = argparse.ArgumentParser()
parser.add_argument("input_image")  # -> caminho para imagem
parser.add_argument("structuring_element")  # -> elemento estruturante - quadrado, cruz
args = parser.parse_args()


def my_erode(img, kernel):
    h, w = img.shape
    erode = np.zeros((h, w))
    for i in range(h-1):
        for j in range(w-1):
            list = []
            for k in range(3):
                for l in range(3):
                    if kernel[k][l] == 1:
                        try:
                            list.append(img[i+k][j+l])
                        except:
                            pass
            erode[i][j] = min(list)
    return erode.astype("uint8")


def my_dilatation(img, kernel):
    h, w = img.shape
    dilatation = np.zeros((h, w))
    for i in range(h-1):
        for j in range(w-1):
            list = []
            for k in range(3):
                for l in range(3):
                    if kernel[k][l] == 1:
                        try:
                            list.append(img[i+k][j+l])
                        except:
                            pass
            dilatation[i][j] = max(list)
    return dilatation.astype("uint8")


def my_opening(img, kernel):
    opening = my_dilatation(img, kernel)
    return opening.astype("uint8")


def my_closing(img, kernel):
    closing = my_erode(img, kernel)
    return closing.astype("uint8")


image = cv2.imread(args.input_image, 0)
filter_size = (3, 3)

if args.structuring_element == "cruz":
    structuring_element = cv2.getStructuringElement(cv2.MORPH_CROSS, filter_size)
elif args.structuring_element == "quadrado":
    structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, filter_size)
else:
    structuring_element = np.ones(filter_size)
    os.abort()

cv2.imshow("Original", image)

erode = my_erode(image, structuring_element)
cv2.imshow("Erode", erode)

dilatation = my_dilatation(image, structuring_element)
cv2.imshow("Dilatation", dilatation)

opening = my_opening(erode, structuring_element)
cv2.imshow("Opening", opening)

closing = my_closing(dilatation, structuring_element)
cv2.imshow("Closing", closing)

cv2.waitKey(0)
