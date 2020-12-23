#!venv/bin/python
# -*- coding: utf-8 -*-import sys

import os
import sys
from moduler.fileOperations import fetch_config
from common.freefilesync import install_freefilesync
from common.jetbrains_toolbox import install_jetbrains_toolbox
from common.nosqlbooster import install_nosqlbooster

menu = """Menu for desktop installation og opdateringer
=============================================
\t1)  FreefileSync
\t2)  JetBrains Toolbox
\t3)  NoSQLBooster
\t4)  Postman
\t5)  SmartGit
\t6)  SSH key
===========================================
\t99) I do not know, Exit!
"""
switcher = {
    1: install_freefilesync,
    2: install_jetbrains_toolbox,
    3: install_nosqlbooster
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
    filename = f'{os.path.dirname(__file__)}/config/config.ini'
    try:
        configuration = fetch_config(filename)
    except Exception as err:
        print(err)
        sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
    else:
        print(f'Konfigurationsfilen {filename} er indlæst')

    show_menu(configuration)
