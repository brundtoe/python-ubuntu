#!../venv/bin/python
#
# installation af Postman

from moduler.fileOperations import fetch_config, fetch_archive
from moduler.desktopfile import create_desktop_file


def install_postman(configs):
    """
    Installation af Postman til test af REST API
    :param configs: parametre fra config.ini
    :return: void
    """

    # https://www.postman.com/downloads/release-notes
    version = configs['Common']['postman']
    # url = "https://dl.pstmn.io/download/version/${Common:postman}/linux64"
    url = "https://dl.pstmn.io/download/latest/linux64"
    user = configs['Common']['user']
    program = 'Postman'
    fetch_archive(url, user, program, version)

    tmpl = f'{program}.jinja'
    create_desktop_file(program, tmpl, user)


if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    install_postman(configs)
