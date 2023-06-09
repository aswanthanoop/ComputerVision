import cv2 #importing opencv for computer vision functions

#creating an matrix of pixels reading from the image
myimg = cv2.imread(r"C:\Users\Aswanth\Downloads\WhatsApp Image 2022-03-25 at 10.44.45 AM (1).jpeg", 1)

#prints a matrix
print(myimg)

#displaying the image on a window
cv2.imshow("Sample", myimg)
cv2.waitKey(1000) #we use this to keep the window for a few moments
cv2.destroyAllWindows() #destroys the windows that have been open

#write image
cv2.imwrite('Sample1.jpeg', myimg)

#change color of the image to grayscale
gray = cv2.cvtColor(myimg, cv2.COLOR_BGR2GRAY)
cv2.imshow('SampleGrayScale', gray)
cv2.waitKey(1000)
cv2.destroyAllWindows()

#detecting edge of the image
edges = cv2.Canny(myimg, 100, 200) #this function uses 3 arguement (image matrix, min value of pixel, max value of pixel)
cv2.imshow('SampleEdges', edges)
cv2.waitKey(1000)
cv2.destroyAllWindows()