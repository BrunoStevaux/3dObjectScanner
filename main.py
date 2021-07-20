from step_motor import *
from cam import *
from move import *
from create_folder import *

from shutil import copyfile
import datetime, time
import os
from tqdm import tqdm


resolution = int(input("Resolution (1-100):\t"))
#motor takes steps. not degrees. this converts from degrees to steps for you.
deg = degToStep(360.0 / resolution)

# checkFreeSpace returns FALSE if there is not enough space.
if not checkFreeSpace(resolution, usb = USB_connected()):
    exit(1)

folderPath, folderDate = create_folder()

# https://www.raspberrypi.org/documentation/raspbian/applications/camera.md
settings = " -r -t 1500 -ss 50000"

cameras = Camera()
motor = Motor()

for x in tqdm(range(1, resolution + 1), desc = "Capturing photos", unit = "4 photos"):
    cameras.Capture(name = x,
                    directory = folderPath,
                    settings = settings)
    motor.rotate(deg)
    time.sleep(1)

move(folderPath, folderDate)