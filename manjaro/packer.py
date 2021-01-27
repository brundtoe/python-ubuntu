# -*- coding: utf-8 -*-
#
#
from manjaro.packages import install_program


def install_packer(configs):
    print('Installation af Packer ...')
    try:
        install_program('packer')

    except OSError as err:
        print(err)
        print('Kunne ikke installere Packer')
        return
    else:
        print('Afsluttet installation af Packer')
