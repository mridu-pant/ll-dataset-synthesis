import os
import shutil
import random

# Set the source directory and the destination directories
source_directory = 'digiface'  # Replace with your source directory path
test_directory = 'test'

# List all subdirectories in the source directory
subdirectories = [d for d in os.listdir(source_directory) if os.path.isdir(os.path.join(source_directory, d))]

# Move subdirectories to the test directory
for subdir in subdirectories:
    source_subdir_path = os.path.join(source_directory, subdir)
    test_subdir_path = os.path.join(test_directory, subdir)
    os.makedirs(test_subdir_path, exist_ok=True)

    images = [img for img in os.listdir(source_subdir_path)]

    random_image = random.choice(images)
    
    src = os.path.join(source_subdir_path, random_image)
    dst = os.path.join(test_subdir_path, random_image)

    shutil.move(src, dst)

print("Successful")