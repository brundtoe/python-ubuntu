#!../venv/bin/python
#
# Installation af smartgit
#
from moduler.fileOperations import fetch_config, fetch_archive
from moduler.desktopfile import create_desktop_file

def install_smartgit(configs):
    """
    Installation af SmartGit
    Forudsætter installation af gtk2
    :param configs: parametre fra config.ini
    :return: void
    """
    # https://www.syntevo.com/smartgit/download/
    version = configs['Common']['smartgit']
    #url_deb = f"https://www.syntevo.com/downloads/smartgit/smartgit-{version}.deb"
    url = f"https://www.syntevo.com/downloads/smartgit/smartgit-linux-{version}.tar.gz"
    user = configs['Common']['user']
    program = 'SmartGit'
    fetch_archive(url, user, program, version)

    tmpl = f'{program}.jinja'
    create_desktop_file(program, tmpl, user)


if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    install_smartgit(configs)
