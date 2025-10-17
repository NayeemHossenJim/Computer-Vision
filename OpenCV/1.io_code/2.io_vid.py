import os
import cv2

# read video
vid_path = os.path.join('..','Data','Cow.mp4')
video = cv2.VideoCapture(vid_path)

# visualize video
ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('Cute Cow', frame)
        cv2.waitKey(14)

video.release()
cv2.destroyAllWindows()