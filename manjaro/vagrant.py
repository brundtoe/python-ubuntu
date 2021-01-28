# -*- coding: utf-8 -*-
#
#
from manjaro.packages import install_program, is_installed
from moduler.vagrant_plugin import vagrant_plugins


def install_vagrant(configs):

    if is_installed('vagrant'):
        print('Vagrant er allerede installeret')
        return

    print('Installation af Vagrant ...')
    try:
        install_program('vagrant')
        vagrant_plugins(configs)
    except OSError as err:
        print(err)
        print('Kunne ikke installere Vagrant')
        return
    else:
        print('Afsluttet installation af Vagrant')
