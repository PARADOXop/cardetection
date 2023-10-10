import cv2
import numpy as np
3,378
4,212
220,140
424,142
638,217
637,382

# Define the points to plot to form the polygon
polygon_points = np.array([[3,378], [4,212], [220,140], [424,142], [638,217], [637,382]], np.int32)

# Load the image

image_path = './train/frame_3.jpg'


image = cv2.imread(image_path)
image = cv2.resize(image, (640, 384))
# Draw the polygon on the image
cv2.polylines(image, [polygon_points], True, (0, 0, 255), 2)

# Display the image with the polygon
cv2.imshow('Image with Polygon', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
