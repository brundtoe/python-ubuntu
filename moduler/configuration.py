# -*- coding: utf-8 -*-
#
# indlæsning af konfigruationsoplysninger
#
import os
import sys
import re
import distro
import platform
import shlex
import subprocess
from configparser import ConfigParser, ExtendedInterpolation


def get_host_info():
    distrib = distro.linux_distribution(full_distribution_name=False)[0]
    distrib = 'archlinux' if distrib == 'arch' else distrib
    release = distro.codename().lower()
    return {'distro': distrib, 'release': release, 'hostname': platform.node(), 'virtualization': virtual_platform()}


def virtual_platform():
    cmd = shlex.split('hostnamectl')
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    hostnamectl = res.stdout.decode("UTF - 8")
    if re.search('Virtualization: oracle', hostnamectl):
        return 'oracle'
    elif re.search('Virtualization: vmware', hostnamectl):
        return 'vmware'
    else:
        return ''


def update_config(configs):
    host_info = get_host_info()
    configs['Common']['distro'] = host_info['distro']
    configs['Common']['release'] = host_info['release']
    configs['Common']['hostname'] = host_info['hostname']
    configs['Common']['virtualization'] = host_info['virtualization']
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


def get_config(project_path, filename):

    try:
        configuration = fetch_config(f'{project_path}/{filename}')
        configuration['Common']['project_path'] = project_path
        configs = update_config(configuration)
    except Exception as err:
        print(err)
        sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
    else:
        print(f'Konfigurationsfilen {filename} er indlæst')
        return configs
