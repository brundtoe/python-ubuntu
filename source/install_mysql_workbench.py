#!../venv/bin/python
#
# Installation af mysql workbench
#
import sys,os
from moduler.fileOperations import fetch_config, install_dpkg

if __name__ == '__main__':
    if os.geteuid() != 0:
       sys.exit('Script skal udføres med root access')
    configs = fetch_config('../config/config.ini')
    url = configs['dev.mysql.com']['url']
    version = configs['Common']['workbench']
    print(url, version)
    install_dpkg(url,version)
