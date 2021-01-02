# -*- coding: utf-8 -*-
#

# from os import path
# import sys
from moduler.exceptions import AddLineFileNotFound
# from moduler.fileOperations import add_line

from subprocess import run

try:
    res = run(['ls'], capture_output=True)
except FileNotFoundError as err:
    print(err)
    raise AddLineFileNotFound('olsen')
except AddLineFileNotFound as err:
    print(err)
else:
    print(f'subprocess call succeeds. {res.stdout}')
