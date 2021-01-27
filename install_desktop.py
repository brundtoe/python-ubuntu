# -*- coding: utf-8 -*-

import os
import sys
from moduler.utilities import get_host_info
from moduler.fileOperations import fetch_config
from common.freefilesync import install_freefilesync
from common.jetbrains_toolbox import install_jetbrains_toolbox
from common.nosqlbooster import install_nosqlbooster
from common.postman import install_postman
from common.smartgit import install_smartgit
from common.sshkeys import create_sshkeys
from manjaro.mongodb import install_mongodb

menu = """Menu for desktop installation og opdateringer
=============================================
\t1)  FreefileSync
\t2)  JetBrains Toolbox
\t3)  NoSQLBooster
\t4)  Postman
\t5)  SmartGit
\t6)  SSH key
\t7)  MongoDB på Manjaro og Archlinux
=============================================
\t99) I do not know, Exit!
"""
switcher = {
    1: install_freefilesync,
    2: install_jetbrains_toolbox,
    3: install_nosqlbooster,
    4: install_postman,
    5: install_smartgit,
    6: create_sshkeys,
    7: install_mongodb
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
            print(f"Du valgte  {option}")
            action = switcher.get(option, lambda argument: not_supported())
            action(configs)
            input("Enter RETURN to Continue ...")


if __name__ == "__main__":

    if os.geteuid() == 0:
        sys.exit('Scriptet må ikke udføres med root access')

    configuration = ''
    filename = 'config/config.ini'
    try:
        configuration = fetch_config(filename)
        configuration['Common']['project_path'] = os.path.dirname(os.path.realpath(__file__))
        host_info = get_host_info()
        configuration['Common']['distro'] = host_info['distro']
        configuration['Common']['release'] = host_info['release']
        configuration['Common']['hostname'] = host_info['hostname']

    except Exception as err:
        print(err)
        sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
    else:
        print(f'Konfigurationsfilen {filename} er indlæst')

    show_menu(configuration)
