#!../venv/bin/python
# Installation og konfiguration af Apache

import sys, os, shlex
import subprocess

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


def update_fstab(filename, filename_disks):
    with open(filename_disks) as src_file:
        for line in src_file:
            add_line(filename, line)


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres  med root access')
    print('Konfiguration af wdmycloud')
    # configs = fetch_config('../config/config.ini')
    filename_disks = '../config/wdmycloud'
    filename = '/etc/fstab'
    update_fstab(filename, filename_disks)
