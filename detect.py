import cv2
import os
import numpy as np
from PIL import Image
from ultralytics import YOLO
from shapely.geometry import Polygon

# Define the polygon points
polygon_points = np.array([[3, 382], [1, 154], [216, 81], [432, 82], [633, 156], [633, 380]])
output_folder = 'predict'
if not os.path.exists(output_folder):
        os.makedirs(output_folder)
# Convert the polygon points to a Shapely Polygon object
polygon = Polygon(polygon_points)

# Load the image

video_path = "./video.mkv"
cap = cv2.VideoCapture(video_path)

# Perform object detection using YOLO (replace with your YOLO model and detection logic)
# Assuming you have a model named 'model' from ultralytics.YOLO
model = YOLO()  # You should load your specific YOLO model
frame_count = 0
while cap.isOpened():
    # Read a frame from the video
    success, image = cap.read()

    if success:
        
        image = cv2.resize(image, (640, 384)) 
        cv2.polylines(image, [polygon_points], True, (0, 0, 255), 2) 
        results = model.predict(image, show=True, save=True, conf=0.4)

# Extract bounding box information
        objects_inside_polygon = []
        boxes = results[0].boxes.xywh.cpu()
        for box in boxes:
            x, y, w, h = box
            x_min = int(x - (w / 2))
            y_min = int(y - (h / 2))
            x_max = int(x + (w / 2))
            y_max = int(y + (h / 2))
            # Create a Shapely Polygon object for the bounding box
            bbox_polygon = Polygon([(x_min, y_min), (x_max, y_min), (x_min, y_max), (x_max, y_max)])

            # Check if the bounding box is within the polygon
            if bbox_polygon.within(polygon):
                objects_inside_polygon.append([x_min, y_min, x_max, y_max])

        # Draw bounding boxes for objects inside the polygon
        for obj in objects_inside_polygon:
            x_min, y_min, x_max, y_max = map(int, obj[:4])
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)  # Green rectangle
# Display the image with bounding boxes
        cv2.imshow('Objects Inside Polygon', image)
        frame_count += 1
        frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_filename, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

