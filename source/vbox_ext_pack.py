# installation af VirtualBox Extension pack
import os, sys, shlex, re
import subprocess
from urllib.request import urlopen
from shutil import copyfileobj, copyfile
from tempfile import NamedTemporaryFile
from moduler.fileOperations import fetch_config

def vbox_ext_pack(url,vbox_version):

    try:
        cmd = shlex.split('VBoxManage --version')
        res = subprocess.run(cmd, stdout=subprocess.PIPE)
        version = re.search('^\d{1,}\.\d{1,}\.\d{1,}',res.stdout.decode('utf-8'))

        if version.group(0) != vbox_version:
            print(f'Opdater vbox_ext_pack i config.ini til {version.group(0)} og prøv igen')
            exit(2)
    except Exception as err:
        print('Kan ikke kontrollere VirtualBox installationen - Er VirtualBox Installeret?')
        exit(2)

    local_filename = url.split('/')[-1]

    outfile = f'/tmp/{local_filename}'

    try:

        with urlopen(url) as fsrc, NamedTemporaryFile(delete=False) as fdst:
            copyfileobj(fsrc, fdst)
            print(fdst.name)
        copyfile(fdst.name,outfile)
    except Exception as err:
        print(f'Exception: download af {url} fejlede')
        print(err)
        exit(1)

    try:
        cmd = shlex.split(f'VBoxManage extpack install --replace {outfile}')
        res = subprocess.run(cmd)
    except Exception as err:
        print(f'Exception: Installation af {outfile} fejlede')
        print(err)
        exit(1)

if __name__ == '__main__':
    configs = fetch_config('../config/config.ini')
    url = configs['virtualbox.org']['extention_pack']
    vbox_version = configs['Common']['vbox_ext_pack']
    vbox_ext_pack(url, vbox_version)
