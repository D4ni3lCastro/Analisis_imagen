#Librería
import cv2
from cv2 import imshow
import numpy as np
"""import pytesseract
tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'"""

imgText="people"
#Lectura de imagen
img= cv2.imread(imgText+'.png')
imshow('Imagen Original',img)

#Imagen escala de grises
imgGrau= cv2.imread(imgText+'.png',0)
imshow('Grises',imgGrau)

cv2.waitKey(0)
cv2.destroyAllWindows()