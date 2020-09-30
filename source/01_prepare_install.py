#!../venv/bin/python
# -*- coding: utf-8 -*-
# script som samler de enkelte del og foretages den samlede installation på Kubuntu
#
# Inden scriptet runnes oprettes i mappen infile filen -env med password til wdmycloud
#
import sys, os, shlex
from subprocess import run

from moduler.fileOperations import fetch_config
from moduler.add_mountpoints import add_mountpoints
from moduler.smbcredentials import smbcredentials
from moduler.fileOperations import addLine
from moduler.home_bin import homebin
from moduler.apt_update import apt_update

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


try:
    user = configs['Common']['user']
    filename = '../config/.env_develop'
    password = fetch_config(filename)['Common']['password']
    smbcredentials(user, password)
except Exception as err:
    sys.exit('Der opstod fejl ved opdatering af ~/.smbcredentials')
else:
    print('~/.smbcredentials er opdateret med mountpoint')


try:
    filename = '/etc/sysctl.d/99-local.conf'
    text = 'fs.inotify.max_user_watches=524288\n'
    addLine(filename, text)
except Exception as err:
    sys.exit(f'Der opstod fejl ved opdatering af {filename}')
else:
    print(f'{filename} er opdateret med {text}')


try:
    user = configs['Common']['user']
    homebin(user)
except Exception as err:
    print(err)
    sys.exit(f'Der opstod fejl ved oprettelse af /home/{user}/bin')
else:
    print(f'/home/{user}/bin er opdateret')


try:
    apt_update()
except Exception as err:
    sys.exit('Der opstod fejl ved opdatering af systemet med apt update')
else:
    print('apt-get update og apt-get upgrade udført')

print('*' * 50)
print('Konfiguration og forberedelse af installation er afsluttet')
