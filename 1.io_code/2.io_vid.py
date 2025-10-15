import os
import cv2

# read video
video = cv2.VideoCapture("Cow.mp4")

# visualize video
ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('Cute Cow', frame)
        cv2.waitKey(14)

video.release()
cv2.destroyAllWindows()