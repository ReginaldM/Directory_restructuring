import os, re, shutil, subprocess
from pathlib import Path

moviesPath = Path.home()/"Videos"/"Movies"

for item in os.listdir(moviesPath): # Items in movies folder
    if os.path.isdir(moviesPath/item) and item != "Subs":

        for subItem in os.listdir(moviesPath/item): # iterating through the sub folder
            if subItem.endswith("srt"):
                # Move subs into the main Subs folder
                shutil.move(moviesPath/item/subItem, moviesPath/"Subs"/subItem)
            elif subItem.endswith("mp4"):
                # Move movies out to main Movies directory
                movieYear = re.findall("\d{4}", subItem)[0]
                movieName = re.split("\.\d{4}", subItem, 1)[0]
                movieTitle = f"{movieName.replace('.', ' ')} ({movieYear}).mp4"
                shutil.move(moviesPath/item/subItem, moviesPath/movieTitle)
            elif os.path.isdir(moviesPath/item/subItem) and subItem == "Subs":
                # Move the movies Subs into the main Subs folder 
                shutil.move(moviesPath/item/subItem, moviesPath/"Subs"/f'{item.split(")")[0]})')

        # Delete movie folder after moving out it's contents
        subprocess.run(f'rmdir /s/q "{moviesPath/item}/"', shell=True)
