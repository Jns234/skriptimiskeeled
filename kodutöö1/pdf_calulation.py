import os
import pathlib

HOME_DIR = os.environ['HOME'] 
# HOME_DIR = pathlib.Path.home()

def get_all_pdf_files(dir_path):
    """Returns a list of all .pdf files starting from a provided root dir."""
    files = []
    for path, subdirs, files in os.walk(dir_path):
        for name in files:
            if '.pdf' in name:
                files.append(os.path.join(path, name))

def calculate_size():
    """Prints out the size of all .pdf files in MegaBytes."""
    files = get_all_pdf_files(HOME_DIR)
    size = 0
    for file in files:
        file_stats = os.stat(file)
        size += file_stats.st_size
    print(f'File Size in MegaBytes is {size / (1024 * 1024)}')

calculate_size()