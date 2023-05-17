import cv2

myimg = cv2.imread(r"C:\Users\Aswanth\Downloads\WhatsApp Image 2022-03-29 at 5.43.02 PM.jpeg", 1)

print(myimg)

edges = cv2.Canny(myimg, 100, 200)
cv2.imshow("sampleEdge", edges)
cv2.waitKey(10000)
cv2.destroyAllWindows()


