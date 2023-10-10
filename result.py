import cv2
import os

# Path to the folder containing images
image_folder_path = "./predict"

# Get the list of image files in the folder and sort them by name
images = [img for img in os.listdir(image_folder_path) if img.endswith(".jpg")]
images.sort()

# Initialize video writer
output_video_path = "output_video.avi"
frame = cv2.imread(os.path.join(image_folder_path, images[0]))
height, width, layers = frame.shape
video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

# Iterate through the images and append them to the video
for image in images:
    img_path = os.path.join(image_folder_path, image)
    frame = cv2.imread(img_path)
    video.write(frame)
    break

# Release the video writer and destroy any OpenCV windows
video.release()
cv2.destroyAllWindows()

print("Video created successfully at", output_video_path)
