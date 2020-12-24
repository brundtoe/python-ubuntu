# -*- coding: utf-8 -*-
#
# installation af VirtualBox Extension pack
#
import re
import shlex
import subprocess
import sys

from moduler.fileOperations import download_file


def install_vbox_ext_pack(url, vbox_ext_version):
    """
    Installation af VirtualBox Extension Pack
    :param url: path til extension pack
    :param vbox_ext_version: version svarende til den installerede VirtualBox
    :return: void
    """
    print(f'Extension pack version: {vbox_ext_version}')
    try:
        if not is_vbox_installed(vbox_ext_version):
            outfile = download_file(url)
            cmd = shlex.split(f'VBoxManage extpack install --replace {outfile}')
            res = subprocess.run(cmd)
            if res.returncode != 0:
                raise ValueError
    except Exception as err:
        print(err)
        sys.exit(f'Exception: installation af VirtualBox Extension Pack fejlede')


def is_vbox_installed(ext_version):
    """
    Tjek at at den extension pack der forsøges installere svarer til den installerede verison af VirtualBox
    :param ext_version: extension versionen
    :return:
    """
    try:
        print(f'cheking-ext_version-{ext_version}')
        cmd = shlex.split('VBoxManage --version')
        res = subprocess.run(cmd, stdout=subprocess.PIPE)
        version = re.search(r'^\d+\.\d+\.\d+', res.stdout.decode('UTF-8'))
        if version.group(0) == ext_version:
            return True
        else:
            print(f'fundet vbox version:-{version.group(0)}-')
    except Exception as err:
        print(err)
        sys.exit('Kan ikke kontrollere VirtualBox installationen - Er VirtualBox Installeret?')
    else:
        return False
