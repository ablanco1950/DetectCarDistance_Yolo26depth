# DetectCarDistance_Yolo26depth

Detects the distance between a camera and a car using yolo26n-depth.pt model from ultralytics

Requirements:

pip install ultralytics opencv-python numpy

It is important to have the latest version of Ultralytics; otherwise, the recently developed YOLO26 modules will not be found.

pip install --upgrade ultralytics

Test:

Download the project to disk and run:

python VIDEODetectCarDepth_Yolo26.py


A demonstrationDepth.mp4 file is generated with the test results.

You can replace the video referenced in line 14 with any other; in the code there are some references indicating where you can download videos.

This project with yolo26 represents a significant improvement in terms of speed and car detection comparing with https://github.com/ablanco1950/DetectCarDistance_Depth-Anything-V2-Metric-Outdoor-Small-hf


References

https://docs.ultralytics.com/tasks/depth

https://github.com/ablanco1950/DetectCarDistance_Depth-Anything-V2-Metric-Outdoor-Small-hf

https://github.com/ablanco1950/DetectCarDistanceAndRoadLane


