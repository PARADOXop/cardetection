from PIL import Image
import os

def resize_images(input_folder, output_folder=None, target_width=640, target_height=384):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Process each file
    for file in files:
        # Check if the file is an image (supports jpg, png, etc.)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)

            # Open the image
            with Image.open(input_path) as img:
                # Resize the image while maintaining the aspect ratio
                resized_img = img.resize((target_width, target_height), Image.LANCZOS)

                # Save the resized image
                resized_img.save(output_path)

if __name__ == "__main__":
    # Input folder containing the images
    input_folder = "train"

    # Output folder to save resized images
    output_folder = "train"

    # Target width for resizing
    target_width = 640

    # Resize images in the input folder and save them in the output folder
    resize_images(input_folder, output_folder, target_width)
