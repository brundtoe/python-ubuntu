#!../venv/bin/python
# Installation og konfiguration af Apache

import sys, os, shlex
import subprocess

from moduler.fileOperations import fetch_config, isFound, addLine
from moduler.add_mountpoints import add_mountpoints

def disk_exists(disk_entry):
    disk_path = disk_entry[0:54]
    if os.path.exists(disk_path):
        # print(disk_entry)
        return True
    else:
        print(f'Oops disken {disk_path} ... findes IKKE')
        return False

def update_mount_point(configs):
    # Tilføj mount points for interne diske
    try:
        user = configs['Common']['user']
        mount_points = configs[configs['Common']['host']]
        add_mountpoints(user, mount_points)
    except Exception as err:
        sys.exit('Der opstod fejl ved tilføjelse af mount points for interne diske')
    else:
        print('Mount points for interne diske er tilføjet')

def update_fstab(configs, filename, filename_disks):
    try:
        update_mount_point(configs)
        with open(filename_disks) as src_file:
            for line in src_file:
                if disk_exists(line):
                   addLine(filename, line)
    except Exception as err:
        sys.exit('Kan ikke tilføje ekstra diske')


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres  med root access')
    print('Konfiguration af ekstra diske')
    configs = fetch_config('../config/config.ini')
    filename_disks = '../config/extradiske'
    #filename = '/home/jackie/Downloads/untitled'
    filename = '/etc/fstab'
    update_fstab(configs, filename, filename_disks)
