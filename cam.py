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
        gp.setwarnings(True)
        gp.setmode(gp.BOARD)
        gp.setup(7, gp.OUT)
        gp.setup(11, gp.OUT)
        gp.setup(12, gp.OUT)

    def setup(self):
        gp.setwarnings(True)
        gp.setmode(gp.BOARD)
        gp.setup(7, gp.OUT)
        gp.setup(11, gp.OUT)
        gp.setup(12, gp.OUT)

    def clean(self):
        gp.cleanup()

    def Capture(self, camera = "", name = ""):
        
        self.setup()
        name = str(name)
        
        if camera:
            print(f"Capturing: {name + camera}")
            cam = self.adapter_info.get(camera)
            # print(cam)
            if cam == None:
                print(f"Invalid camera: {cam}")
            os.system(cam["i2c"]) # i2c write
            gpio_sta = cam["gpio_sta"] # gpio write
            gp.output(7, gpio_sta[0])
            gp.output(11, gpio_sta[1])
            gp.output(12, gpio_sta[2])

            cmd = f"raspistill -t 1500 -ss 50000 -o capture_{name+camera}.jpg"
            os.system(cmd)
            print(" done")
            
        else:
            cameras = ["A", "B", "C", "D"]
            for cam in cameras: 
                print(f"Capturing: {name + cam}")
                camInfo = self.adapter_info.get(cam)
                # print(camInfo)
                if camInfo == None:
                    print(f"Invalid camera: {cam}")
                os.system(camInfo["i2c"]) # i2c write
                gpio_sta = camInfo["gpio_sta"] # gpio write
                gp.output(7, gpio_sta[0])
                gp.output(11, gpio_sta[1])
                gp.output(12, gpio_sta[2])

                cmd = f"raspistill -t 1500 -ss 50000 -o capture_{name+cam}.jpg"
                os.system(cmd)
                print(" done")  
        self.clean()

    def MultiCapture(num):
        for x in range(1, num):
            capture(name = num)