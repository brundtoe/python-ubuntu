#!/usr/bin/env python3
#
import sys, os
from subprocess import run
from fileOperations import download_file


def nodejs_repo(url):
    """
    Installation af Node.js repositoriet
    :param url: path til setup script
    :return: void
    """
    outfile = ''
    try:
        outfile = download_file(url)
    except Exception as err:
        print(err)
        sys.exit(f'Download fra {url} er fejlet')

    try:
        os.chmod(outfile, 0o755)
    except Exception as err:
        print(err)
        sys.exit(f'Node.js Setup filen kan ikke gøres eksekverbar')

    try:
        run([outfile])
    except Exception as err:
        print(err)
        exit(f'Registrering af Node.js repository er fejlet.')
