# -*- coding: utf-8 -*-
#
# Installation af nodejs og globale node packages
#

import shlex
import subprocess
from os import path

from moduler.apt_update import apt_update
from moduler.fileOperations import add_line
from moduler.install_programs import install_program
from moduler.install_repo import repokey_install


def install_nodejs(configs):

    if path.exists('/etc/apt/sources.list.d/nodesource.list'):
        print('Node.js er allerede installeret')
        return
    print('Installation af Node.js')
    version = configs['Common']['nodejs_release']
    release = configs['Common']['release']
    repo_key = "https://deb.nodesource.com/gpgkey/nodesource.gpg.key"
    repo_nodejs = f"https://deb.nodesource.com/node_{version} {release} main"

    try:
        repokey_install(repo_key)
        code = f'deb {repo_nodejs}\n'
        source = f'deb-src {repo_nodejs}\n'
        outfile = f'/etc/apt/sources.list.d/nodesource.list'
        add_line(outfile, code)
        add_line(outfile, source)
    except Exception as err:
        print(err)
        print('kunne ikke registrere node.js repository')
    else:
        print('Installerede node.js repository')

    options = configs['Common']['install_options']
    try:
        apt_update()
        install_program('nodejs', options)
        programs = "express-generator json-server nodemon pm2"
        cmd = shlex.split(f"npm install -g {programs}")
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as err:
        print(err)
        print('Kunne ikke opdatere systemet med nodejs og globalemoduler')
    print('Afsluttet installation af Node.js')