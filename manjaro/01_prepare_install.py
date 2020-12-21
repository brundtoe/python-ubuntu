#!../venv/bin/python
# -*- coding: utf-8 -*-
# script som samler de enkelte del og foretages den samlede installation på Kubuntu
#
# Inden scriptet runnes oprettes i mappen infile filen .env.develop med password til wdmycloud
#

import sys, os, shlex
from subprocess import run

from moduler.global_config import install_prepare
from moduler.fileOperations import addLine
if os.geteuid() != 0:
    sys.exit('Scriptet skal udføres med root access')

# Systemopdatering
try:
    cmd = shlex.split('pacman -Syu --noconfirm')

    res = run(cmd)
except Exception as err:
    print(err)
    sys.exit('Der opstod fejl ved opdatering af systemet med Pacman')
else:
    print('Pacman updatering udført')

print('*' * 50)
print('Systemopdatering er gennemført')

# Indledende konfiguration
try:
    install_prepare()
except Exception as err:
    sys.exit('Den indledende konfiguration er fejlet')
else:
    print('Den indledende konfiguration er gennemført')

    user = 'jackie'
try:
    addLine(f'/home/{user}/.bashrc', 'source .bash_aliases')
except Exception as err:
    print('Kan ikke tilføje .bash_aliases til .bashrc')
else:
    print('Tilføjede .bash_aliases til .bashrc')
