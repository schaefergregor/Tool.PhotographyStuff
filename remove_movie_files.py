"""
Remove movie files in subdirectories
"""
import os

# declare list of types
extenstions = (".mp4", ".MOV")
# get current path
dir_path = cwd = os.getcwd()
# get all subfolders
directories = os.listdir(dir_path)

def remove_movie_files(directory, subdirectory):
    # declare directory
    movie_directory = os.path.join(directory, subdirectory)
    # check dir exists
    if not os.path.exists(movie_directory):
        return

    for file in os.listdir(movie_directory):
        if file.endswith(extenstions):
            file_to_delete = os.path.join(movie_directory, file)
            print(file_to_delete)
            os.remove(file_to_delete)

# iterate folders
for directory in directories:
    if directory.startswith('.'):
        continue
    
    # remove camera movies
    remove_movie_files(os.path.join(dir_path, directory), "camera")
    # remove mobile movies
    remove_movie_files(os.path.join(dir_path, directory), "mobile")