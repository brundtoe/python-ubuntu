# -*- coding: utf-8 -*-
#
#
import pwd
from manjaro.packages import install_program, is_installed
from moduler.groups import usermod


def install_docker(configs):

    if is_installed('docker'):
        print('Docker er allerede installeret')
        return

    print('Installation af Docker ...')
    user = pwd.getpwuid(1000).pw_name
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
