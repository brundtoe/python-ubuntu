"""
Dette module anvendes til at foretage den indledende konfiguration 

1. Indlæsning af konfigurationsfilen
2. Timezone opdateres
3. Tilføj max watches for filer
4. Opret mappen home/bin og kopier images
5. mount af wdmycloud
6. mount af extra diske
"""

import sys
import os
import shlex
from subprocess import run

from moduler.fileOperations import addLine
from moduler.install_programs import install_program
from moduler.extra_diske import update_extradiske
from moduler.wdmycloud import update_wdmycloud


def global_config(configs):

    # timezone opdateres
    timezone = configs['Common']['timezone']
    try:
        cmd = shlex.split(f'timedatectl set-timezone {timezone}')
        res = run(cmd)
    except OSError as err:
        print(err)
        sys.exit(f'Der opstod fejl ved set-timezone {timezone}')
    else:
        print(f'timezone er sat til {timezone}')

    # Tilføj max watches for filer
    try:
        filename = '/etc/sysctl.d/40-max_user_watches.conf'
        max_watches = 'fs.inotify.max_user_watches = 524288\n'
        addLine(filename, max_watches)
    except OSError as err:
        print(err)
        sys.exit(f'Der opstod fejl ved opdatering af {filename}')
    else:
        print(f'{filename} er opdateret med {max_watches}')

    # set PLATFORM=VAGRANT
    try:
        addLine('/etc/environment', 'PLATFORM=VAGRANT')
    except OSError as err:
        print(err)
        sys.exit(f'Der opstod fejl ved opdatering af environment med PLATFORM')
    else:
        print('/etc/environment opdateret med PLATFORM=VAGRANT')

    # set default editor
    try:
        addLine('/etc/profile.d/editor.sh', "export EDITOR='vim'")
    except OSError as err:
        print(err)
        sys.exit(f'Der opstod fejl ved opdatering af environment med PLATFORM')
    else:
        print("/etc/profile.d/editor.sh opdateret med export EDITOR='vim'")

