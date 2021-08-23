import datetime, time
import os
from shutil import disk_usage

def create_folder(resolution):
    # Get the directory from user
    directory = drive(resolution)
    destination = f"{directory}/Scans"

    # Create a /Scans folder if there isn't one.
    if not os.path.isdir(destination):
        os.mkdir(destination)

    # Create a folder with the current time
    date = datetime.datetime.fromtimestamp(int(time.time()))
    date = str(date).replace(" ", "_")
    date = date.replace(":","-")
    photoFolder = f"{destination}/{date}"

    # If folder already exists..? It shouldn't, but what IF..
    if not os.path.isdir(photoFolder):
        os.mkdir(photoFolder)
    else:
        os.mkdir(photoFolder+ " (1)")

    return photoFolder, date


def drive(resolution):
    MB = (1000 ** 2)
    PHOTO = 4 * 5 * MB # 5Mb per photo, 4 photos per capture.

    drives = os.listdir("/media/pi/")
    if len(drives) < 1:
        print("No drives detected.")
        exit(0)
    elif len(drives) == 1:
        #Check free space
        usb_total, usb_used, usb_free = disk_usage(f"/media/pi/{drives[0]}")
        if(usb_free < (resolution * PHOTO)):
            print("Not enough free space!")
            exit(0)
        
        # Format with decimals.
        print(f"({'{:,}'.format(usb_free // MB)} Mb free | {'{:,}'.format(resolution * (PHOTO // MB))} Mb needed)")
        return (f"/media/pi/{drives[0]}")
         
    print("CONNECTED DRIVES")
    for x, drive in enumerate(drives):
        usb_total, usb_used, usb_free = disk_usage(f"/media/pi/{drive}")
        print(f"{x + 1}: {drive} -\t({'{:,}'.format(usb_free // MB)} Mb free | {'{:,}'.format(resolution * (PHOTO // MB))} Mb needed)")
        # Warn about free space
        if(usb_free < (resolution * PHOTO)):
            print("Not enough free space!")

    # If drive index is not there
    d = int(input("Select a drive:\t")) - 1
    if d >= len(drives):
        print("Invalid drive.")
        exit(0)

    return (f"/media/pi/{drives[d]}")

if __name__ == "__main__":
    # Test case
    print(drive(100))