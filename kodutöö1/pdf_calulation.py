import os
import pathlib

#HOME_DIR = os.environ['HOME'] 
HOME_DIR = pathlib.Path.home()

def get_all_pdf_files(dir_path):
    """Returns a list of all .pdf files starting from a root dir."""
    files = []
    for path, subdirs, files in os.walk(dir_path):
        for name in files:
            if '.pdf' in name:
                files.append(os.path.join(path, name))

get_all_pdf_files(HOME_DIR)