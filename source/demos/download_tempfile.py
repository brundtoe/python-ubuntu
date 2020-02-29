from urllib.request import urlopen
from shutil import copyfileobj
from tempfile import NamedTemporaryFile

url = 'http://cdimage.ubuntu.com/kubuntu/releases/eoan/release/kubuntu-19.10-desktop-amd64.iso'

local_filename = url.split('/')[-1]

outfile = f'../outfile/{local_filename}'

with urlopen(url) as fsrc, NamedTemporaryFile(delete=False) as fdst:
      copyfileobj(fsrc, fdst)
      print(fdst.name)

