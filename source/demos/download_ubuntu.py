import requests

url = 'http://cdimage.ubuntu.com/kubuntu/releases/eoan/release/kubuntu-19.10-desktop-amd64.iso'

local_filename = url.split('/')[-1]

outfile = f'../outfile/{local_filename}'

r = requests.get(url, stream = True)
with open(outfile, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=2048):
        fd.write(chunk)
print('Det var så det')