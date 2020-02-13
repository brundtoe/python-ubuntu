# opret mount path

import os
import shutil

if __name__ == "__main__":
    mappe = '/home/training/jackie'
    print(os.path.isdir('/home/wdmycloud'))
    if not os.path.isdir(mappe):
        os.makedirs(mappe)
    shutil.chown(mappe, user= 1000, group=0)

