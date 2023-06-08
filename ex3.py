import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.draw import disk
from skimage.morphology import(erosion, dilation, closing, opening, area_closing, area_opening)
from skimage.color import rgb2gray


element = np.array([[0,1,0],[1,1,1],[0,1,0]])
plt.imshow(element, cmap='gray');

