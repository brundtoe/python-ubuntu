# -*- coding: utf-8 -*-
#
# Install and configure SSH server
#
import os
import subprocess
import shlex
from moduler.install_programs import install_program
from moduler.fileOperations import add_line


def config_nfs_server(shares, network):
    print('Network File Server konfigureres')
    try:
        for key in shares:
            if os.path.exists(shares[key]):
                add_line('/etc/exports', f'{shares[key]} {network}\n')
            else:
                print(f'share {shares[key]} findes ikke')
    except OSError as err:
        print(err)
        print('Kan ikke konfigurere nfs server og genstarte serveren')
        return 0


def install_nfs_server(configs):
    print('network file server installeres')
    virtual = configs['Common']['virtualization']
    if virtual in ['oracle', 'vmware']:
        print('Kan ikke installeres på virtuelle maskiner')
        return 0
    options = configs['Common']['install_options']
    distrib = configs['Common']['distro']

    try:
        if distrib in ['ubuntu', 'debian']:
            install_program('nfs-kernel-server', options)
        elif distrib in ['archlinux', 'manjaro']:
            subprocess.run(shlex.split(f"pacman -S --noconfirm --needed nfs-utils"))
        else:
            print(f'Distributionen {distrib} er ikke implementeret')
            return 0
    except OSError as err:
        print(err)
        return 0

    shares = configs['nfs.share']
    network = configs['Common']['nfs_allow']
    config_nfs_server(shares, network)

    if distrib in ['ubuntu', 'debian']:
        subprocess.run(shlex.split('systemctl restart nfs-kernel-server'))
    else:
        subprocess.run(shlex.split('systemctl restart nfs-server'))
