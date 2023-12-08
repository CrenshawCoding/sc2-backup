import json
import shutil
from datetime import datetime
import os

# Config
starcraft_location = ""
backup_location = ""
keep_amount = 0
with open('./config.json') as config_file:
    config = json.load(config_file)
    backup_location = str(config['backupLocation'])
    keep_amount = int(config['keepAmount'])
    starcraft_location = str(config['starcraftLocation'])
    if not os.path.isdir(backup_location):
        raise Exception(backup_location + " ist kein Verzeichnis auf diesem System. Prüfe die config.json datei.")
    if not os.path.isdir(starcraft_location):
        raise Exception(starcraft_location + " ist kein Verzeichnis auf diesem System. Prüfe die config.json datei.")

# Create zip file
created_file = shutil.make_archive("Starcraft II_" + datetime.now().strftime('%Y%m%dT%H%M%S'), 'zip', starcraft_location)
print("Created " + created_file)

# Move it to backup directory
print('Moving', created_file, 'to', backup_location)
shutil.move(created_file, backup_location)
