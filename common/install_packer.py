#!../venv/bin/python
#
# installation af Packer

from moduler.fileOperations import fetch_config, fetch_archive


def install_packer(configs):
    """
    Installation af Packer til opbygning af vagrant bokse med chef/bento
    :param configs: parametre fra config.ini
    :return: void
    """
    # https://packer.io/
    version = configs['Common']['packer']
    url = f"https://releases.hashicorp.com/packer/{version}/packer_{version}_linux_amd64.zip"
    user = configs['Common']['user']
    program = 'Packer'
    fetch_archive(url, user, program, version, 'zip')

if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    install_packer(configs)
