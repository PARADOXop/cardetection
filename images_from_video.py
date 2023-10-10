import cv2
import os

def fetch_from_video(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    if not cap:
        print("Could not find video")
        return None
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    frame_count = 0
    while True:
        ret, frame = cap.read()

        # Break the loop if we have reached the end of the video
        if not ret:
            break
        
        frame = cv2.resize(frame, (640, 384))
        # Save the frame as an image
        frame_count += 1
        frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_filename, frame)

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

    print(f"Frames saved: {frame_count}")
    print("Frames saved in:", output_folder)



if __name__ == "__main__":
    video_path= 'video.mkv'
    output_folder= 'train'
    fetch_from_video(video_path, output_folder)
