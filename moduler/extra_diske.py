# -*- coding: utf-8 -*-
#
"""
Oprettelse af mount points og fstab for ekstra diske
"""

import os
import sys
import pwd

from moduler.fileOperations import add_line
from moduler.add_mountpoints import add_mountpoints


def disk_exists(disk_entry):
    disk_path = disk_entry[0:54]
    if os.path.exists(disk_path):
        # print(disk_entry)
        return True
    else:
        print(f'Oops disken {disk_path} ... findes IKKE')
        return False


def update_extradiske(configs):
    filename = '/etc/fstab'
    try:
        user = pwd.getpwuid(1000).pw_name
        host = configs['Common']['hostname']
        section = host if host in ['komplett', 'esprimo'] else 'other'
        mount_points = configs[section]
        add_mountpoints(user, mount_points)
        filename_extradiske = configs['Common']['filename_extradiske']
        with open(filename_extradiske) as src_file:
            for line in src_file:
                if disk_exists(line):
                    add_line(filename, line)
    except OSError as err:
        print(err)
        sys.exit('Kan ikke tilføje ekstra diske')
    else:
        print('De ekstra diske er mounted')
