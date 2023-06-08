import cv2
myimg = cv2.imread("D:\wp7541111-atreus-wallpapers.jpg",1)
cv2.waitkey(10000)


img_grey = cv2.cvtcolor(myimg,cv2)