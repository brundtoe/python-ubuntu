#!../venv/bin/python


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

def update_fstab(configs, filename):
    try:
        user = configs['Common']['user']
        mount_points = configs[configs['Common']['host']]
        filename_extradiske = configs['Common']['filename_extradiske']
        print(user,mount_points,filename_extradiske)
        with open(filename_extradiske) as src_file:
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
    filename = '/etc/fstab'
    update_fstab(configs, filename)
