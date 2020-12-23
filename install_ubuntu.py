#!venv/bin/python
# -*- coding: utf-8 -*-import sys

import os
import sys
from moduler.extra_diske import update_extradiske
from moduler.fileOperations import fetch_config
from moduler.flip_server import flip_server
from moduler.global_config import global_config
from moduler.wdmycloud import update_wdmycloud
from moduler.user_profile import user_profile
from ubuntu.apache import install_apache
from ubuntu.docker import install_docker
from ubuntu.chrome import install_chrome
from ubuntu.mongodb import install_mongodb
from ubuntu.mysql import install_mysql
from ubuntu.nginx import install_nginx
from ubuntu.nodejs import install_nodejs
from ubuntu.packages import install_packages
from ubuntu.packer import install_packer
from ubuntu.php import install_php
from ubuntu.vagrant import install_vagrant
from ubuntu.virtualbox import install_vbox

menu = """Menu for systeminstallation og opdateringer
===========================================
\t1)  Update user profile
\t2)  Global configruation
\t3)  Mount WD My Cloud
\t4)  Update extra diske
\t5)  Install basis software
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
    3: update_wdmycloud,
    4: update_extradiske,
    5: install_packages,
    6: install_nodejs,
    7: install_mongodb,
    8: install_php,
    9: install_apache,
    10: install_nginx,
    11: install_mysql,
    12: install_docker,
    13: flip_server,
    14: install_vagrant,
    15: install_packer,
    16: install_vbox,
    17: install_chrome
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