# -*- coding: utf-8 -*-
#
# Installation af MongoDB
#

import sys
from shutil import copyfile
from moduler.install_repo import install_repo
from moduler.apt_update import apt_update
from moduler.install_programs import install_program


def install_mongodb(configs):

    path = configs['Common']['path']
    # https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
    mongodb_release = configs['Common']['mongodb_release']
    lsb_mongodb = configs['Common']['lsb_mongodb']
    repo_key = f"https://www.mongodb.org/static/pgp/server-{mongodb_release}.asc"
    release = f"{lsb_mongodb}/mongodb-org/{mongodb_release}"
    sources_string = f"deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu {release} multiverse"
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
        print('MongoDB installeret')
        src = f"{path}/config/mongod.conf"
        dest = "/etc/mongod.conf"
        copyfile(src, dest)
    except Exception as err:
        print(err)
        print('Installationen af MongoDB fejlede')
