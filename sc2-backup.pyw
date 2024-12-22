import json
import shutil
from datetime import datetime
import os
import pathlib

backup_file_prefix = "Starcraft II"

config_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "config.json")
if not os.path.isfile(config_file):
    raise Exception("Config file not found.", config_file)
# Config
with open(config_file) as file_content:
    config = json.load(file_content)
    backup_location = str(config['backupLocation'])
    keep_amount = int(config['keepAmount'])
    starcraft_location = str(config['starcraftLocation'])
    if not os.path.isdir(backup_location):
        raise Exception(backup_location + " Is not a directory in this file system. Check your config.json file.")
    if not os.path.isdir(starcraft_location):
        raise Exception(starcraft_location + " Is not a directory in this file system. Check your config.json file.")

print("Creating zip file")

# Create zip file
created_file = shutil.make_archive(backup_file_prefix + "_" + datetime.now().strftime('%Y%m%dT%H%M%S'), 'zip',
                                   starcraft_location)
print("Created " + created_file)

# Move it to backup directory
print('Moving', created_file, 'to', backup_location)
shutil.move(created_file, backup_location)

# Cleaning up backup directory
if keep_amount != 0:
    dir_content = os.listdir(backup_location)
    temp = list(map(lambda file_name: os.path.join(backup_location, file_name), dir_content))
    filtered = list(filter(lambda o: os.path.isfile(o), temp))
    if len(filtered) > keep_amount:
        filtered.sort()
        to_delete = filtered[0:len(filtered) - keep_amount]
        for file in to_delete:
            file_name = os.path.basename(file)
            if file_name.startswith(backup_file_prefix) and file_name.endswith(".zip"):
                print('Deleting', file)
                os.remove(file)
