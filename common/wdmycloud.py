#!../venv/bin/python
# Installation og konfiguration af Apache

import sys, os, shlex
import subprocess

from moduler.fileOperations import fetch_config
from moduler.smbcredentials import smbcredentials
from moduler.add_mountpoints import add_mountpoints

def add_line(filename, disk_entry):
    disk = disk_entry.split()
    # print(f'Tilføj .. {disk}')
    try:
        cmd = shlex.split(f'grep -qF "{disk[0]}" {filename}')
        res = subprocess.run(cmd)
        if res.returncode != 0:
            # print('så opdateres')
            cmd = shlex.split(f'sed -i "$a {disk_entry}" {filename}')
            res = subprocess.run(cmd)
            # print(res)
        else:
            print(f'Mount {disk[0]} ... findes allerede i fstab')
    except Exception as err:
        print(err)
        sys.exit(f'kan ikke opdatere fstab for disken {disk}')

# Tilføj mount point for wdmycloud
def update_mount_points(configs):
    try:
        mount_points = configs['mount.points']
        user = configs['Common']['user']
        add_mountpoints(user, mount_points)
    except Exception as err:
        sys.exit('Der opstod fejl ved tilføjelse af mount points for wdmycloud')
    else:
        print('Mount points for wdmycloud er tilføjet')


# Opdater smbcredentials med password til wdmycloud
def update_credentials(configs):
    try:
        user = configs['Common']['user']
        filename = '../config/.env_develop'
        password = fetch_config(filename)['Common']['password']
        smbcredentials(user, password)
    except Exception as err:
        sys.exit('Der opstod fejl ved opdatering af ~/.smbcredentials')
    else:
        print('~/.smbcredentials er opdateret med mountpoint')

def update_fstab(configs, filename, filename_disks):
    try:
        update_mount_points(configs)
        update_credentials(configs)

        with open(filename_disks) as src_file:
            for line in src_file:
                add_line(filename, line)
    except Exception as err:
        sys.exit('Der opstod fejl ved opdatering af wdmycloud')



if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres  med root access')
    print('Konfiguration af wdmycloud')
    configs = fetch_config('../config/config.ini')
    filename_disks = '../config/wdmycloud'
    filename = '/etc/fstab'
    update_fstab(configs, filename, filename_disks)
