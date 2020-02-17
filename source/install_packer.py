# installation af Packer

import sys,os, shutil
from moduler.fileOperations import fetch_config
import requests

try:
    configs = fetch_config('../config/config.ini')
    url = configs['packer.io']['url']
    version = configs['Common']['packer']
    user = configs['Common']['user']
    print(url)
    req = requests.get(url, allow_redirects=True, stream=True)

    outfile = f'/home/{user}/Downloads/{url.split("/")[-1]}'

    with open(outfile, 'wb') as fd:
        for chunk in req.iter_content(chunk_size=4096):
            fd.write(chunk)
    shutil.unpack_archive(outfile,f'/home/{user}/bin','zip')
except Exception as err:
    sys.exit(f'Download af Packer version {version} er fejlet\n')
else:
    print(f'Packer version {version} er downloded og pakket ud')


