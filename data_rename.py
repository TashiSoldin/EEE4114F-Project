from PIL import Image
import os

source_folder = 'handdrawn_png\\resistor'
destination_folder = 'handdrawn_png\\resistor'

# specify the expected image extension 
extension = 'png'

image_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

for i, file_name in enumerate(image_files):

    # ensures that any hidden files (e.g. .DS_Store) are disregarded
    if file_name[-3:] == extension:
        # Open the image file
        image_path = os.path.join(source_folder, file_name)
        img = Image.open(image_path)

        # Generate the new name for the image using numbering
        new_file_name = f"{i+1}.png"  # Example: 1.jpg, 2.jpg, 3.jpg, ...

        # Generate the new path for the renamed image in the destination folder
        new_image_path = os.path.join(destination_folder, new_file_name)

        # Save the renamed image to the destination folder
        img.save(new_image_path)