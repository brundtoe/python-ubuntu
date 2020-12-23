# -*- coding: utf-8 -*-import sys
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

    cmd = shlex.split('vagrant --version')
    res = run(cmd, stdout=PIPE, stderr=PIPE)
    findes = re.search(version, res.stdout.decode('UTF-8'))
    if findes is None:
        install_dpkg(url, version)
        vagrant_plugins(configs)
    else:
        print('Vagrant er allerede installeret')
