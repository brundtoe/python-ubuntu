#!/usr/bin/env python3
#
import sys, os
import subprocess

from moduler.fileOperations import download_file, fetch_config


def puppet_repo(url):
    """
    Installation af puppet repository
    :param url: path til repository
    :return: void
    """

    try:
        outfile = download_file(url)
    except Exception as err:
        print(err)
        sys.exit('Download af Puppet repository er fejlet')

    try:
        pass
        subprocess.run(['dpkg', '-i', outfile])
    except Exception as err:
        print(err)
        sys.exit('Installation af Puppet repository er fejlet')


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Script skal udføres med root adgang')
    try:
        configs = fetch_config('../config/config.ini')
        url = configs['puppetlabs.com']['repo']
        puppet_repo(url)
        print('Puppet repository er installeret')
    except Exception as err:
        print(err)
        sys.exit(1)
