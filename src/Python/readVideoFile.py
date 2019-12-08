#!/home/mhyde/vEnvs/rosPy/bin/python

'''
Run a WebCam Feed Using OpenCV

From the ROS course on Udemy:

https://www.udemy.com/course/ros-essentials/

'''

import cv2
import numpy as np

videoCap = cv2.VideoCapture('video/tennis-ball-video.mp4')

while True:
    ret, frame = videoCap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1000 / 60) & 0xFF == ord('m'):
        break

videoCap.release()
cv2.destroyAllWindows()
