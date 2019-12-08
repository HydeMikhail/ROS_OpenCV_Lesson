#!/home/mhyde/vEnvs/rosPy/bin/python

'''
Color Filtering
'''

import cv2

#Pull image from file
image = cv2.imread("images/tennisball02.jpg")
cv2.imshow("OG Tennis Ball", image)

#Convert Image to HSV Colorspace for easier data handling
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Tennis Ball", hsv)

#Define the bounds of the mask

            #Col/2 Sat  Bri
yellowLower = (30, 150, 100)
yellowUpper = (50, 255, 255)

#Define the mask by applying the image type and the bounds
mask = cv2.inRange(hsv, yellowLower, yellowUpper)

cv2.imshow("mask image", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()
