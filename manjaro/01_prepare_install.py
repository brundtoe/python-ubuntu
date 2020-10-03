#!../venv/bin/python
# -*- coding: utf-8 -*-
# script som samler de enkelte del og foretages den samlede installation på Kubuntu
#
# Inden scriptet runnes oprettes i mappen infile filen -env med password til wdmycloud
#
import sys, os, shlex
from subprocess import run

from moduler.fileOperations import fetch_config, addLine

from moduler.home_bin import homebin

configs = ''

if os.geteuid() != 0:
    sys.exit('Scriptet skal udføres med root access')

# Indlæsning af konfigurationsfilen
try:
    filename = '../config/config.ini'
    configs = fetch_config(filename)
except Exception as err:
    sys.exit(f'Konfigurationsfilen {filename} kan ikke læses')
else:
    print(f'Konfigurationsfilen {filename} er indlæst')

# timezone opdateres
try:
    timezone = configs['Common']['timezone']
    cmd = shlex.split(f'timedatectl set-timezone {timezone}')
    res = run(cmd)
except Exception as err:
    sys.exit(f'Der opstod fejl ved set-timezone {timezone}')
else:
    print(f'timezone er sat til {timezone}')

# Tilføj max watches for filer
try:
    filename = '/etc/sysctl.d/50-max_user_watches.conf'
    max_watches = 'fs.inotify.max_user_watches = 524288\n'
    addLine(filename, max_watches)
except Exception as err:
    print(err)
    sys.exit(f'Der opstod fejl ved opdatering af {filename}')
else:
    print(f'{filename} er opdateret med {max_watches}')

# Opret mappen home/bin og kopier images
try:
    user = configs['Common']['user']
    homebin(user)
except Exception as err:
    print(err)
    sys.exit(f'Der opstod fejl ved oprettelse af /home/{user}/bin')
else:
    print(f'/home/{user}/bin er opdateret')

# Systemopdatering
try:
    cmd = shlex.split('pacman -Syu --noconfirm')

    res = run(cmd)
except Exception as err:
    sys.exit('Der opstod fejl ved opdatering af systemet med Pacman')
else:
    print('Pacman updatering udført')

print('*' * 50)
print('Konfiguration og forberedelse af installation er afsluttet')
