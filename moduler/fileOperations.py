# -*- coding: utf-8 -*-
#
import sys
import os
import shutil
import requests
import subprocess

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


def download_file(url, filename=None):
    try:
        req = requests.get(url, allow_redirects=True, stream=True)
        if filename:
            outfile = f'/tmp/{filename}'
        else:
            outfile = f'/tmp/{url.split("/")[-1]}'
        with open(outfile, 'wb') as fd:
            for chunk in req.iter_content(chunk_size=8192):
                fd.write(chunk)
        return outfile
    except Exception as err:
        print(err)
        sys.exit(f'Download fra {url} er fejlet')


def addLine(filename, text):
    """Tilføj en linje til en fil hvis den ikke allerede findes"""
    if os.path.exists(filename):
        if isFound(filename, text):
            # print(f"{text} er allered defineret in {filename}")
            return False
    with open(filename, 'a') as file:
        file.write(text)
        # print(f'filen {filename} er nu opdateret med {text}')
    return True


def fetch_archive(url, user, program, version, filename=None, zip_format='gztar'):
    print(url)
    try:
        outfile = download_file(url, filename)
        unpackedfile = f'/home/{user}/programs'
        shutil.unpack_archive(outfile, unpackedfile, zip_format)

    except Exception as err:
        print(err)
        sys.exit(f'Download af {program} version {version} er fejlet\n')
    else:
        print(f'programmet {program} version {version} er downloded og pakket ud')


def install_dpkg(url, version):
    try:
        req = requests.get(url, allow_redirects=True, stream=True)
        outfile = f'/tmp/{url.split("/")[-1]}'
        with open(outfile, 'wb') as fd:
            for chunk in req.iter_content(chunk_size=4096):
                fd.write(chunk)
        subprocess.run(['dpkg', '-i', outfile])
    except Exception as err:
        print(err)
        print(f'Download og installation af Vagrant version {version} er fejlet')
        exit(1)
    else:
        print(f'Vagrant {version} er installeret')
