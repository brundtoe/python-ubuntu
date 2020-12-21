#!venv/bin/python
# -*- coding: utf-8 -*-import sys

import os
import sys
from moduler.fileOperations import fetch_config
from moduler.user_profile import userProfile
from moduler.wdmycloud import update_wdmycloud
from moduler.extra_diske import update_extradiske

menu = """Menu for systeminstallation og opdateringer
\t1)  Update user profile
\t2)  Mount WDMycloud
\t3)  Update extra diske
\t99) I do not know, Exit!
"""

def not_supported():
    print('Selection is not supported')


def show_menu(configs):
    os.system('clear')
    print(menu)
    sel = input("Vælg en funktion: ")
    selection = ''
    try:
        selection = int(sel)
    except ValueError as err:
        answ = input('Vælg et nummer mellem 1 og 20 ...')
        show_menu(configs)
    if selection == 99:
        exit(0)
    while selection not in range(1, 20):
        show_menu(configs)
    run_option(selection, configs)


switcher = {
    1: userProfile,
    2: update_wdmycloud,
    3: update_extradiske
}


def run_option(option, configs):
    print(f"Du valgte  {option}")
    action = switcher.get(option, lambda argument: not_supported())
    action(configs)
    input("Enter RETURN to Continue ...")
    show_menu(configs)


if __name__ == "__main__":

    if os.geteuid() != 0:
        sys.exit('Scriptet skal udføres med root access')

    configuration = ''
    filename = f'{os.path.dirname(__file__)}/config/config.ini'
    try:
        configuration = fetch_config(filename)
    except OSError as err:
        sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
    else:
        print(f'Konfigurationsfilen {filename} er indlæst')

    show_menu(configuration)
