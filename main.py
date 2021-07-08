from step_motor import *
from cam import *
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
    photoFolder = f"{destination}/{date}"
    photoFolder = photoFolder.replace(" ", "_")

    # If folder alreayd exists.
    if not os.path.isdir(photoFolder):
        os.mkdir(photoFolder)
    else:
        os.mkdir(photoFolder+ " (1)")

    return photoFolder

cameras = Camera()
motor = Motor()

resolution = int(input("Resolution (1-100):\t"))
#motor takes steps. not degrees. this converts from degrees to steps for u.
deg = degToStep(360.0 / resolution)

path = create_folder()

for x in range(resolution):
    cameras.Capture(name = x + 1,
                    directory=path)

    motor.rotate(deg)
    time.sleep(1)