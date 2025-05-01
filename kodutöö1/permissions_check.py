import os
import pathlib
import datetime

CHECKED_DIR = "/home/ubuntu-machine/skriptimiskeeled/kodutöö1/testDir"
HOME_DIR = pathlib.Path.home()
LOG_FILE = "permission-control.log"
LOG_FILE_PATH = os.path.join(HOME_DIR, LOG_FILE)

def check_too_much_permissions(file_path):
    """Is given a file path and return true if it has too many permissions aka 777."""
    stat = os.stat(file_path)
    perm_value = oct(stat.st_mode)[-3:]
    if perm_value == "777":
        return True
    else:
        return False

def get_files_from_dir(dir_path):
    """Returns a list of files in a given directory."""
    files = []
    for file in os.listdir(dir_path):
        files.append(os.path.join(dir_path, file))
    return files

def log_file_event(file):
    """Adds a log line into the users HOME_DIR into the permission-control.log file about the file."""
    date = datetime.datetime.now()
    date_formatted = date.strftime("%Y-%m-%d %H:%M")
    event = f'{date_formatted} {file} privileged permissions were downgraded\n'
    try:
        with open(LOG_FILE_PATH, 'x') as file:
            file.write(event)
    except FileExistsError:
        with open(LOG_FILE_PATH, '+a') as file:
            file.write(event)


def check_files_in_dir(dir_path):
    """Checks all the files in a directory and initiates the change of permissions and logs."""
    files = get_files_from_dir(dir_path)
    for file in files:
        if check_too_much_permissions(file):
            os.chmod(file, 0o664)
            log_file_event(file)


#print(HOME_DIR)
#print(check_too_much_permissions(CHECKED_DIR + "/testTooMuchRights.txt"))
#print(check_too_much_permissions(CHECKED_DIR + "/testNoRights.txt"))

#print(get_files_from_dir(CHECKED_DIR))

print(check_files_in_dir(CHECKED_DIR))

#print(log_file_event("test"))