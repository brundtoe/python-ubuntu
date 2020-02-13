import sys, os, shutil
from moduler.fileOperations import fetch_config

def add_mountpoints(user,mount_points):
    for key in mount_points:
        path = mount_points[key]
        print(path)
        if not os.path.exists(path):
            os.makedirs(path)
        shutil.chown(path,user,user)

if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres med root access')

    filename = '../config/config.ini'
    configs = fetch_config(filename)
    mount_points = configs['mount.points']
    user = configs['Common']['user']
    add_mountpoints(user,mount_points)
