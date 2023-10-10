import cv2
from PIL import Image
import os
import numpy as np
from ultralytics import YOLO
# Open the video file
video_path = "./video.mkv"
cap = cv2.VideoCapture(video_path)
model = YOLO('yolov8n.pt')
"""3,382
1,154
216,81
432,82
633,156
633,380"""

polygon_points = np.array([[3,382], [1,154], [216,81], [432,82], [633,156], [633,380]], np.int32)
# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        
        frame = cv2.resize(frame, (640, 384))
        # Draw the polygon on the image
        cv2.polylines(frame, [polygon_points], True, (0, 0, 255), 2)

        # Display the annotated frame
        model.predict(frame, show = True, save=False)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
