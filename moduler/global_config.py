# -*- coding: utf-8 -*-
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
import shlex
from subprocess import run

from moduler.fileOperations import addLine


def global_config(configs):
    # timezone opdateres
    timezone = configs['Common']['timezone']
    try:
        cmd = shlex.split(f'timedatectl set-timezone {timezone}')
        run(cmd)
    except OSError as err:
        print(err)
        sys.exit(f'Der opstod fejl ved set-timezone {timezone}')
    else:
        print(f'timezone er sat til {timezone}')

    # Tilføj max watches for filer
    filename = '/etc/sysctl.d/40-max_user_watches.conf'
    try:
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
