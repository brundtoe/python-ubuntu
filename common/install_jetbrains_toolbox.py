#!../venv/bin/python
#
# installation af jetBrains ToolBox

from moduler.fileOperations import fetch_config, fetch_archive
from moduler.desktopfile import create_desktop_file


def install_jetbrains_toolbox(configs):
    """
    Installation af JetBrains Toolbox
    :param configs: parametre fra configpaser config/config.ini
    :return: void
    """
    url = configs['jetbrains.toolbox']['url']
    user = configs['Common']['user']
    program = 'JetBrains Toolbox'
    version = configs['Common']['jetbrains-toolbox']
    fetch_archive(url, user, program, version)

    program = 'JetBrains'
    tmpl = f'{program}.jinja'
    create_desktop_file(program, tmpl, user)


if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    install_jetbrains_toolbox(configs)
