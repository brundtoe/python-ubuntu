# -*- coding: utf-8 -*-
#
# Installation af Virtualbox
#

import sys

from moduler.install_repo import install_repo
from moduler.apt_update import apt_update
from moduler.install_programs import install_program
from moduler.groups import usermod
from moduler.vbox_ext_pack import install_vbox_ext_pack


def install_vbox(configs):

    # lsb_release er første del af release navnet *lsb_release -sc*
    vbox_lts_release = configs['Common']['vbox_lts_release']
    sources_string = f"deb http://download.virtualbox.org/virtualbox/debian {vbox_lts_release} contrib"

    program = 'virtualbox'
    repo_key = "https://www.virtualbox.org/download/oracle_vbox_2016.asc"
    try:
        install_repo(repo_key, program, sources_string)
    except Exception:
        sys.exit(f'{program} repository er ikke installeret')
    else:
        print(f'{program} repository er installeret')

    options = configs['Common']['install_options']
    vbox_version = configs['Common']['vbox_version']
    user = configs['Common']['user']
    try:
        apt_update()
        install_program(f'virtualbox-{vbox_version}', options)
        usermod(user, 'vboxusers')
        print('Installation af Virtualbox er afsluttet')
    except Exception:
        print('Kunne ikke opdatere systemet med Virtualbox')

    vbox_ext_pack = configs['Common']['vbox_ext_pack']
    ext_pack_filename = f"Oracle_VM_VirtualBox_Extension_Pack-{vbox_ext_pack}.vbox-extpack"
    extention_pack = f"https://download.virtualbox.org/virtualbox/{vbox_ext_pack}/{ext_pack_filename}"

    try:
        install_vbox_ext_pack(extention_pack, vbox_ext_pack)
        print('Virtualbox extension pack er installeret')
    except Exception as err:
        print(err)
        print('Kunne ikke opdatere systemet med Virtualbox extension pack')
