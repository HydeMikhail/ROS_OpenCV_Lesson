#!/home/mhyde/vEnvs/rosPy/bin/python

'''
Simple script for getting comfortable with
the OpenCV library in Python

From the ROS course on Udemy:

https://www.udemy.com/course/ros-essentials/

'''

import cv2
import numpy as np

imageName = 'Tree'

print "Reading Image File ... "
img = cv2.imread("images/"+imageName+".jpg")

print "Create a window to hold the image ... "
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

print "Display the Image ... "
cv2.imshow("Image", img)

print 'Press any key to make the copy ... '
cv2.waitKey(0)

print "Image copied to Folder images/copy/ ... "
cv2.imwrite('images/copy/'+imageName+"_copy.jpg", img)
