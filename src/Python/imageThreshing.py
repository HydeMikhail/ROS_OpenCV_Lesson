#!/home/mhyde/vEnvs/rosPy/bin/python

'''
Simple example of image thresholding
in a ROS + OpenCV Environment
'''

import cv2

def readImage(imageName, asGray):
    '''
    Reads an image upon call in either
    grayscale or color
    '''
    if asGray:
        image = cv2.imread(imageName, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(imageName, cv2.IMREAD_COLOR)

    return image

def basicThresholding(grayImage, threshValue):
    '''
    Basic thresholding technique in image
    processing
    '''
    ret, threshBasic = cv2.threshold(grayImage,
                                     threshValue,
                                     255,
                                     cv2.THRESH_BINARY_INV)
    cv2.imshow("Basic Thresholding", threshBasic)

def adaptiveThresholding(grayImage, threshValue):
    '''
    Adaptive thresholding technique in image
    processing
    '''
    threshAdapt = cv2.adaptiveThreshold(grayImage,
                                        255,
                                        cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY_INV,
                                        threshValue,
                                        2)
    cv2.imshow("Adaptive Thresholding", threshAdapt)

def main():
    '''
    Main function to demonstrate each aforementioned thresholding
    technique
    '''
    imageName = "images/shapes.png"
    #imageName = "images/tomato.jpg"
    asGray = True
    threshValue = 115
    grayImage = readImage(imageName, asGray)
    basicThresholding(grayImage, threshValue)
    #adaptiveThresholding(grayImage, threshValue)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
