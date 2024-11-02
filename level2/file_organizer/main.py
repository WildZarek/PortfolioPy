# Script that Organizes Files into Directories
# by WildZarek ~ 2024

import glob
import os
import shutil

def file_organizer(target_directory: str) -> None:
    file_types = {
        "*.doc": "Documents",
        "*.txt": "Documents",
        "*.pdf": "Documents",
        "*.odt": "Documents",
        "*.rtf": "Documents",
        "*.bmp": "Images",
        "*.jpg": "Images",
        "*.jpeg": "Images",
        "*.gif": "Images",
        "*.png": "Images",
        "*.wav": "Audio",
        "*.mid": "Audio",
        "*.mp3": "Audio",
        "*.m4a": "Audio",
        "*.ogg": "Audio",
        "*.3gp": "Video",
        "*.avi": "Video",
        "*.mp4": "Video",
        "*.mpg": "Video",
        "*.mov": "Video"
        # Add more file types and folders as needed.
    }

    for pattern, folder in file_types.items():
        # Find all files matching the pattern
        for file_path in glob.glob(os.path.join(target_directory, pattern)):
            # Create the target folder if it doesn't exists
            target_folder = os.path.join(target_directory, folder)
            os.makedirs(target_folder, exist_ok=True)
            # Move the file to the target folder
            shutil.move(file_path, target_folder)
    else:
        print("No files matches any of the extensions defined.")

if __name__ == "__main__":
    target_directory = "." # Current path
    file_organizer(target_directory)