# -*- coding: utf-8 -*-
"""
@author:  Alfonso Blanco



"""
######################################################################
# PARAMETERS
#####################################################################
######################################################
# Video from https://github.com/anmspro/Traffic-Signal-Violation-Detection-System/tree/master/Resources
#dirVideo="Traffic IP Camera video.mp4"
dirVideo="project_video.mp4"

# in  14 minutes = 800 seconds finish  
TimeLimit=800
# Max number of Snapshots to consider a image
LimitSnapshot=1
# Max number of Snapshots to consider a image
# lower 3 snapshots is consider noisy

# to increase the speed of the process,
# even if some license plates are lost,
# only one snapshot out of every SpeedUpFrames is processed
SpeedUpFrames=60

# to increase speed, jump frames  
ContFramesJumped=0
fps=25 #frames per second of video dirvideo, see its properties
fpsReal= fps/SpeedUpFrames # To speed up the process only one of SpeedUpFrames
                           # is considered
                         
##############################################################
# DOWNLOAD VIDEOS TO TEST
###############################################################
# video from https://github.com/hasaan21/Car-Number-Plate-Recognition-Sysytem
#dirVideo="vid.mp4"

#dirVideo="video12.mp4"
#dirVideo="C:\\Car_Speed_Detection\\Comma.ai.Data.and.Model\\Comma.ai Model\\train.mp4"

# from https://www.pexels.com/video/video-of-famous-landmark-on-a-city-during-daytime-1721294/
#dirVideo="Pexels Videos 1721294.mp4"

#https://pixabay.com/es/videos/tr%C3%A1fico-coche-autopista-calle-27260/
#dirVideo= "traffic_-_27260 (540p).mp4"
# https://pixabay.com/es/videos/carros-autopista-velocidad-1900/
#dirVideo="car_-_2165 (540p).mp4"

# https://pixabay.com/es/videos/la-carretera-carril-arbolado-28287/
#dirVideo="road_-_28287 (540p).mp4"

import numpy as np

import cv2

import time

import math

TimeIni=time.time()


###########################################################
# MAIN
##########################################################

from Depth_anything_Cars_Yolo26 import estimar_distancia_coches

# A standard car width is assumed equal to the width of a parking space
# 2.3 meters
real_width=2.3


cap = cv2.VideoCapture(dirVideo)
     # https://levelup.gitconnected.com/opencv-python-reading-and-writing-images-and-videos-ed01669c660c

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
fps=5.0
frame_width = 680
frame_height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
     
video_writer = cv2.VideoWriter('demonstrationDepth.mp4',fourcc,fps, size)   
while (cap.isOpened()):
        ret, imgComplete = cap.read()
     
        if ret != True: break
        frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  
        frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  
        center_x = int(frame_width // 2)
        center_y = int(frame_height // 2)
        radius = min(center_x, center_y) - 30  # Radius of the circle where clock hands are drawn

        cv2.imwrite("pp.jpg", imgComplete)
        imageComplete=estimar_distancia_coches("pp.jpg")
        
        
        
        cv2.imshow("Webcam", imageComplete)
        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'): break 
        # saving video
        video_writer.write(imageComplete)    
        # a los 10 minutos = 600 segundos acaba     
        if time.time() - TimeIni > TimeLimit:       
            break
                
                    
cap.release()
video_writer.release()
cv2.destroyAllWindows()

     
    
print("")           
