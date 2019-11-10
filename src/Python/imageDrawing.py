#!/home/mhyde/vEnvs/rosPy/bin/python

'''
Run a WebCam Feed Using OpenCV

From the ROS course on Udemy:

https://www.udemy.com/course/ros-essentials/

'''

import numpy as np
import cv2

#Define Numpy Array of Zeros (0 = Black)
image = np.zeros((1000, 2000, 3), np.uint8)

#Define a line
#       OBJECT  START   END         RGB Values       LineWidth
cv2.line(image, (0, 0), (1999, 999), (150, 255, 0), 20)

#Define Rectangle
#             OBJECT  LEFT TOP  BOTTOM RIGHT    COLOR   THICKNESS
cv2.rectangle(image, (384, 0), (510, 128), (0, 255, 0), 3)

#Define Ellipse
#           OBJECT  CENTER      MAJOR/MIN START END THICKNESS AND COLOR
cv2.ellipse(image, (256, 256), (100, 50), 0, 0, 180, 255, -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))

#Define Polygon
#             OBJECT  POINTS ISCLOSE  COLOR
cv2.polylines(image, [pts], True, (0, 255, 255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'ROS OpenCV', (1000, 500), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("Image Window", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
