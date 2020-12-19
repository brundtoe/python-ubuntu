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
    version = configs['Common']['workbench']
    url = url = f"https://dev.mysql.com/get/Downloads/MySQLGUITools/mysql-workbench-community_{version}"
    print(url, version)
    install_dpkg(url, version)
