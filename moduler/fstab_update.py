# -*- coding: utf-8 -*-

#
import sys
from moduler.fileOperations import add_line


def update_fstab(mount_string, mount_points, fstab):
    """
    Opdater mount point i fstab
    :param mount_string: mountstring til wdmycloud
    :param mount_points: mount punktet på den interne disk
    :param fstab: ref til wdmycloud partitioner
    :return:
    """
    line = ''
    try:
        for key in fstab:
            line = f'{fstab[key]} {mount_points[key]} {mount_string}\n'
            add_line('/etc/fstab', line)
    except Exception as err:
        print(err)
        sys.exit(f'Kan ikke opette {line} i /etc/fstab')
