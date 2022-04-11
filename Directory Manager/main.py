import os
import shutil
import argparse
import configparser

# Reading config.ini from within root directory for the script
config = configparser.ConfigParser()
try:
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))
except Exception as e:
    print("Error: Could not read config.ini")
    print(e)
    exit()

# Retrieving the path to start working on using -p/--path options when launching the script
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required = True, help = "Enter path to manage")
args = vars(ap.parse_args())
source = args['path']

# Retrieving the collapsed setting from settings section
collapsed = config.getboolean('Settings', 'Collapsed')


# Set destination to either a collapsed mode with a main directory and the aforementioned directories in the configuration file's FolderMapping section to avoid overlapping
# OR 
# Set destination to an expanded mode with all the directories in the entered path to the --path command
__maindest__ = source
if(collapsed):
    __maindest__ = source + '\\DirectoryManager'
    if not os.path.exists(__maindest__):
        os.makedirs(__maindest__)

# Pre-creation of the destination folders (Will be deleted if any of them ended up empty)
folders = config['FolderMapping']

for key in folders:
    destination = __maindest__  + '\\' + folders[key]
    if not os.path.exists(destination):
        os.makedirs(destination)

# Grab file extensions to work on
extensions = config['SupportedExtensions']

# Counters for stats
file_count = 0
file_counts = {}

# Move files from source to destination
for files in os.listdir(source):
    for key in extensions:
        if(files.endswith('.' + key)):
            file_count += 1
            if(key in file_counts.keys()):
                file_counts[key] += 1
            else:
                file_counts[key] = 1
            try:
                destination = __maindest__ + '\\' + folders[extensions[key]]
                shutil.move(source + '\\' + files, destination)
                break
            except:
                print("File already exists in destination or doesn't exist in source.")
                exit()

# Check if any of the created folders are empty and remove them
for files in os.listdir(__maindest__):
    path = __maindest__ + '\\' + files
    if(os.path.isdir(path)):
        if(files in folders.values() and len(os.listdir(path)) <= 0):
            try:
                os.rmdir(path)
            except:
                print("Error occured while deleting an empty directory, please check the directory.")
                print("Path: " + path)
                exit()


# Print out some stats for nerds
stats = config.getboolean('Settings', 'Stats')

if(stats):
    c = 0
    if(file_count > 0):
        print("\nMoved", end = ' ')
    for (key, value) in file_counts.items():
        print(str(value) + ' ' + key , end = ' ')
        if((c + 1) % 3 == 0 and c < len(file_counts) - 1):
            print("\nMoved", end = ' ')
        c += 1
    print("\n\nOrganised " + str(file_count) + " total files, Have fun =)")