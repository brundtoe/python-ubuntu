# -*- coding: utf-8 -*-

import os
import sys
from moduler.configuration import get_config
from moduler.extra_diske import update_extradiske
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
from moduler.nfsServer import install_nfs_server
from moduler.secure_ssh import secure_ssh_server

menu = """
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
\t18) Network File server
\t19) Secure SSH server
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
    17: install_chrome,
    18: install_nfs_server,
    19: secure_ssh_server
}


def not_supported():
    print('Selection is not supported')


def show_menu(configs):
    option = 0
    go_on = True
    while option in range(1, len(switcher)) or go_on:
        os.system('clear')
        hostname = configs['Common']['hostname']
        print(f'{hostname.title()} Menu for systeminstallation og opdateringer')
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

    project_path = os.path.dirname(os.path.realpath(__file__))
    filename = 'config/config.ini'
    configs = get_config(project_path, filename)
    
    distro = configs['Common']['distro']
    if distro not in ['ubuntu', 'debian']:
        sys.exit(f'På {distro} skal installationen foretages med install_manjaro.py')

    show_menu(configs)
