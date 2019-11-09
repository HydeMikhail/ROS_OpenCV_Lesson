#!/home/mhyde/vEnvs/rosPy/bin/python

'''
Practice breaking Color image into Color Channels
and converting images to GrayScale

From the ROS course on Udemy:

https://www.udemy.com/course/ros-essentials/

'''

import cv2

imageName = 'Tree.jpg'

xLoc, yLoc = 3440 / 2, (1440 / 2) - 100

#Read Image (Color)
cImg = cv2.imread("images/" + imageName, cv2.IMREAD_COLOR)
#Read Image (GrayScale)
gsImg = cv2.imread("images/" + imageName, cv2.IMREAD_GRAYSCALE)

#Display Image in Native Color
cv2.imshow("Original Color", cImg)
cv2.moveWindow("Original Color", xLoc, yLoc)
print cImg.shape

#Split The Image into Color Channels
height, width, length = cImg.shape
blue, green, red = cv2.split(cImg)

cv2.imshow("Blue Channel", blue)
cv2.moveWindow("Blue Channel", xLoc + 275, yLoc)

cv2.imshow("Green Channel", green)
cv2.moveWindow("Green Channel", xLoc - 275, yLoc)

cv2.imshow("Red Channel", red)
cv2.moveWindow("Red Channel", xLoc, yLoc - 350)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Display Image in GrayScale
cv2.imshow("GrayScale", gsImg)
cv2.moveWindow("GrayScale", xLoc, yLoc)
print gsImg.shape

cv2.waitKey(0)
cv2.destroyAllWindows()
