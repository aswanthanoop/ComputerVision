import cv2
import numpy as np
while True:
    imagergb = cv2.imread(r"C:\Users\Aswanth\Downloads\wp7020037.jpg")
    srcpts = np.float32([[0,100],[700,260],[0,700],[700,400]])
    destpts = np.float32([[0,200],[600,0],[0,700],[1000,700]])
    resmatrix = cv2.getPerspectiveTransform(srcpts,destpts)
    resultimage = cv2.warpPerspective(imagergb, resmatrix, (500,600))
    cv2.imshow('frame',imagergb)
    cv2.imshow('frame1', resultimage)

    if cv2.waitKey(24) ==27:
        break