#!venv/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from moduler.fileOperations import fetch_config

from moduler.user_profile import user_profile
from moduler.global_config import global_config
from moduler.manjaro import install_packages
from moduler.wdmycloud import update_wdmycloud
from moduler.extra_diske import update_extradiske



menu = """Manjaro Menu for systeminstallation og opdateringer
===========================================
\t1)  Update user profile
\t2)  Global configuration
\t3)  Install basis software
\t4)  Mount WD My Cloud
\t5)  Update extra diske
\t6)  Node.js
\t7)  MongoDB
\t8)  PHP incl. Composer
\t9)  Apache2 med libapache2-mod-php
\t10) Nginx
\t11) MySQL
\t12) Docker
\t13) Flip http web server
===========================================
Desktop programmer til fysisk host
===========================================
\t14) Vagrant
\t15) Packer
\t16) Virtualbox
\t17) Google Chrome
===========================================
\t99) I do not know, Exit!
"""
switcher = {
    1: user_profile,
    2: global_config,
    3: install_packages;
    4: update_wdmycloud,
    5: update_extradiske
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

    show_menu(configuration)
