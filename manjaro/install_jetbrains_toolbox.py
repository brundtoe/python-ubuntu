#!../venv/bin/python
#
# installation af jetBrains ToolBox

from fileOperations import fetch_config, fetch_archive


def install_jetbrains_toolbox(configs):
    """
    Installation af JetBrains Toolbox
    :param configs: parametre fra configpaser config/manjaro.ini
    :return: void
    """
    url = configs['jetbrains.toolbox']['url']
    version = configs['Common']['jetbrains-toolbox']
    user = configs['Common']['user']
    program = 'JetBrains Toolbox'
    fetch_archive(url,user,program,version)


if __name__ == '__main__':
    configs = fetch_config('../config/manjaro.ini')
    install_jetbrains_toolbox(configs)
