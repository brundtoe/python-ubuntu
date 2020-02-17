# installation af Google Chrome

import sys,os, shutil
from moduler.fileOperations import fetch_config
import requests

try:
    configs = fetch_config('../config/config.ini')
    url = configs['freefilesync.org']['url']
    version = configs['Common']['freefilesync']
    user = configs['Common']['user']
    print(url)
    req = requests.get(url, allow_redirects=True, stream=True)

    outfile = f'/home/bent/Downloads/{url.split("/")[-1]}'

    with open(outfile, 'wb') as fd:
        for chunk in req.iter_content(chunk_size=4096):
            fd.write(chunk)
    shutil.unpack_archive(outfile,f'/home/{user}/bin','gztar')
except Exception as err:
    sys.exit(f'Download af FreefileSync version {version} er fejlet\n')
else:
    print(f'FreeFileSync version {version} er downloded og pakket ud')


