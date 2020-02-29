.. index:: !Download Files
.. _download-files:

==============
Download Files
==============
Opdateret februar 2020

Det er muligt at downloade filer med **urllib** fra Pythons standard library, med **urllib3** eller med modulet **requests**

**urllib3** og **requests** er mere programmørvenlige end **urrlib** bl.a. i forbindelse med download hvor http request bliver redirected. De to førstnævnte følger defualt en redirigering.

Download af store filer skal opdeles i blokker for at reducere memory forbruget.

Urllib
======
Urllib fra Pythons standard library kan anvendes til download af filer, hvor der er sikkerhed for, at der ikke foregår redirection.

Eksempel på download af en lille fil::

   from urllib.request import urlopen

   with urlopen(url) as response, open(outfile, "w+b") as f:
       res = response.read()
       f.write(res)

Ovenstående indlæser hele filen i memory inden den gemmes på disken.

Når der downloades større filer så skal der læses mindre blokke ad gangen for at begrænse memory belastningen, der læses 4096 bytes ad gangen::

   from urllib.request import urlopen

   with urlopen(url) as response, open(outfile,"w+b") as f:
      while True:
            chunk = response.read(4096)
            if len(chunk) < 1:
               break
            f.write(chunk)

Download med **NamedTemporaryFile**, som default gemmes i **/tmp**, der anvendes en default systemafhængig buffer størrelse, som er 4096 eller 8192 bytes::

   from urllib.request import urlopen
   from shutil import copyfileobj
   from tempfile import NamedTemporaryFile

   with urlopen(url) as fsrc, NamedTemporaryFile(delete=False) as fdst:
         copyfileobj(fsrc, fdst)
         return(fdst.name)

Som standard slettet filen igen, når den lukkers. **delete=False** anvendes for at bevare filen.

Find default_buffer_size::

   import io
   print("Default buffer size:",io.DEFAULT_BUFFER_SIZE)

Package requests
================
Python package requests anvendes bl.a. når der kan forventes redirects i forbindelse med en download::

   import requests
   def download_file(url):
      req = requests.get(url, allow_redirects=True, stream=True)
      outfile = f'/tmp/{url.split("/")[-1]}'
      with open(outfile, 'wb') as fd:
         for chunk in req.iter_content(chunk_size=8192):
         fd.write(chunk)
      return outfile

Ref. https://requests.readthedocs.io/en/master/