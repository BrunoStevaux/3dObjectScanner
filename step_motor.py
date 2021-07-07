import RPi.GPIO as gp
import time
import os

ROTATIONS = 512

def stepToDeg(num):
    # print(f"{num} steps = {(360.0 / ROTATIONS) * num} degs")
    return (360.0 / ROTATIONS) * num
    
def degToStep(num):
    # print(f"{num} degrees = {num / (360.0 / ROTATIONS)} steps")
    return  num / (360.0 / ROTATIONS)

class Motor():
    # 8 cycles = 1 revolution
    # 1/64 reduction
    # 8 * 64 = 512
    # controlPin = [6, 13 ,19,26]
    def __init__(self):
        gp.setmode(gp.BOARD)
        self.controlPin = [31,33,35,37]
        
        for pin in self.controlPin:
            gp.setup(pin, gp.OUT)
            gp.output(pin, 0)
        
        self.seq = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]
        
        self.ROTATIONS = 512
        self.STEPS = len(self.seq)
        self.degrees = 0
    def setup(self):
        gp.setmode(gp.BOARD)
        for pin in self.controlPin:
            gp.setup(pin, gp.OUT)
            gp.output(pin, 0)

    def clean():
        gp.cleanup()
 
    def rotate(self, cycles):
        self.setup()
        cycles = int(cycles)
        # totalPauses = degToStep(360.0 / photos)

        for _ in range(cycles):
            for step in range(self.STEPS):
                for pin in range(self.STEPS):
                    gp.output(self.controlPin[pin], self.seq[step][pin])
                time.sleep(0.002 )
        return cycles

def main():    
    motor = Motor()
    motor.setup()
    resolution = int(input("Resolution:\t"))
    stepsForResolution = degToStep(360.0 / resolution)
    # print(stepsForResolution)
    total = 0
    while(total < 512):
        if(total + stepsForResolution < 512):
            print("TAKING PHOTO")
            total += motor.rotate(stepsForResolution)
        else: 
            if (512-total) / 512 > 0.05:
                print(f"difference: {(512-total) / 512}")
                print("TAKING PHOTO")
                total += motor.rotate(stepsForResolution)
                
            else:
                print(f"NOT TAKING PHOTO. CORRECTING: {512-total} step(s)")
                total += motor.rotate(512-total)


        print(f"{total}/512, {int(stepToDeg(total))} degs")
        time.sleep(0.5)

    gp.cleanup()

if __name__ == "__main__":
    main()