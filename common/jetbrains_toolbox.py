# -*- coding: utf-8 -*-import sys
#
# installation af jetBrains ToolBox

from moduler.fileOperations import fetch_archive
from moduler.desktopfile import create_desktop_file


def install_jetbrains_toolbox(configs):
    """
    Installation af JetBrains Toolbox
    :param configs: parametre fra configpaser config/config.ini
    :return: void
    """
    # https://www.jetbrains.com/toolbox-app/download/download-thanks.html?platform=linux

    version = configs['Common']['jetbrains-toolbox']
    url = f"https://download.jetbrains.com/toolbox/jetbrains-toolbox-{version}.tar.gz"
    # sha256 = "https://download.jetbrains.com/toolbox/jetbrains-toolbox-{version}.tar.gz.sha256"
    user = configs['Common']['user']
    program = 'JetBrains Toolbox'
    fetch_archive(url, user, program, version)

    program = 'JetBrains'
    tmpl = f'{program}.jinja'
    project_path = configs['Common']['path']
    create_desktop_file(program, project_path, tmpl, user)


