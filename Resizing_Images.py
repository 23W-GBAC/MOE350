import os
from PIL import Image

def resize_images_in_folder(folder_path, new_size=(300, 200)):
    files = os.listdir(folder_path)
    image_files = [file for file in files if file.lower().endswith(('jpeg', 'jpg', 'png', 'gif', 'bmp'))]

    for file in image_files:
        file_path = os.path.join(folder_path, file)
        image = Image.open(file_path)
        print(f"Current size of {file}: {image.size}")
        resized_image = image.resize(new_size)
        new_filename = file.replace('.', '_resized.')
        new_file_path = os.path.join(folder_path, new_filename)
        resized_image.save(new_file_path)
        print(f"Resized image saved as {new_filename}")

# Get user input for folder path
folder_path = input("Enter the path to the folder containing your images: ")

# Get user input for new image size
width = int(input("Enter the desired width for the images: "))
height = int(input("Enter the desired height for the images: "))
new_size = (width, height)

# Resize images in the specified folder with user-defined size
print(f"\nProcessing images in folder: {folder_path}")
resize_images_in_folder(folder_path, new_size)
