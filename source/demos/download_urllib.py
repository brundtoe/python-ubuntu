import sys
from urllib.request import urlopen

def download_urllib(url, outfile):
    """
    Download a small file
    :param url: web page to be downloaded
    :param outfile: where to save the file
    :return: true on success
    """
    try:
        with urlopen(url) as response:
            with open(outfile, "w+b") as f:
                res = response.read()
                f.write(res)
    except FileNotFoundError as err:
        sys.exit(f'kan ikke gemme {outfile} fejl {err.strerror}')
    except Exception as err:
        sys.exit(f'Kan ikke downloade fra {url}, {err.msg}')
    else:
        return True

if __name__ == "__main__":
    url = 'https://sphinxdoc.brundtoe.dk/esprimo.html'
    outfile = "../../outfile/esprimo.html"
    download_urllib(url,outfile)