from step_motor import *
from cam import *
import time
import os

cameras = Camera()
motor = Motor()

resolution = int(input("Resolution (1-100):\t"))
#motor takes steps. not degrees. this converts from degrees to steps for u.
deg = degToStep(360.0 / resolution)

for x in range(resolution):
    cameras.Capture(name = x + 1)
    motor.rotate(deg)
    time.sleep(1)