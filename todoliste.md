## Opgaveliste

## Import af mysql data

Se eksemplet common/mysql_data.py
Scriptet fungerer på Manjaro

TODO generaliser import af mysqldata

tjek af db server afhæninger af om det er kubuntu eller manjaro

bør også tjekke for om alle source filerne eksisterer inden der opdateres

lopp gennem inddata filen::

   with open(filename) as file:
      if line.startswith('source'):
         datafile = line[line.find('/home'),-1].strip()
         if not os.path.exists(datafile:
            sys.exit(f'Filen .. {datafile} eksisterer ikke')
   


PyCharm noter om anvendelse af subprocess.Popen med tilhørende eksempel

## phpMyAdmin

DONE phpMyAdmin på Manjaro

Der er oprettet en vejledning phpmyadmin.rst

TODO installer phpmyadmin på Kubuntu

skal downloades fra phpmyadmin.net

## wdmycloud user er hardkodet

indsæt en dummy user og erstat den via en search og replace

kan formentlig gøres med en python string funktion



## web server site definitioner

Kubuntu Apache2 site definition
===============================
en apache site konfiguration med
   - opdatering af hosts
   - en site konfig til /etc/apache2/sites-available
   - enable med a2ensite <filnavn>

ref. file:///home/jackie/SphinxDoc/source/webserver/Apache.html#oprettelse-af-virtuel-host

## Kubuntu nginx site konfiguration

Se eksempel i mappen devops-files


## Manjaro http site konfiguration

Se eksempel i mappen devops-files og evt. i docker_standard

## Manjaro nginx site konfiguration

Se eksempel i mappen devops-files og evt. i docker_standard

## Udenstående efterfølgende på Komplett eller Esprimo

   - laravel/homestead

## Testcases med unittest

https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

med PyCharm support

- Pytest https://docs.pytest.org/en/latest/
- UnitTest (PyUnit) - Standard library https://docs.python.org/3.7/library/unittest.html
- Django har sit eget testframework
- flask dokumentationen viser PyTest eksempler