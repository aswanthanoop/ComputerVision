import glob
import cv2
import numpy as np

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30 , 0.001)
objp = np.zeros((9*6,3), np.float32)
objp[:,:2] = np.mgrid[0:6.0:9].T.reshape(-1,2)

objpoints = []
imgpoints = []
images = glob.glob(r"D:\wallpapers redbull\1917899.jpg")

for fname in images:
  img = cv2.imread(fname)
  gray = cv2.cvtColor(img,cv.COLOR_BGR2GRAY)
  ret , corners = cv2.findChessboardCorners(gray,(6,9), None)

  if ret == True:
    objpoints.append(objp)
    corners2 = cv2.cornerSubPix(gray , corners , (11,11) , (-1,-1) , criteria)
    imgpoints.append(corners)

    cv2.drawChessboardCorners(img , (6,9) , corners2 , ret)