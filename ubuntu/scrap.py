#!../venv/bin/python
# -*- coding: utf-8 -*-
#
# Installation af Virtualbox
#

import os
import sys
import shutil
import shlex
from subprocess import run
from moduler.fileOperations import fetch_config
from moduler.download_file import fetch_file
from moduler.sha256sum import hash_file


if __name__ == '__main__':
    #    if os.geteuid() != 0:
    #        sys.exit('Scriptet skal udføres med root access')

    print(os.path.realpath(__file__))
    print(os.getcwd())