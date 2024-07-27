import cv2
import numpy as np
import matplotlib.pyplot as plt

# Copy the Path
path = r"C:\Users\MD ARSLAAN\Desktop\Project 1\vid_mpeg4.mp4"

#backGround Subtractor

back_gd =cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

back_subtractor=cv2.createBackgroundSubtractorMOG2()

# Create the video Reader Object
vid = cv2.VideoCapture(path)

print(vid)
print(vid.isOpened())

while(vid.isOpened()):
    val, frame = vid.read()
    
    mask_image=back_subtractor.apply(frame)
    cv2.imshow("mask",mask_image)
    cv2.imshow("original",frame)
    if(cv2.waitKey(1)==ord('q')):
        break
vid.release()
cv2.destroyAllWindows()