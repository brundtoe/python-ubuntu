# -*- coding: utf-8 -*-
#
# Installation af Google Chrome
#

import os
import sys

from moduler.apt_update import apt_update
from moduler.install_programs import install_program
from moduler.install_repo import install_repo


def install_chrome(configs):
    print('Installation af Google Chrome')
    if os.path.exists('/etc/apt/sources.list.d/google-chrome.list'):
        print('Google-chrome er allerede installeret')
        return
    # https://www.google.com/linuxrepositories/
    # https://www.ubuntuupdates.org/ppa/google_chrome
    repo_key = "https://dl.google.com/linux/linux_signing_key.pub"
    program = 'google-chrome'
    sources_string = "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
    try:
        install_repo(repo_key, program, sources_string)
        print(f'{program} repository er installeret')
    except Exception as err:
        print(err)
        sys.exit(f'{program} repository er ikke installeret')

    options = configs['Common']['install_options']
    try:
        apt_update()
        install_program('google-chrome-stable', options)
        print(f'{program} installeret')
    except Exception as err:
        print(err)
        sys.exit(f'Installationen af {program} fejlede')
    print('Installation af Google Chrome')