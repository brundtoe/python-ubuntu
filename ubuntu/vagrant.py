# -*- coding: utf-8 -*-
#
# Installation af Vagrant
#
import re
import shlex
from subprocess import run, PIPE

from moduler.fileOperations import install_dpkg
from moduler.vagrant_plugin import vagrant_plugins


def install_vagrant(configs):

    # https://www.vagrantup.com/downloads.html
    version = configs['Common']['vagrant']
    url = f"https://releases.hashicorp.com/vagrant/{version}/vagrant_{version}_x86_64.deb"
    findes = None
    try:
        cmd = shlex.split('vagrant --version')
        res = run(cmd, stdout=PIPE, stderr=PIPE)
    except Exception as err:
        print(err)
        print('Vagrant skal installeres')
    else:
        findes = re.search(version, res.stdout.decode('UTF-8'))
    if findes is None:
        install_dpkg(url, version)
        vagrant_plugins(configs)
        print('Afsluttet installation af Vagrant')
    else:
        print('Vagrant er allerede installeret')
