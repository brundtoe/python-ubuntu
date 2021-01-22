# -*- coding: utf-8 -*-
#
# Installation af MongoDB
#

import sys
from os import path
import distro
import shlex
from shutil import copyfile
import subprocess
from moduler.apt_update import apt_update
from moduler.install_programs import install_program
from moduler.install_repo import install_repo


def install_mongodb(configs):
    if path.exists('/usr/lib/systemd/system/mongod.service'):
        print('MongoDB er allerede installeret')
        return
    distrib = distro.linux_distribution(full_distribution_name=False)[0]
    project_path = configs['Common']['project_path']
    # https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
    mongodb_release = configs['Common']['mongodb_release']
    repo_key = f"https://www.mongodb.org/static/pgp/server-{mongodb_release}.asc"
    if distrib == 'ubuntu':
        lsb_mongodb_ubuntu = configs['Common']['lsb_mongodb_ubuntu']
        release = f"ubuntu {lsb_mongodb_ubuntu}/mongodb-org/{mongodb_release}"
        sources_string = f"deb [ arch=amd64 ] https://repo.mongodb.org/apt/{release} multiverse"
    else:
        lsb_mongodb_debian = configs['Common']['lsb_mongodb_debian']
        release = f"debian {lsb_mongodb_debian}/mongodb-org/{mongodb_release}"
        sources_string = f"deb https://repo.mongodb.org/apt/{release} main"
    program = 'mongodb'
    try:
        install_repo(repo_key, program, sources_string)
    except Exception as err:
        print(err)
        sys.exit(f'{program} repository er ikke installeret')
    else:
        print(f'{program} repository er installeret')

    options = configs['Common']['install_options']
    try:
        apt_update()
        install_program('mongodb-org', options)
        subprocess.run(shlex.split('systemctl stop mongod'))
        print('MongoDB installeret')
        src = f"{project_path}/config/mongod.conf"
        dest = "/etc/mongod.conf"
        copyfile(src, dest)
    except Exception as err:
        print(err)
        print('Installationen af MongoDB fejlede')
