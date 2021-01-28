# -*- coding: utf-8 -*-
#
#
from manjaro.packages import install_program, is_installed


def install_packer(configs):

    if is_installed('packer'):
        print('Packer er allerede installeret')
        return

    print('Installation af Packer ...')
    try:
        install_program('packer')

    except OSError as err:
        print(err)
        print('Kunne ikke installere Packer')
        return
    else:
        print('Afsluttet installation af Packer')
