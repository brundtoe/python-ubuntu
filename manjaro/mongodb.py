# -*- coding: utf-8 -*-
#
#
import os
import shlex
from subprocess import run


def install_mongodb(configs):
    if os.geteuid() == 0:
        print('MongoDB kan ikke installeres med root access')
        return

    distro = configs['Common']['distribution']
    if distro == 'ubuntu':
        print('På Ubuntu skal installationen foretages fra systemmenuen')
        return

    if os.path.exists('/etc/apt/sources.list.d/mongodb.list'):
        print('MongoDB er allerede installereet')
        return

    project_path = configs['Common']['project_path']

    cmd = shlex.split('sudo pacman -Syu --needed base-devel')
    run(cmd)
    if run.returncode != 0:
        print('Systemopdatering fejlede')
        return
