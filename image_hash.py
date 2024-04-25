import hashlib
import os
import cv2
import numpy as np
import random
import shutil

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{old_name}' not found.")
    except FileExistsError:
        print(f"Error: File '{new_name}' already exists.")
        
def move_file(source, destination):
    try:
        # Check if the source file exists
        if os.path.exists(source):
            # Check if the destination directory exists
            if os.path.exists(os.path.dirname(destination)):
                # Perform the move operation
                shutil.copy(source, destination)
                print(f"File moved from {source} to {destination}")
            else:
                print(f"Destination directory {os.path.dirname(destination)} does not exist")
        else:
            print(f"Source file {source} does not exist")
    except Exception as e:
        print(f"Error: {e}")

def random_change_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Get image dimensions
    height, width, channels = image.shape

    # Randomly select a type of change
    change_type = random.choice(['brightness', 'contrast', 'blur', 'color'])

    if change_type == 'brightness':
        # Generate a random brightness factor
        brightness_factor = random.uniform(0.5, 1.5)

        # Apply brightness change
        adjusted = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)
    
    elif change_type == 'contrast':
        # Generate a random contrast factor
        contrast_factor = random.uniform(0.5, 1.5)

        # Apply contrast change
        adjusted = cv2.convertScaleAbs(image, alpha=contrast_factor, beta=128 * (1 - contrast_factor))

    elif change_type == 'blur':
        # Generate a random blur level
        blur_level = random.randint(1, 5) * 2 + 1  # Ensure odd kernel size

        # Apply Gaussian blur
        adjusted = cv2.GaussianBlur(image, (blur_level, blur_level), 0)
    
    elif change_type == 'color':
        # Generate random intensity changes for each color channel
        color_delta = [random.randint(-50, 50) for _ in range(3)]

        # Apply color change
        adjusted = np.clip(image + np.array(color_delta), 0, 255).astype(np.uint8)

    return adjusted




def check_file_existence(directory, file_name):
    file_path = os.path.join(directory, file_name)
    if os.path.exists(file_path):
       return True
    else:
        return False

def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")

if __name__ == "__main__":
    directory_name = "example_directory"

    create_directory(directory_name)
    create_directory("Secure_Images")
    move_file("images.jpg","example_directory\images.jpg")
    if (check_file_existence(directory_name,"Kool-Aid_Man.png")):
        # Example usage:
        image_path = 'D:\Password Manager Project\example_directory\Kool-Aid_Man.png'  # Replace with your image path
        changed_image = random_change_image(image_path)

        # Display the original and changed images
        # Save the changed image
        cv2.imwrite('Secure_Images\pest.jpg', changed_image)

        print("Image saved successfully.")
    else:
        print("nud")
        
    
"""  
filename = "D:\Password Manager Project\Kool-Aid_Man.png"
with open(filename,"rb") as f:
    bytes = f.read() # read entire file as bytes
    readable_hash = hashlib.sha256(bytes).hexdigest()
    print(readable_hash)
   """ 