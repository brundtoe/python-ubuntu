from urllib.request import urlopen
from shutil import copyfileobj
from tempfile import NamedTemporaryFile
import sys, os
def download_chuncks(url, chunk_size, outfile):
    """
    Download a large file in chuncks
    :param url: web page to be downloaded
    :param chunck_size: buffer size used when downloading
    :param outfile: where to save the file
    :return: true on success
    """
    try:
        with urlopen(url) as response, open(outfile, "w+b") as f:
                while True:
                    chunk = response.read(chunk_size)
                    if len(chunk) < 1:
                        break
                    f.write(chunk)
    except FileNotFoundError as err:
        sys.exit(f'kan ikke gemme {outfile} fejl {err.strerror}')
    except Exception as err:
        sys.exit(f'Kan ikke downloade fra {url}, {err.msg}')
    else:
        return True

if __name__ == "__main__":
    url = 'http://cdimage.ubuntu.com/kubuntu/releases/eoan/release/kubuntu-19.10-desktop-amd64.iso'
    local_filename = url.split('/')[-1]
    outfile = f'../../outfile/{local_filename}'
    chunck_size = 8192
    download_chuncks(url,chunck_size,outfile)