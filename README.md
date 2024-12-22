# How to use

## Prerequisites:
- [python 3](https://www.python.org/) installation
- An empty folder in your onedrive/google drive/dropbox/where ever that files can be moved to for backup.

## Installation
1. Unzip the contents of the [release](https://github.com/CrenshawCoding/sc2-backup/releases/tag/1.1) somewhere of your chosing.
2. Open the config.json
3. Replace `path/to/backup/dir` with the path to your backup directory (e.g `C:/Users/user/OneDrive/Backup/starcraft`) ❗**This folder should be empty, as my script deletes things in there**
4. Set `keep amount` to the number of backup files you want to keep at any time (older ones will be deleted when a new one is created)
5. Replace `path/to/documents/starcraft` with the path to your starcraft 2 documents folder (e.g. `C:/Users/user/Documents/StarCraft II`)

Executing the script now from a terminal via `python main.pyw` will create a zip file backup and manage the files in the backup directory.

## Automated execution (sorry for the German screenshots)

1. Press `windows key` + `r` and enter `taskschd.msc`
2. Right click below the existing tasks (if any) and select "create new task")

![grafik](https://github.com/CrenshawCoding/sc2-backup/assets/45495757/500e9a99-34d5-40ae-9fb1-0efa6812ad83)
4. Give it a name

![grafik](https://github.com/CrenshawCoding/sc2-backup/assets/45495757/857c72bc-9a71-40f2-bfc2-3433544ee607)

5. Go to Trigger
6. Click "New..."
7. Configure it to your liking (The following screenshots are for a schedule that runs once every day or as soon as the PC turns on)

![grafik](https://github.com/CrenshawCoding/sc2-backup/assets/45495757/589667c5-4eba-4b28-a736-ec0e95f1e17c)
![grafik](https://github.com/CrenshawCoding/sc2-backup/assets/45495757/8454e0df-422d-44d5-ac4f-372668aa2743)

8. Go to "Actions"
9. Press "New..." and select "start program"
10. Enter the path to your pythonw.exe under `Program/Script` (e.g. `C:\Users\user\AppData\Local\Programs\Python\Python311\pythonw.exe`)
11. Enter the path to the downloaded main.pyw under `arguments` (e.g. `C:\Users\user\PycharmProjects\sc2-backup\main.pyw`)
12. Enter the path to the ❗***FOLDER*** ❗ that contains the downloaded program under `start in` (e.g. `C:\Users\user\PycharmProjects\sc2-backup\`) ❗this should be the same path that you entered last without `main.pyw`❗

![grafik](https://github.com/CrenshawCoding/sc2-backup/assets/45495757/b63c5b83-1acc-4b63-a7f2-52e2a957c13b)
![grafik](https://github.com/CrenshawCoding/sc2-backup/assets/45495757/67ee0e3f-1dbe-414f-bf69-d73ef7f0f4e6)

Phew that's it. Now it will run automatically at the point in time you configured.

> ℹ️ if you want to copy my config and have it backup once you start the PC you also need to go to Settings and activate "Execute as soon as possible after a missed start" or whatever it is in English.
