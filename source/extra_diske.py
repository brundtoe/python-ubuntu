#!/usr/bin/env python3
# Installation og konfiguration af Apache

import sys, os, shlex
import subprocess


def disk_exists(disk_entry):
    disk_path = disk_entry[0:54]
    if os.path.exists(disk_path):
        print(disk_entry)
        return True
    else:
        print(f'Oops disken {disk_path} findes IKKE')
        return False


def add_line(filename, disk_entry):
    disk = disk_entry[0:54]
    print(f'Tilføj .. {disk}')
    try:
        cmd = shlex.split(f'grep -qF "{disk}" {filename}')
        res = subprocess.run(cmd)
        if res.returncode != 0:
            #print('så opdateres')
            cmd = shlex.split(f'sed -i "$a {disk_entry}" {filename}')
            res = subprocess.run(cmd)
            #print(res)
        else:
            print('disken findes allerede i fstab')
    except Exception as err:
        print(err)
        sys.exit(f'kan ikke opdatere fstab for disken {disk}')


def update_fstab(filename, filename_disks):
    with open(filename_disks) as src_file:
        for line in src_file:
            if disk_exists(line):
                add_line(filename, line)
            else:
                print(f'Disken {line[0:54]}findes ikke')

if __name__ == '__main__':
    #    if os.geteuid() != 0:
    #       sys.exit('Scriptet skal udføres  med root access')
    print('Konfiguration af ekstra diske')
    # configs = fetch_config('../config/config.ini')
    filename_disks = '../config/extradiske'
    filename = '/home/jackie/Downloads/untitled'
    update_fstab(filename, filename_disks)
