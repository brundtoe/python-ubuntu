# -*- coding: utf-8 -*-
#
# indlæsning af konfigruationsoplysninger
#

import distro
import platform


def get_host_info():
    distrib = distro.linux_distribution(full_distribution_name=False)[0]
    distrib = 'archlinux' if distrib == 'arch' else distrib
    release = distro.codename().lower()
    return {'distro': distrib, 'release': release, 'hostname': platform.node()}

def update_config(configs):
    host_info = get_host_info()
    configs['Common']['distro'] = host_info['distro']
    configs['Common']['release'] = host_info['release']
    configs['Common']['hostname'] = host_info['hostname']
    return configs