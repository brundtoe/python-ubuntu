from urllib.request import urlopen
from shutil import copyfileobj, copyfile
from tempfile import NamedTemporaryFile
import os

def fetch_file(url, outfile):

    try:
        with urlopen(url) as fsrc, NamedTemporaryFile(delete=False) as fdst:
            copyfileobj(fsrc, fdst)
            print(fdst.name)
        copyfile(fdst.name, outfile)
        os.remove(fdst.name)
    except Exception as err:
        raise os.error
    else:
        return True