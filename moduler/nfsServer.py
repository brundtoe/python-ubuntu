# -*- coding: utf-8 -*-
#
# Install and configure SSH server
#
import distro
import subprocess
import shlex
from moduler.install_programs import install_program


def install_nfsserver(configs):
    host_type = configs['Common']['host']
    if host_type == 'virtual.local':
        print('Kan ikke installeres på virtuelle maskiner')
        return 0
    options = configs['Common']['install_options']
    distrib = distro.linux_distribution(full_distribution_name=False)

    try:
        if distrib in ['ubuntu', 'debian']:
            install_program('nfs-kernel-server', options)
        elif distrib in ['arch', 'manjaro']:
            subprocess.run(shlex.split(f"pacman -S --noconfirm nfs-utils"))
        else:
            print(f'Distributionen {distrib} er ikke implementeret')
    except OSError as err:
        print(err)
        return 0

