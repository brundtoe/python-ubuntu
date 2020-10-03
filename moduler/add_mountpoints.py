#!/usr/bin/env python3
import sys, os, shutil
from moduler.fileOperations import fetch_config


def add_mountpoints(user, mount_points):
    """
    Add a directory with subdirectories to be used as mount points
    :param user: user accouten
    :param mount_points: liste fra configparser
    :return: void
    """
    try:
        for key in mount_points:
            path = mount_points[key]
            
            if not os.path.exists(path):
                os.makedirs(path)
                print(f'Oprettet {path}')
            else:
                print(f'Path {path} ... findes allerede')
            shutil.chown(path, user, user)
    except Exception as err:
        print(err)
        sys.exit('Kan ikke oprette mount points')


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres med root access')

    filename = '../config/config.ini'
    configs = fetch_config(filename)
    mount_points = configs['mount.points']
    user = configs['Common']['user']
    add_mountpoints(user, mount_points)
