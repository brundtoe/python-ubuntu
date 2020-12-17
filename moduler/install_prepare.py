"""
Dette module anvendes til at foretage den indledende konfiguration 

1. Indlæsning af konfigurationsfilen
2. Timezone opdateres
3. Tilføj max watches for filer
4. Opret mappen home/bin og kopier images
5. mount af wdmycloud
6. mount af extra diske
"""

import sys, os, shlex
from subprocess import run

from moduler.fileOperations import fetch_config, addLine
from moduler.home_bin import homebin
from moduler.install_programs import install_program
from moduler.extra_diske import update_extradiske
from moduler.wdmycloud import update_wdmycloud

if os.geteuid() != 0:
    sys.exit('Scriptet skal udføres med root access')

def install_prepare():

    # Indlæsning af konfigurationsfilen
    configs = ''
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
        filename = '/etc/sysctl.d/40-max_user_watches.conf'
        max_watches = 'fs.inotify.max_user_watches = 524288\n'
        addLine(filename, max_watches)
    except Exception as err:
        print(err)
        sys.exit(f'Der opstod fejl ved opdatering af {filename}')
    else:
        print(f'{filename} er opdateret med {max_watches}')

    # Opret mappen home/bin samt /home/.local/binog kopier images
    try:
        user = configs['Common']['user']
        homebin(user)
    except Exception as err:
        print(err)
        sys.exit(f'Der opstod fejl ved oprettelse af /home/{user}/bin')
    else:
        print(f'/home/{user}/bin er opdateret')

    # set PLATFORM=VAGRANT
    try:
        addLine('/etc/environment', 'PLATFORM=VAGRANT')
    except Exception as err:
        print(err)
        sys.exit(f'Der opstod fejl ved opdatering af environment med PLATFORM')
    else:
        print('/etc/environment opdateret med PLATFORM=VAGRANT')

    # set default editor
    try:
        addLine('/etc/profile.d/editor.sh', "export EDITOR='vim'")
    except Exception as err:
        print(err)
        sys.exit(f'Der opstod fejl ved opdatering af environment med PLATFORM')
    else:
        print('/etc/environment opdateret med PLATFORM=VAGRANT')



    # Installation af cifs-utils

    try:
        options = configs['Common']['install_options']
        install_program('cifs-utils',options)
    except Exception as err:
        sys.exit('Kan ikke installere cifs-utils')

    # Mount wdmycloud
    try:
        update_wdmycloud(configs,'/etc/fstab')
    except Exception as err:
        sys.exit(f'Der opstod fejl ved mount af wdmycloud')
    else:
        print('wdmycloud credentials og fstab er opdateret')

    # mount extra diske
    try:
        update_extradiske(configs,'/etc/fstab')
    except Exception as err:
        sys.exit('Der opstod fejl ved mount af ekstra diske')
    else: 
        print('Ekstra diske er mounted')
    