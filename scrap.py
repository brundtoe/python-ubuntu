# -*- coding: utf-8 -*-
#

from os import path
import sys
from moduler.exceptions import AddLineFileNotFound
from moduler.fileOperations import add_line

user = 'jesper'
try:
    add_line(f'/home/{user}/.bashrc', 'fusker')
    #with open(f'/home/{user}/.bashrc', 'w') as file:
    #    file.write('hovsa')

except AddLineFileNotFound as err:
    print(err)

#except OSError as err:
#    print('Fejl', err)
    sys.exit(f'Der opstod fejl ved opdatering af bashrc med PS1')
else:
    print(f'bashrc for {user} er  opdateret med command prompt')