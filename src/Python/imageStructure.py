#!/home/mhyde/vEnvs/rosPy/bin/python

'''
Veiwing some of the Data Structures properties
of an image.

From the ROS course on Udemy:

https://www.udemy.com/course/ros-essentials/

'''

import numpy as np
import cv2

imageName = "B&W"

print 'Read an image from file'
img = cv2.imread("images/"+imageName+".jpg")

print 'Display the content of the image\n'
print img
print 'In Python, an image is stored in a numpy array. Numpy is \
library used for scientific computing of multi-dimensional \
arrays and matrices.\n'

print 'We can determine several features of the images using numpy \
array properties\n'
print 'Type of an image type(img): %s\n'%type(img)
print 'Size of the image img.size: %d\n'%img.size
print 'Length of the image (number of pixel in the vertical direction) \
len(img): %d\n'%len(img)
print 'Shape of an image (length in pixe, width in pixel, number of color) \
img.shape (%d,%d,%d)\n'%img.shape
print 'Image length (also height) img.shape[0]: %d\n'%img.shape[0]
print 'Image width img.shape[1]: %d\n'%img.shape[1]

height, width, channels = img.shape
print 'Height = %d\n'%height
print 'Width = %d\n'%width
print 'Channels = %d\n'%channels

print 'Number of colors per pixel img.shape[2]: %d\n'%img.shape[2]
print 'Number of pixels: %d'%(img.shape[0]*img.shape[1])
print 'Type of the image img.dtype: %s\n'%img.dtype
print 'Sub-image at row [10] (img[10])\n'
print img[10]
print 'Shape of sub-image at row [0] (img[10].shape)\n'
print img[10].shape
print 'Pixel at raw 10 and column 5 (img[10, 5])\n'
print img[10, 5]
print img[10][5]
print 'Pixel at raw 0 and column 0 (img[0, 0])\n'
print img[0, 0]
print img[0][0]

print 'You can see a single channel in the image, for example only the \
first channel\n'
print img[:, :, 0]
