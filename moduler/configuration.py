# -*- coding: utf-8 -*-
#
# indlæsning af konfigruationsoplysninger
#
import os
import distro
import platform
from configparser import ConfigParser, ExtendedInterpolation


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


def fetch_config(filename):
    config = ConfigParser(interpolation=ExtendedInterpolation())
    if not os.path.exists(filename):
        print(f'Kan ikke læse konfiguationsfilen {filename}')
        exit(1)
    try:
        config.read(filename)
    except Exception as err:
        print(err)
    return config
