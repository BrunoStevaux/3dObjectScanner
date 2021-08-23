from step_motor import *
from cam import *
from create_folder import *

from shutil import copyfile
import datetime, time
import os
import sys
from tqdm import tqdm

deg = 0
resolution = 0


if len(sys.argv) == 2:
    print("<resolution> <force degree>")
    resolution = int(sys.argv[1])
    deg = degToStep(360.0 / resolution)
elif len(sys.argv) == 3:
    print("<resolution> <force degree>")
    resolution = int(sys.argv[1])
    deg = int(sys.argv[2])
else:
    resolution = int(input("Resolution (1-100):\t"))
    #motor takes steps. not degrees. this converts from degrees to steps for you.
    deg = degToStep(360.0 / resolution)

folderPath, folderDate = create_folder(resolution)

# https://www.raspberrypi.org/documentation/raspbian/applications/camera.md
settings = "-ss 8000"

cameras = Camera()
motor = Motor()

for x in tqdm(range(1, resolution + 1), desc = "Capturing photos", unit = "4 photos"):
    cameras.Capture(name = x,
                    directory = folderPath,
                    settings = settings)
    motor.rotate(deg)
    time.sleep(1)

print(f"All finished. Your files are located here: {folderPath}")