import sys, os, shutil
from urllib.request import urlopen
from shutil import copyfileobj
from tempfile import NamedTemporaryFile
import requests

from configparser import ConfigParser, ExtendedInterpolation

def fetch_config(filename):
    config = ConfigParser(interpolation=ExtendedInterpolation())
    if not os.path.exists(filename):
        print(f'Kan ikke læse konfiguationsfilen {filename}')
        exit(1)
    try:
        config.read(filename)
    except Exception as err:
        print(err)
    return config

def isFound(filename, text):
    """Find en linje som begynder med text"""
    with open(filename) as file:
        for line in file:
            if line.startswith(text):
                return True
    return False

def download_file(url):

    try:
        with urlopen(url) as fsrc, NamedTemporaryFile(delete=False) as fdst:
            copyfileobj(fsrc, fdst)
            return fdst.name
    except Exception as err:
        print(err)
        raise os.error

def addLine(filename, text):
    """Tilføj en linje til en fil hvis den ikke allerede findes"""
    if os.path.exists(filename):
        if isFound(filename,text):
            #print(f"{text} er allered defineret in {filename}")
            return False
    with open(filename,'a') as file:
        file.write(text)
        #print(f'filen {filename} er nu opdateret med {text}')
    return True

def fetch_archive(url,user,program, version, format='gztar'):
    print(url)
    try:
        req = requests.get(url, allow_redirects=True, stream=True)

        outfile = f'/tmp/{url.split("/")[-1]}'
        unpackedfile =  f'/home/{user}/programs'
        with open(outfile, 'wb') as fd:
            for chunk in req.iter_content(chunk_size=4096):
                fd.write(chunk)
        shutil.unpack_archive(outfile, unpackedfile, format)

    except Exception as err:
        sys.exit(f'Download af {program} version {version} er fejlet\n')
    else:
        print(f'programmet {program} version {version} er downloded og pakket ud')

