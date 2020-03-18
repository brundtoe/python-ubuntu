#!/usr/bin/env python3
#
# Installation af smartgit
#
import sys, os
from moduler.fileOperations import fetch_config, fetch_archive
from moduler.desktopfile import create_desktop_file

def install_smartgit(configs):
    """
    Installation af SmartGit
    Forudsætter installation af gtk2
    :param configs: parametre fra config.ini
    :return: void
    """

    url = configs['syntevo.com']['url_targz']
    user = configs['Common']['user']
    program = 'SmartGit'
    version = configs['Common']['smartgit']
    fetch_archive(url, user, program, version)


    tmpl = f'{program}.jinja'
    create_desktop_file(program, tmpl, user)

if __name__ == '__main__':
    configs = fetch_config('../config/manjaro.ini')
    install_smartgit(configs)
