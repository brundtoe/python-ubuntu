import sys, os
from moduler.fileOperations import addLine, fetch_config

def update_fstab(mount_string,mount_points,fstab):
    for key in fstab:
        line = f'{fstab[key]} {mount_points[key]} {mount_string}\n'
        addLine('/etc/fstab',line)

if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres med root access')

    filename = '../config/config.ini'
    configs = fetch_config(filename)
    mount_string = configs['Common']['mount_string']
    mount_points = configs['mount.points']
    fstab = configs['etc.fstab']
    update_fstab(mount_string,mount_points,fstab)