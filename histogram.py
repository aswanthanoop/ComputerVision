import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread(r"C:\Users\Aswanth\Downloads\WhatsApp Image 2022-03-25 at 10.44.45 AM (1).jpeg",0)

plt.hist(img.ravel(),256,[0,256])
equalize = cv.equalizeHist(img)
plt.hist(equalize.ravel(),256,[0,256])
plt.show

cv.imshow("Sample", img)
cv.waitKey(1000) #we use this to keep the window for a few moments
cv.destroyAllWindows()



