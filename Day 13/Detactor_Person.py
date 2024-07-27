import cv2
import numpy as np
import imutils

# Copy the Path of the Video.
path = r"C:\Users\MD ARSLAAN\Desktop\Project 1\VIRAT_S_050201_05_000890_000944.mp4"



# Background Subtractor.
back_substractor = cv2.createBackgroundSubtractorKNN(dist2Threshold=8000)

# Create the Video Reader Object.
vid = cv2.VideoCapture(path)
if not vid.isOpened():
    print("Error: Could not open video.")
    exit()

frame_counter = 0
f = 0

while f <= 1000:
    f += 1
    ret, frame = vid.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Video Background Subtractions.
    mask_image = back_substractor.apply(frame)
    cnts = cv2.findContours(mask_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    final_contours = imutils.grab_contours(cnts)

    for c in final_contours:
        area = cv2.contourArea(c)
        if area > 100:
            print(area)
            M = cv2.moments(c)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                cv2.drawContours(frame, [c], -1, (0, 0, 255))

    cv2.imshow('mask', mask_image)
    cv2.imshow('original', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Close the Video and Windows.
vid.release()
cv2.destroyAllWindows()
