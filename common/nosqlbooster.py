# -*- coding: utf-8 -*-
#
import os
import shutil
import requests
import pwd
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
    down_file = f'nosqlbooster4mongo-{version}.AppImage'
    url = f"https://nosqlbooster.com/s3/download/releasesv{nosql_major}/{down_file}"
    user = pwd.getpwuid(1000).pw_name
    app_path = f'/home/{user}/Applications'
    if os.path.exists(f'{app_path}/{down_file}'):
        print(f'NoSQLBooster version {version} er installeret')
        return
    try:
        if not os.path.exists(app_path):
            os.makedirs(app_path)
            shutil.chown(app_path, user, user)
        req = requests.get(url, allow_redirects=True, stream=True)
        outfile = f'{app_path}/{url.split("/")[-1]}'
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
        program = 'NoSQLBooster'
        project_path = configs['Common']['project_path']
        tmpl = f'{program}.jinja'
        create_desktop_file(program, project_path, tmpl, user, version)
    print(f'NoSQLBooster4MongoDB {version} er installeret')
