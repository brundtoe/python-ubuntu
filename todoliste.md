## Opgaveliste

TODO nye installationer helt forfra.

afprøvning af de opdaterede scripts og vejledninger

- Manjaro
- Kubuntu

FIXME mysql opdateringen fejler på manjaro

- jackie mangler grant option
- sudo kan udføre det rå script

   dvs det er scriptes subprocess.Popen som fejler.

FIXME nosqlbooster Manjaro

Manjaro download fejler, måske det er clietn i request som skal justeres så siteet tror det er Firefox som downloader

## justeringer

der skal i docs være link så man efter en tur til en udnervejledning i afslutnigenn af denne kan klikke tilbage til den oprindelige.

kræver også ankre i de oprindelige docs


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
