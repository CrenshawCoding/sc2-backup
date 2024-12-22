# How to use

## Prerequisites:
- An empty folder in your onedrive/google drive/dropbox/where ever that files can be moved to for backup. (e.g. `C:/Users/user/OneDrive/Backup/starcraft`)

## Installation
1. Download `sc2-backup.zip` from the [releases](https://github.com/CrenshawCoding/sc2-backup/releases) and unzip the contents somewhere of your chosing, e.g. somewhere in `C:\Program Files`.
2. Open the `config.json` found in the unzipped directory.
![img](https://i.imgur.com/WjcByOK.png)
3. Replace `path/to/backup/dir` with the path to your backup directory (e.g `C:/Users/user/OneDrive/Backup/starcraft`) ❗**This folder should be empty, as my script deletes things in there**
4. Set `keep amount` to the number of backup files you want to keep at any time (older ones will be deleted when a new one is created).
5. Replace `path/to/documents/starcraft` with the path to your starcraft 2 documents folder (e.g. `C:/Users/user/Documents/StarCraft II`)
6. Right-click the `sc2-backup.exe` and select "create shortcut".
7. Press the `win` + `r` (or use the windows search for "run") and enter `shell:startup`. This will open the windows autostart folder.
8. Move the shortcut created in step 6 into this folder. It'll look like this (Sorry for the German screenshot):
![img](https://i.imgur.com/kNiFPRl.png)

Et voilà youre done. The program will now create a backup from your sc2 folder and move it to the backup directory every time you start your PC.
