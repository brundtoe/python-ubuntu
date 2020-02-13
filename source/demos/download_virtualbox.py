import requests

url = 'https://download.virtualbox.org/virtualbox/6.1.2/virtualbox-6.1_6.1.2-135662~Ubuntu~eoan_amd64.deb'

outfile = '../outfile/virtualbox-6.1.2.deb'

r = requests.get(url, stream = True)
with open(outfile, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=4096):
        fd.write(chunk)

# TODO en progress bar https://github.com/verigak/progress/
# Det virker næppe i ovenstående idet download skal udføres i et loop
# det vil kræve en mere manuel download hvor der læses et chunck ad gangen
# modellen er her
# https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
# der er eksmepler med modulet request og med urllib
# eksemplerne downloader et ubuntu image
# se også https://likegeeks.com/downloading-files-using-python/
# requests https://requests.readthedocs.io/en/master/