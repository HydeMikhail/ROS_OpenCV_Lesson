#!/home/mhyde/vEnvs/rosPy/bin/python

'''
Run a WebCam Feed Using OpenCV

From the ROS course on Udemy:

https://www.udemy.com/course/ros-essentials/

'''

import cv2
import numpy as np

videoCap = cv2.VideoCapture('/dev/video0')

while True:
    ret, frame = videoCap.read()

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1000 / 60) & 0xFF == ord('m'):
        break

videoCap.release()
cv2.destroyAllWindows()
