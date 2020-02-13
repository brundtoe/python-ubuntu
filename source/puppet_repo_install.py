import sys
import subprocess

from moduler.fileOperations import download_file

def puppet_repo(url):

    outfile = ''
    try:
        outfile = download_file(url)
    except Exception as err:
        print(err)
        sys.exit(1)

    try:
        subprocess.run(['dpkg','-i',outfile])
    except Exception as err:
        print(err)
        exit(1)
