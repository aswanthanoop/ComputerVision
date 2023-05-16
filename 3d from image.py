import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import itertools
import stl

def inc_str(x, angle_a):
    #x is the distance or number of row
    #angle_a is the angle of camera
    cos_val = math.cos(math.radians(90-angle_a))
    x_depth = x / cos_val
    return(x_depth)

cap = cv2.VideoCapture(r"C:\Users\Aswanth\Downloads\Midnight Run. (R34 GTR, FD RX7, Evo and more) _ Zhiyun Crane 3 Lab _ 4K.mp4")
image_3D =[]
counter=0 #counter will help us keep the size if the final output
lower_red = np.array([168,120,70])
upper_red = np.array([210,255,255])
kernel = np.ones((3, 3), np.uint8)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
for i in range(length):
    ret, img = cap.read()
    if counter%1==0:
        #dilate and erode to make the light continous
        #img = cv2.flip(img, 0)
        img = cv2.dilate(img, kernel = kernel, iterations = 8)
        img = cv2.erode(img, kernel = kernel, iterations = 8)
        #convert to HSV for masking
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #create mask 1
        mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
        res = cv2.bitwise_and(img,img, mask= mask1)
        #dilate and erode to remove sharp edges
        res = cv2.erode(res, kernel, iterations = 4)
        res = cv2.dilate(res, kernel, iterations=5)
        #convert res to gray and thresholding
        res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        ret, res = cv2.threshold(res, 0, 255, cv2.THRESH_BINARY)
        #create mask 2
        mask2 = cv2.bitwise_not(res)
        #apply mask 2 on original image
        result = cv2.bitwise_and(img, img, mask = mask2)
        result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(result, 100, 255, cv2.THRESH_BINARY)
        thresh = cv2.bitwise_not(thresh)
        new_row_lenght = round(inc_str(thresh.shape[0], 40))
        new_array = np.full((new_row_lenght, thresh.shape[1]), 254, dtype='uint8')
        for i in range(thresh.shape[1]):
            for j in range(thresh.shape[0]):
                new_j = round(inc_str(j, 39.940))
                new_array[new_j, i] = thresh[j, i]
        ret, new_array = cv2.threshold(new_array, 254, 255, cv2.THRESH_BINARY)
        new_array = cv2.dilate(new_array, kernel)
        new_array[721,:] = 0 # this will create a black line at the end of every image. this will act like a base line for the 3D model
        #print('new image shape: ',new_array.shape)
        image_3D.append(new_array)
    else:
        pass
    counter+=1
image_3D = np.array(image_3D)


vertices_list = []
for i, k in itertools.product(range(image_3D.shape[0]), range(image_3D.shape[2])):
    for j in range(image_3D.shape[1]):
        if image_3D[i][j][k]==0:
            vertix = [i,j,k]
            vertices_list.append(vertix)
            break
vertices_list = np.array(vertices_list)

ncol = image_3D.shape[0]
nrow = image_3D.shape[2]
ndepth = image_3D.shape[0]
new_array = np.zeros((ndepth, nrow, 3))
for x in range(vertices_list.shape[0]):
    i = vertices_list[x][0]
    j = vertices_list[x][1]
    k = vertices_list[x][2]

    new_array[i][k] = vertices_list[x]

faces = []
for x in range(0,ncol-1):
    for y in range(0, nrow-1):
        #for traingular face 1
        if np.all(new_array[x][y]!=0):
            v1 = new_array[x][y]
            v2 = new_array[x+1][y]
            v3 = new_array[x+1][y+1]
            face1 = np.array([v1, v2, v3])
            #for traingular face 2
            v1 = new_array[x][y]
            v2 = new_array[x][y+1]
            v3 = new_array[x+1][y+1]
            face2 = np.array([v1, v2, v3])
            faces.append(face1)
            faces.append(face2)
        else:
            pass
face_array = np.array(faces)

surface = mesh.Mesh(np.zeros(face_array.shape[0], dtype = mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        surface.vectors[i][j] = face_array[i][j]
#to save the stl file of the surface
surface.save('surface5_1.stl')