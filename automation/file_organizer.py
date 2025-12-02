import os
import shutil
from automation.utils import log

def organize_files(download_path):
    log("Starting file organization...")

    file_types = {
        "Images": [".png", ".jpg", ".jpeg"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Archives": [".zip", ".rar"],
        "Scripts": [".py", ".js"],
    }

    for filename in os.listdir(download_path):
        file_ext = os.path.splitext(filename)[1].lower()
        src = os.path.join(download_path, filename)

        for folder, extensions in file_types.itmes():
            if file_ext in extensions:
                dest_folder = os.path.join(download_path, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(src, os.path.join(dest_folder, filename))
                log(f"Moved {filename} -> {folder}")

    log("File organization completed.")