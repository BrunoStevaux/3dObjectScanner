from step_motor import *
from cam import *
from move import *
from create_folder import *

from shutil import copyfile
import datetime, time
import os
from tqdm import tqdm

cameras = Camera()
motor = Motor()

resolution = int(input("Resolution (1-100):\t"))
#motor takes steps. not degrees. this converts from degrees to steps for u.
deg = degToStep(360.0 / resolution)

folderPath, folderDate = create_folder()

settings = "-t 1500 -ss 50000"

for x in tqdm(range(1, resolution + 1), desc = "Capturing photos", unit = "4 photos"):
    cameras.Capture(name = x,
                    directory = folderPath,
                    settings = settings)
    motor.rotate(deg)
    time.sleep(1)

move(folderPath, folderDate)