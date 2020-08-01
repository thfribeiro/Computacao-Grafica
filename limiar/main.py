import cv2
import numpy as np
import math

def limiar():
    img = cv2.imread("Tatu.jpg", 0)
    h, w = img.shape[:2]
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    l = 256
    prob_max = 0
    max = -1
    for t in range(l):
        for i in range(t):
            Pi = hist[i] / (h * w)
            if Pi > prob_max:
                max = Pi
    print(max)
    return max

img = cv2.imread('Tatu.jpg')
h, w = img.shape[:2]  # Slicing

th = limiar()
res, gray = cv2.threshold(img, th, 255, cv2.THRESH_BINARY)
cv2.imshow("Gray - OTSU", gray)
cv2.waitKey(0)
