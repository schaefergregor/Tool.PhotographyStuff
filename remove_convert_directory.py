"""
Remove folder in current filepath
"""
import os
import shutil

# get current path
dir_path = cwd = os.getcwd()
# get all subfolders
directories = os.listdir(dir_path)

# iterate folders
for directory in directories:
    if directory.startswith('.'):
        continue
    
    # create dir path
    current_dir = os.path.join(dir_path, directory)
    # append camera-subdir
    current_dir = os.path.join(current_dir, "camera")
    # check dir exists
    if not os.path.exists(current_dir):
        continue

    # append convert-subdir
    folder_to_delete = os.path.join(current_dir, "convert")
    # check dir exists
    if not os.path.exists(folder_to_delete):
        continue
    
    # remove folder
    print(folder_to_delete)
    shutil.rmtree(folder_to_delete)
        