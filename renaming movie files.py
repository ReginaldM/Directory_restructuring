import os, re, shutil, subprocess
from pathlib import Path, WindowsPath

moviesPath = Path.home()/"Videos"/"Movies"

for item in os.listdir(moviesPath): # Items in movies folder
    if os.path.isdir(moviesPath/item) and item != "Subs":

        for subItem in os.listdir(moviesPath/item): # sub folder (e.g. inside Fall 2022 folder)
            if subItem.endswith("srt"):
                os.replace(moviesPath/item/subItem, moviesPath/"Subs"/subItem)
            elif subItem.endswith("mp4"):
                movieYear = re.findall("\d{4}", subItem)[0]
                movieName = re.split("\.\d{4}", subItem, 1)[0]
                movieTitle = f"{movieName.replace('.', ' ')} ({movieYear}).mp4"
                os.replace(moviesPath/item/subItem, moviesPath/movieTitle)
            elif os.path.isdir(moviesPath/item/subItem) and subItem == "Subs":
                shutil.move(moviesPath/item/subItem, moviesPath/"Subs"/f'{item.split(")")[0]})')
        # Delete the folder after moving out it's content
        # print(f"rmdir /s/q '{WindowsPath(moviesPath/item)}\\'")
        # subprocess.run(f"rmdir /s/q '{moviesPath/item}\\'", shell=True)
        # shutil.rmtree(moviesPath/item)
