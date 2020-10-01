#!/usr/bin/env python3
#
import sys, os
from fileOperations import addLine, fetch_config


def update_fstab(mount_string, mount_points, fstab):
    """
    Opdater mount point i fstab
    :param mount_string: mountstring til wdmycloud
    :param mount_points: mount punktet på den interne disk
    :param fstab: ref til wdmycloud partitioner
    :return:
    """
    try:
        line = ''
        for key in fstab:
            line = f'{fstab[key]} {mount_points[key]} {mount_string}\n'
            addLine('/etc/fstab', line)
    except Exception as err:
        print(err)
        sys.exit(f'Kan ikke opette {line} i /etc/fstab')


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres med root access')

    filename = '../../config/manjaro.ini'
    configs = fetch_config(filename)
    mount_string = configs['Common']['mount_string']
    mount_points = configs['mount.points']
    fstab = configs['etc.fstab']
    update_fstab(mount_string, mount_points, fstab)
