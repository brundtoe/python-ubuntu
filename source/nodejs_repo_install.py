from subprocess import run
import os
from moduler.fileOperations import download_file

def nodejs_repo(url):

    outfile = ''
    try:
        outfile = download_file(url)
    except Exception as err:
        print(err)
        exit(1)

    try:
        os.chmod(outfile, 0o755)
    except Exception as err:
        print(err)
        exit(1)

    try:
        run([outfile])
    except Exception as err:
        print(err)
        exit(1)
