#!venv/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from moduler.fileOperations import fetch_config

from moduler.user_profile import user_profile
from moduler.global_config import global_config
from manjaro.packages import install_packages
from moduler.wdmycloud import update_wdmycloud
from moduler.extra_diske import update_extradiske
from manjaro.nodejs import install_nodejs
from manjaro.php import install_php
from manjaro.apache import install_apache

menu = """Manjaro Menu for systeminstallation og opdateringer
===========================================
\t1)  Update user profile
\t2)  Global configuration
\t3)  Install basis software
\t4)  Mount WD My Cloud
\t5)  Update extra diske
\t6)  Node.js
\t7)  PHP incl. Composer
\t8)  Http web server
\t9)  Nginx
\t10) MySQL
\t11) Docker
\t12) Flip http web server
===========================================
Desktop programmer til fysisk host
===========================================
\t13) Vagrant
\t14) Packer
\t15) Virtualbox
\t16) Google Chrome
===========================================
\t99) I do not know, Exit!
"""
switcher = {
    1: user_profile,
    2: global_config,
    3: install_packages,
    4: update_wdmycloud,
    5: update_extradiske,
    6: install_nodejs,
    7: install_php,
    8: install_apache
}


def not_supported():
    print('Selection is not supported')


def show_menu(configs):
    option = 0
    go_on = True
    while option in range(1, len(switcher)) or go_on:
        os.system('clear')
        print(menu)
        selection = input("Vælg en funktion: ")
        try:
            option = int(selection)
        except ValueError:
            input('Vælg et nummer mellem 1 og 20 ...')
            go_on = True
        else:
            if option == 99:
                break
            print(f'Du valgte {option}')
            action = switcher.get(option, lambda argument: not_supported())
            action(configs)
            input("Enter RETURN to Continue ...")


if __name__ == "__main__":

    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres med root access')

    configuration = ''
    filename = 'config/config.ini'
    try:
        configuration = fetch_config(filename)
    except Exception as err:
        print(err)
        sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
    else:
        print(f'Konfigurationsfilen {filename} er indlæst')

    distro = configuration['Common']['distribution']
    if distro == 'ubuntu':
        sys.exit(f'På {distro} skal installationen foretages med install_ubuntu.py')

    show_menu(configuration)
