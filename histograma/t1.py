import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread('Tatu.jpg')
print (img.shape)

h,w,c = img.shape
h2 = int(h/4)
w2 = int(w/4)

resized = cv2.resize(img, (w2,h2))
hR = numpy.zeros(256, numpy.float)
hG = numpy.zeros(256, numpy.float)
hB = numpy.zeros(256, numpy.float)

for i in range(h2):
  for j in range(w2):
    pR = resized[i,j,2]
    hR[resized[i,j,2]] = hR[resized[i,j,2]] + 1

    pG = resized[i,j,1]
    hG[resized[i,j,1]] = hG[resized[i,j,1]] + 1

    pB = resized[i,j,0]
    hB[resized[i,j,0]] = hB[resized[i,j,0]] + 1

plt.plot(hR, 'r')
plt.plot(hG, 'g')
plt.plot(hB, 'b')

plt.show()