#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script som samler de enkelte del og foretages den samlede installation på Kubuntu
#
# Inden scriptet runnes oprettes i mappen infile filen -env med password til wdmycloud
#
import sys, os, shlex
from shutil import copy
from subprocess import run
from moduler.fileOperations import fetch_config

configs = ''

if os.geteuid() != 0:
    sys.exit('Scriptet skal udføres med root access')

try:
    filename = '../config/config.ini'
    configs = fetch_config(filename)
except Exception as err:
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')

try:
    timezone = configs['Common']['timezone']
    cmd = shlex.split(f'timedatectl set-timezone {timezone}')
    res = run(cmd)
except Exception as err:
    sys.exit(f'Der opstod fejl ved set-timezone {timezone}')
else:
    print(f'timezone er sat til {timezone}')

from moduler.add_mountpoints import add_mountpoints

try:
    user = configs['Common']['user']
    mount_points = configs[configs['Common']['host']]
    add_mountpoints(user, mount_points)
except Exception as err:
    sys.exit('Der opstod fejl ved tilføjelse af mount points for interne diske')
else:
    print('Mount points for interne diske er tilføjet')

try:
    mount_points = configs['mount.points']
    user = configs['Common']['user']
    add_mountpoints(user, mount_points)
except Exception as err:
    sys.exit('Der opstod fejl ved tilføjelse af mount points for wdmycloud')
else:
    print('Mount points for wdmycloud er tilføjet')

from moduler.smbcredentials import smbcredentials

try:
    user = configs['Common']['user']
    filename = '../config/.env_develop'
    password = fetch_config(filename)['Common']['password']
    smbcredentials(user, password)
except Exception as err:
    sys.exit('Der opstod fejl ved opdatering af ~/.smbcredentials')
else:
    print('~/.smbcredentials er opdateret med mountpoint')

from moduler.fstab_update import update_fstab

try:
    mount_string = configs['Common']['mount_string']
    mount_points = configs['mount.points']
    fstab = configs['etc.fstab']
    update_fstab(mount_string, mount_points, fstab)
except Exception as err:
    sys.exit('Der opstod fejl ved opdatering af /etc/fstab')
else:
    print('/etc/fstab er opdateret med mountpoint')

try:
    filename = '/etc/sysctl.d/50-max_user_watches.conf'
    max_watches = 'fs.inotify.max_user_watches = 524288\n'
    with open(filename, 'w') as user_watches:
        user_watches.write(max_watches)
except Exception as err:
    print(err)
    sys.exit(f'Der opstod fejl ved opdatering af {filename}')
else:
    print(f'{filename} er opdateret med {max_watches}')

from moduler.home_bin import homebin

try:
    user = configs['Common']['user']
    homebin(user)
except Exception as err:
    print(err)
    sys.exit(f'Der opstod fejl ved oprettelse af /home/{user}/bin')
else:
    print(f'/home/{user}/bin er opdateret')

try:
    cmd = shlex.split('pacman -Syu --noconfirm')

    res = run(cmd)
except Exception as err:
    sys.exit('Der opstod fejl ved opdatering af systemet med Pacman')
else:
    print('Pacman updatering udført')

print('*' * 50)
print('Konfiguration og forberedelse af installation er afsluttet')
