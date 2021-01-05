# -*- coding: utf-8 -*-
#
#
from subprocess import run
from manjaro.packages import install_program
from moduler.vagrant_plugin import vagrant_plugins


def install_vagrant(configs):
    print('Installation af Vagrant ...')
    user = configs['Common']['user']
    try:
        install_program('vagrant')
        vagrant_plugins(configs)
    except OSError as err:
        print(err)
        print('Kunne ikke installere Vagrant')
        return
    else:
        print('Afsluttet installation af Vagrant')

