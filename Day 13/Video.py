import cv2
import numpy as np
import matplotlib.pyplot as plt

# Copy the Path
path = r"C:\Users\MD ARSLAAN\Desktop\Project 1\vid_mpeg4.mp4"

# Create the video Reader Object
vid = cv2.VideoCapture(path)

print(vid)
print(vid.isOpened())

while(vid.isOpened()):
    val, frame = vid.read()
    # if the frame is Captured
    if val:
        gray_im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ycrcb_im = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        hsv_im = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        cv2.imshow('Gray', gray_im)
        cv2.imshow('YCrCb', ycrcb_im)
        cv2.imshow('HSV', hsv_im)
        cv2.imshow('Original', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()