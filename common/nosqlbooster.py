# -*- coding: utf-8 -*-import sys
#
import os, shutil
import requests
from moduler.fileOperations import fetch_config
from moduler.desktopfile import create_desktop_file


def install_nosqlbooster(configs):
    """
    Installation af NoSQLBooster
    :param configs: konfigurationsfilen config.ini
    :return: void
    """
    print('Installation af NoSQL Booster ')
    version = configs['Common']['nosqlbooster']
    nosql_major = configs['Common']['nosql-major']
    url = f"https://nosqlbooster.com/s3/download/releasesv{nosql_major}/nosqlbooster4mongo-{version}.AppImage"
    user = configs['Common']['user']

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
        shutil.chown(outfile, user, user)
        os.chmod(outfile, 0o775)
    except Exception as err:
        print(f'Download og installation af NoSQLBooster4MongoDB version {version} er fejlet')
        print(err)
        exit(1)
    else:
        """
        Oprettelse af desktop item er disabled, da første start af programmet
        medfører, at det integreres med system menuen
        """
        # program = 'NoSQLBooster'
        # tmpl = f'{program}.jinja'
        # create_desktop_file(program, tmpl, user, version)
        print(f'NoSQLBooster4MongoDB {version} er installeret')

