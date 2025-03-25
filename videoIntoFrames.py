import sys
import argparse

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))  
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
        count = count + 1


#call the function
input_video_path = "C:/Users/zuhair.aziz/Desktop/python/damageTracker_project/video/sample1.mp4"
output_directory_path = "C:/Users/zuhair.aziz/Desktop/python/damageTracker_project/video/"

extractImages(input_video_path, output_directory_path)