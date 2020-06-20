#!/usr/bin/env python3
#
import sys, os, shutil
from moduler.fileOperations import fetch_config
import requests
from moduler.desktopfile import create_desktop_file

def install_nosqlbooster(url, user, version):
    """
    Installation af NoSQLBooster
    :param url: path til programmet
    :param user: user account hvor installationen foregår
    :param version: NoSQLBooster version
    :return: void
    """
    try:
        path = f'/home/{user}/Applications'
        if not os.path.exists(path):
            os.makedirs(path)
            shutil.chown(path, user, user)
        
        req = requests.get(url, allow_redirects=True, stream=True)
        outfile = f'{path}/{url.split("/")[-1]}'
        with open(outfile, 'wb') as fd:
            for chunk in req.iter_content(chunk_size=8192):
                fd.write(chunk)
        shutil.chown(outfile,user,user)
        os.chmod(outfile,0o775)
        
    except Exception as err:
        print(f'Download og installation af NoSQLBooster4MongoDB version {version} er fejlet')
        print(err)
        exit(1)
    else:
        print(f'NoSQLBooster4MongoDB {version} er installeret')


if __name__ == '__main__':
    configs = fetch_config('../config/manjaro.ini')
    url = configs['nosqlbooster.com']['url']
    version = configs['Common']['nosqlbooster']
    user = configs['Common']['user']
    print(url,user, version)
    install_nosqlbooster(url,user,version)
