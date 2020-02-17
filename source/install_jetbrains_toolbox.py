# installation af jetBrains ToolBox

from moduler.fileOperations import fetch_config, fetch_archive


def install_jetbrains_toolbox(configs):
    url = configs['jetbrains.toolbox']['url']
    version = configs['Common']['jetbrains-toolbox']
    user = configs['Common']['user']
    program = 'JetBrains Toolbox'
    fetch_archive(url,user,program,version)


if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    install_jetbrains_toolbox(configs)
