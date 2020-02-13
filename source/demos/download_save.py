import urllib.request
url = 'http://cdimage.ubuntu.com/kubuntu/releases/eoan/release/kubuntu-19.10-desktop-amd64.iso'

#e56388512a0610bd991192b197a13f1496c107377d9c96d332939c08e305b028 *kubuntu-19.10-desktop-amd64.iso
# e56388512a0610bd991192b197a13f1496c107377d9c96d332939c08e305b028  kubuntu-19.10-desktop-amd64.iso
local_filename = url.split('/')[-1]
outfile = f'../outfile/{local_filename}'
size = 0

with urllib.request.urlopen(url) as response:
    with open(outfile,"w+b") as f:
        while True:
            chunk = response.read(4096)
            if len(chunk) < 1:
                break
            size += len(chunk)
            f.write(chunk)

print(size,'characters copied')
