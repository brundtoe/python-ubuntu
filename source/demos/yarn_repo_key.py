import urllib.request

url = 'https://dl.yarnpkg.com/debian/pubkey.gpg'

outfile = '../outfile/yarn_pubKey.gpg'

with urllib.request.urlopen(url) as response:
    with open(outfile,"w+b") as f:
        res = response.read()
        f.write(res)

## TODO download skal for relevanter filer kunne foretage tjekke med shasum
## TODO for store filer skal der kunne læses i chunks