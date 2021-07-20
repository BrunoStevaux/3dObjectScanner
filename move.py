import os
from tqdm import tqdm
from shutil import copyfile

def move(folderPath, folderDate):
    # If there is a USB device with the name "3D"
    if(os.path.isdir("/media/pi/3D")):
        print("USB Drive Connected: 3D")
        print(f"Saving: {len(os.listdir(folderPath))} items")
        print("Your files are located here:")
        print(f"/media/pi/3D/{folderDate}")
        os.mkdir(r"/media/pi/3D/" + folderDate)

        for item in tqdm(os.listdir(folderPath), desc = "Copying photos to USB", unit = "photo"):
            copyfile(f"{folderPath}/{item}", f"/media/pi/3D/{folderDate}/{item}")

        print("Done!")
        os.system("sudo eject /dev/sda")
        print("USB Drive successfully unmounted.")

    else:
        print("No USB Drive Connected.")
        print("Your files are located here:")
        print(folderPath)