import cv2
import numpy as np
import imutils

# Copy the Path of the Video.
path = r"C:\Users\MD ARSLAAN\Desktop\Project 1\VIRAT_S_050201_05_000890_000944.mp4"

def mouseRGB(event,x,y,flag,param):
 if event == cv2.EVENT_FLAG_LBUTTON:
     colorB = frame[x,y,0]
     colorG = frame[x,y,1]
     colorR = frame[x,y,2]
     print("BGR Values : ",colorB,colorG,colorR)
     print("Corr",x,y)
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",mouseRGB)

# Create the Video Reader Object.
vid = cv2.VideoCapture(path)
print(vid)
print(vid.isOpened)
frame_counter=0
val,frame=vid.read()
cv2.imshow('Frame',frame)
while(1):
    if(cv2.waitKey(1)==ord('p')):
        break
# Close the Video and Windows.
vid.release()
cv2.destroyAllWindows()
