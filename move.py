import os
import time
from tqdm import tqdm
from shutil import copyfile, disk_usage

def move(folderPath, folderDate):
    # If there is a USB device with the name "3D"
    if(os.path.isdir("/media/pi/3D")):
        print("USB Drive Connected: 3D")
        print(f"Saving: {len(os.listdir(folderPath))} items")
        os.mkdir(r"/media/pi/3D/" + folderDate)

        for item in tqdm(os.listdir(folderPath), desc = "Copying photos to USB", unit = "photo"):
            copyfile(f"{folderPath}/{item}", f"/media/pi/3D/{folderDate}/{item}")

        print("Your files are located here:")
        print(f"/media/pi/3D/{folderDate}")
        print("Done!")
        time.sleep(5)
        os.system("sudo eject /dev/sda")
        print("USB Drive successfully unmounted.")

    else:
        print("No USB Drive Connected.")
        print("Your files are located here:")
        print(folderPath)

def USB_connected():
    return os.path.isdir("/media/pi/3D")

# 1Gb = 1,000,000,000
# 1Mb = 1,000,000
# 1Kb = 1,000
# 1b  = 1

def checkFreeSpace(amount, usb=False, raw=False):
    pi_total, pi_used, pi_free = disk_usage("/")
    usb_total, usb_used, usb_free = 0, 0, 0
    if usb:
        usb_total, usb_used, usb_free = disk_usage("/media/pi/3D")
    
    MB = (1000 ** 2)
    if raw:
        photo = 16 * MB
    else:
        photo = 5 * MB

    needed = photo * (amount * 4)

    print(f"Space needed:        {needed // MB} Mb")
    print(f"Free space on pi:    {pi_free // MB} Mb")
    print(f"Free space on USB:   {usb_free // MB} Mb")

    if(pi_free < needed or usb_free < needed):
        print(f"Not enough space. Please free {(needed - pi_free) // MB} Mb")
        return False
    
    return True