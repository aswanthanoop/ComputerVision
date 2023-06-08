import cv2 as cv
import argparse
## [Load image]
parser = argparse.ArgumentParser(description='Code for Histogram Equalization tutorial.')
parser.add_argument('--input', help='Path to input image.', default='pen.jpg')
args = parser.parse_args()
src = cv.imread(r"C:\Users\Aswanth\Downloads\WhatsApp Image 2022-03-25 at 10.44.45 AM (1).jpeg")
cv.imshow('Source image',src)
# if src is None:
#print('Could not open or find the image:', args.input)
exit(0)
# ## [Convert to grayscale]
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# ## [Apply Histogram Equalization]
dst = cv.equalizeHist(src)
# ## [Display results]
cv.imshow('Equalized Image', dst)
# ## [Wait until user exits the program]
cv.waitKey()
cv.destroyAllWindows()
