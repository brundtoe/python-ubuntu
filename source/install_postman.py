# installation af postman

import sys, shutil,os
from moduler.fileOperations import fetch_config
import requests

try:
    configs = fetch_config('../config/config.ini')
    url = configs['postman.com']['url']
    version = configs['Common']['postman']
    user = configs['Common']['user']
    print(url)
    req = requests.get(url, allow_redirects=True, stream=True)

    outfile = f'/home/{user}/Downloads/{url.split("/")[-1]}'

    with open(outfile, 'wb') as fd:
        for chunk in req.iter_content(chunk_size=4096):
            fd.write(chunk)
    shutil.unpack_archive(outfile,f'/home/{user}/bin','gztar')
except Exception as err:
    sys.exit(f'Download af Postman version {version} er fejlet\n')
else:
    print(f'Postman version {version} er downloded og pakket ud')


