import sys,os
import subprocess
from moduler.fileOperations import fetch_config
import requests

def install_smartgit(url,user, version):

    try:
        req = requests.get(url, allow_redirects=True, stream=True)
        outfile = f'/home/{user}/Downloads/{url.split("/")[-1]}'
        with open(outfile, 'wb') as fd:
            for chunk in req.iter_content(chunk_size=4096):
                fd.write(chunk)
        subprocess.run(['dpkg','-i',outfile])
    except Exception as err:
        print(f'Download og installation af SmartGit version {version} er fejlet')
        print(err)
        exit(1)
    else:
        print(f'SmartGit {version} er installeret')

if __name__ == '__main__':
    if os.geteuid() != 0:
       sys.exit('Script skal udføres med root access')
    configs = fetch_config('../config/config.ini')
    url = configs['syntevo.com']['url']
    version = configs['Common']['freefilesync']
    user = configs['Common']['user']
    print(url,user, version)
    install_smartgit(url,user,version)