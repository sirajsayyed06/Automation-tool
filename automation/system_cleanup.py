import os
from automation.utils import log

def clean_system(path):
    log("Running system cleanup...")

    removed = 0
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        os.remove(file_path)
        removed += 1

    log(f"System cleanup completed. Removed {removed} files.")
