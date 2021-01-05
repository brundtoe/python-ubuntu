# -*- coding: utf-8 -*-
#
#
import sys
import shlex
from subprocess import run
from manjaro.packages import install_program
from moduler.groups import usermod


def install_docker(configs):
    print('Installation af Docker ...')
    user = configs['Common']['user']
    try:
        install_program('docker')
        install_program('docker-compose')
        usermod(user, 'docker')
    except OSError as err:
        print(err)
        print('Kunne ikke installere Docker og docker-compose')
        return
    else:
        print('Afsluttet installation af Docker og docker-compose')
