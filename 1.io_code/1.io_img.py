import os
import cv2

# read image
img = cv2.imread("Cow.jpg")

# write image
cv2.imwrite('cow_out.jpg', img)

# visualize image
cv2.imshow('Moooo', img)
cv2.waitKey(0)