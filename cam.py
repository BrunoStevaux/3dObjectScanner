import RPi.GPIO as gp
import os
import time

class Camera:
    adapter_info = {
        "A":{   "i2c":"i2cset -y 1 0x70 0x00 0x04",
                "gpio_sta":[0,0,1],
            },
        "B":{   "i2c":"i2cset -y 1 0x70 0x00 0x05",
                "gpio_sta":[1,0,1],
            },
        "C":{   "i2c":"i2cset -y 1 0x70 0x00 0x06",
                "gpio_sta":[0,1,0],
            },
        "D":{   "i2c":"i2cset -y 1 0x70 0x00 0x07",
                "gpio_sta":[1,1,0],
            },
        } 

    def __init__(self):
        self.setup()

    def setup(self):
        # Set the board
        gp.setwarnings(True)
        gp.setmode(gp.BOARD)
        gp.setup(7, gp.OUT)
        gp.setup(11, gp.OUT)
        gp.setup(12, gp.OUT)

    def clean(self):
        # Clean
        gp.cleanup()

    def Capture(self, camera = "", name = "", directory = None, settings = None):
        if settings == None:
            settings = "-r -t 1500 -ss 50000"
        if directory == None:
            print("Supply a directory.")
            exit(0)

        # Setup board
        self.setup()
        name = str(name)
        
        # Single camera capture
        if camera:
            # print(f"Capturing: {name + camera}", end = "", flush = True)
            cam = self.adapter_info.get(camera)
            # print(cam)
            if cam == None:
                print(f"Invalid camera: {cam}")
            os.system(cam["i2c"]) # i2c write
            gpio_sta = cam["gpio_sta"] # gpio write
            gp.output(7, gpio_sta[0])
            gp.output(11, gpio_sta[1])
            gp.output(12, gpio_sta[2])

            cmd = f"raspistill {settings} -o {directory}/capture_{name+camera}.jpg"
            os.system(cmd)
            # print(" done")

        # Multi camera capture    
        else:
            cameras = ["A", "B", "C", "D"]
            # print("Capturing: xx", end = "", flush = True)

            # A B C D cameras
            for cam in cameras: 
                camInfo = self.adapter_info.get(cam)

                if camInfo == None:
                    print(f"Invalid camera: {cam}")

                os.system(camInfo["i2c"]) # i2c write
                gpio_sta = camInfo["gpio_sta"] # gpio write
                gp.output(7, gpio_sta[0])
                gp.output(11, gpio_sta[1])
                gp.output(12, gpio_sta[2])

                # Update print command
                # print(f"\b\b{name+cam}", end = "", flush=True)
                # Take the photo
                cmd = f"raspistill {settings} -o {directory}/capture_{name+cam}.jpg"
                os.system(cmd)
            
            # print(f" \b\b done")  
        self.clean()