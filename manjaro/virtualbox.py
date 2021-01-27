# -*- config: utf-8 -*-
#
from subprocess import run
import pwd
from manjaro.packages import install_program
from moduler.groups import usermod
from moduler.vbox_ext_pack import install_vbox_ext_pack


def install_virtualbox(configs):

    print('Installation af Virtualbox ...')
    user = pwd.getpwuid(1000).pw_name
    linux_kernel = configs['Common']['manjaro_kernel']
    host_modules = f'linux{linux_kernel}-virtualbox-host-modules'
    
    try:
        install_program('virtualbox')
        install_program(host_modules)
        usermod(user, 'vboxusers')
    except OSError as err:
        print(err)
        print('Kan ikke installere virtualbox og host-modules')
        return

    run(['vboxreload'])

    print('Installation af Virtualbox extension pack')
    vbox_ext_pack = configs['Common']['vbox_ext_pack']
    ext_pack_filename = f"Oracle_VM_VirtualBox_Extension_Pack-{vbox_ext_pack}.vbox-extpack"
    url_ext_pack = f"https://download.virtualbox.org/virtualbox/{vbox_ext_pack}/{ext_pack_filename}"

    try:
        install_vbox_ext_pack(url_ext_pack, vbox_ext_pack)
        print('Virtualbox extension pack er installeret')
    except Exception as err:
        print(err)
        print('Kunne ikke opdatere systemet med Virtualbox extension pack')

    print('Afsluttet installation af virtualbox og extension pack')
