import os
import cv2

# read image
img_path = os.path.join('..','Data','Cow.jpg')
img = cv2.imread(img_path)

# write image
cv2.imwrite('cow_out.jpg', img)

# visualize image
cv2.imshow('Moooo', img)
cv2.waitKey(0)