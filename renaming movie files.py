import os, re, shutil
from pathlib import Path

moviesPath = Path.home()/"Videos"/"Movies"

for item in os.listdir(moviesPath): # In movies folder
    if os.path.isdir(moviesPath/item) and item != "Subs":
        for subItem in os.listdir(moviesPath/item): # sub folder (e.g. Fall 2022 folder)
            if subItem.endswith("srt"):
                os.replace(moviesPath/item/subItem, moviesPath/"Subs"/subItem)
            elif subItem.endswith("mp4"):
                movieYear = re.findall("\d{4}", subItem)[0]
                movieName = re.split("\.\d{4}", subItem, 1)[0]
                movieTitle = f"{movieName.replace('.', ' ')} ({movieYear}).mp4"
                os.replace(moviesPath/item/subItem, moviesPath/movieTitle)
            elif os.path.isdir(moviesPath/item/subItem) and subItem == "Subs":
                os.replace(moviesPath/item/subItem, moviesPath/"Subs"/f'{item.split(")")[0]})')
        # Delete the folder after moving out it's content
        shutil.rmtree(moviesPath/item)
