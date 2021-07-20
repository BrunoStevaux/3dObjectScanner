import datetime, time
import os

def create_folder():
    # Get the current working directory
    directory = os.getcwd()
    destination = f"{directory}/Scans"

    # Create a /Scans folder if there isn't one.
    if not os.path.isdir(destination):
        os.mkdir(destination)

    # Create a folder with the current time
    date = datetime.datetime.fromtimestamp(int(time.time()))
    date = str(date).replace(" ", "_")
    date = date.replace(":","-")
    photoFolder = f"{destination}/{date}"

    # If folder alreayd exists.
    if not os.path.isdir(photoFolder):
        os.mkdir(photoFolder)
    else:
        os.mkdir(photoFolder+ " (1)")

    return photoFolder, date
