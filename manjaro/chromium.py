# -*- coding: utf-8 -*-
#
#
from subprocess import run
from manjaro.packages import install_program

def install_chromium(configs):
    print('Installation af Chromium ...')
    try:
        install_program('chromium')

    except OSError as err:
        print(err)
        print('Kunne ikke installere Chromium')
        return
    else:
        print('Afsluttet installation af Chromium')

