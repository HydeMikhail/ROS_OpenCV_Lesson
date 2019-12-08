#!/home/mhyde/vEnvs/rosPy/bin/python

'''
Run a WebCam Feed Using OpenCV

From the ROS course on Udemy:

https://www.udemy.com/course/ros-essentials/

'''

import sys
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

bridge = CvBridge()

def imageCallback(imageData):
    '''
    Recieves the image sensor data and converts it to an
    OpenCV format using CV Bridge
    '''
    #Convert ROS Image into OpenCV Image
    try:
        cvImage = bridge.imgmsg_to_cv2(imageData, "bgr8")
    except CvBridgeError as error:
        print error
    #Now ROS can work directly weith OpenCV

    (rows, cols, channels) = cvImage.shape
    if cols > 200 and rows > 200:
        cv2.circle(cvImage, (100, 100), 90, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(cvImage, "WebCam Activated with ROS + OpenCV",
                (10, 250), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Image Window", cvImage)
    cv2.waitKey(3)

def main(args):
    '''
    Main Function. Initializes the Subscriber Node for
    Image Processing
    '''
    rospy.init_node('image_converter', anonymous=True)
    rospy.Subscriber("/usb_cam/image_raw", Image, imageCallback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting Down ... "

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
