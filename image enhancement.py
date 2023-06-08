import cv2
from matplotlib import pyplot as plt
import numpy as np
im = cv2.imread("D:\wp7541111-atreus-wallpapers.jpg",0)
im_inverse = 255 - im
fig = plt.figure(figsize=(15,5))

ax=fig.add_subplot(121)
plt.title('Original',fontsize=18)
plt.imshow(im,cmap='gray')

ax= fig.add_subplot(122)
plt.imshow(im_inverse,cmap='gray')
ax.set_title('Inverse Transform',fontsize=18)

print(im_inverse)

cv2.imshow("sample", im_inverse)
cv2.waitKey(10000)
cv2.destroyAllWindows()
