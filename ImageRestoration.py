import numpy as np
import cv2

src = cv2.imread(r"C:\Users\Aswanth\Downloads\Screenshot_2022-02-11-12-50-29-362_com.google.android.youtube.jpg")




grayscale = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

edge_kernel = np.array([[-1,-1,-1],[-1,9--1],[-1,-1,-1]])
sharpen_kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
img = cv2.filter2D(grayscale,-1,sharpen_kernel)

blur = cv2.medianBlur(img,3)
blur = cv2.GaussianBlur(img,(3,3),0)

cv2.imshow('Source image',src)
cv2.imshow('blur',blur)
cv2.waitKey()