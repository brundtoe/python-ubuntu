import requests

def download_file(url):
    local_filename = url.split('/')[-1]
    outfile = f'../outfile/{local_filename}'
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(outfile, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
    return local_filename

if __name__ == "__main__":
    url = 'https://sphinxdoc.brundtoe.dk/raisedemo.html'
    try:
        res = download_file(url)
    except Exception as err:
        print(err.response.status_code,err.response.url)
    else:
        print('Den hentede fil',res)
    finally:
        print('Det var så det')
