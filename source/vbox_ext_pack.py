# installation af VirtualBox Extension pack
import sys,os, shlex, re
import subprocess
from moduler.fileOperations import fetch_config, download_file

def vbox_ext_pack(url,vbox_version):

    try:
        if is_vbox_installed(vbox_version):
            outfile = download_file(url)
            cmd = shlex.split(f'VBoxManage extpack install --replace {outfile}')
            res = subprocess.run(cmd)
            if res.returncode != 0:
                raise ValueError
    except Exception as err:
        print(err)
        sys.exit(f'Exception: installation af VirtualBox Extension Pack fejlede')

def is_vbox_installed(vbox_version):

    try:
        cmd = shlex.split('VBoxManage --version')
        res = subprocess.run(cmd, stdout=subprocess.PIPE)
        version = re.search('^\d{1,}\.\d{1,}\.\d{1,}',res.stdout.decode('utf-8'))
        if version.group(0) == vbox_version:
            return True
        if version.group(0) != vbox_version:
            sys.exit(f'Opdater vbox_ext_pack i config.ini til {version.group(0)} og prøv igen')
    except Exception as err:
        print(err)
        sys.exit('Kan ikke kontrollere VirtualBox installationen - Er VirtualBox Installeret?')

if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Script skal udføres med root access')
    configs = fetch_config('../config/config.ini')
    url = configs['virtualbox.org']['extention_pack']
    vbox_version = configs['Common']['vbox_ext_pack']
    vbox_ext_pack(url, vbox_version)
