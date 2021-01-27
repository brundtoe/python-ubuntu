# -*- coding: utf-8 -*-
#
#
import sys
from moduler.apt_update import apt_update
from moduler.install_programs import install_programs


def install_packages(configs):
    print('Installaton af sw packages')
    try:
        apt_update()
    except OSError as err:
        print(err)
        sys.exit('Der opstod fejl ved opdatering af systemet med apt update')
    else:
        print('apt-get update og apt-get upgrade udført')

    try:
        programs = configs['programs']
        options = configs['Common']['install_options']
        install_programs(programs, options)
    except OSError as err:
        print(err)
        sys.exit('Der opstod fejl ved installation af base software')
    else:
        print('Afsluttet apt-get installation af base software')
