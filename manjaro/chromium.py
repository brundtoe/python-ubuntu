# -*- coding: utf-8 -*-
#
#

from manjaro.packages import install_program, is_installed


def install_chromium(configs):

    if is_installed('chromium'):
        print('Chromium er allerede installeret')
        return

    print('Installation af Chromium ...')
    try:
        install_program('chromium')

    except OSError as err:
        print(err)
        print('Kunne ikke installere Chromium')
        return
    else:
        print('Afsluttet installation af Chromium')
