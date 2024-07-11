from PIL import Image as image, ImageFilter as imagefilter
import sys
import os

# Getting arguments from command line
images_dir = sys.argv[1]
to_path = sys.argv[2]

# Create the folder if it doesn't exist
if not os.path.exists(to_path):
    os.mkdir(to_path)

# Check if the source directory exists
if not os.path.exists(images_dir):
    print('No such directory')
else:
    # Check if the source directory is empty
    if not os.listdir(images_dir):
        print('Folder is empty')
    else:
        # Loop through each file in the directory
        for file in os.listdir(images_dir):
            # Get the full file path
            full_file_path = os.path.join(images_dir, file)
            
            # Check if the file is a .png file
            if not file.endswith(".png"):
                try:
                    # Create new file name with .png extension
                    f, e = os.path.splitext(file)
                    new_file_name = f + '.png'
                    new_file_path = os.path.join(to_path, new_file_name)

                    # Open the image file
                    with image.open(full_file_path) as im:
                        # Save the image in the new format
                        im.save(new_file_path)
                except Exception as e:
                    print(f"Failed converting {file} to .png file: {e}")
            else:
                print(f"{file} is already in the right format")

