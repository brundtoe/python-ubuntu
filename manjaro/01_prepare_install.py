#!../venv/bin/python
# -*- coding: utf-8 -*-
# script som samler de enkelte del og foretages den samlede installation på Kubuntu
#
# Inden scriptet runnes oprettes i mappen infile filen .env.develop med password til wdmycloud
#

import sys, os, shlex
from subprocess import run

from moduler.install_prepare import install_prepare

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
