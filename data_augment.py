# import the Python Image 
# processing Library
from PIL import Image
import os

# specify the source folder (kaggle dataset images) and destination folder where the rotated images will be saved
source_folder = 'input_png/capacitor'
destination_folder = 'input_png_rotated/capacitor'

# specify the expected image extension 
extension = 'png'

# retrieves images stored in the source folder to a image list
image_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# loops through each image list to apply rotation to each image in the source folder
for file_name in image_files:

    # ensures that any hidden files (e.g. .DS_Store) are disregarded
    if file_name[-3:] == extension:

        # opens the image file using the source folder file path and name of image
        image_path = os.path.join(source_folder, file_name)
        img = Image.open(image_path)

        # rotates the image by 90 degrees clockwise
        rotated_img = img.rotate(315)

        # specifies the destination folder where the rotated images will be stored and their image name
        destination_path = os.path.join(destination_folder, "315_degrees_"+ file_name)  

        # saves the rotated image to the destination folder
        rotated_img.save(destination_path)

