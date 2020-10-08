## Opgaveliste

DONE nye installationer helt forfra.

afprøvning af de opdaterede scripts og vejledninger

- Manjaro
- Kubuntu

FIXME mysql opdateringen fejler på manjaro

- sudo kan udføre det rå script

   dvs det er scriptes subprocess.Popen som fejler.

Øvrige foregår med python_scripts

hvis python scriptet opgives så anvende scriptet blot fra command line

FIXME nosqlbooster Manjaro

Det er OK på Kubuntu - måske der blot skal ventes en rum tid

Manjaro download fejler, måske det er user_agent i request som skal justeres så sitet tror det er Firefox som downloader

er det bedre med curl eller wget

FIXME freefilesync

Download fejler ved første forsøg men ved gentales af script er alt ok.

er det bedre med curl eller wget

Er filezilla en smartere option

## prøv mysql workbench på Kubuntu


## phpMyAdmin

DONE phpMyAdmin på Manjaro

Der er oprettet en vejledning phpmyadmin.rst

TODO installer phpmyadmin på Kubuntu

skal downloades fra phpmyadmin.net



## justeringer

der skal i docs være link så man efter en tur til en udnervejledning i afslutnigenn af denne kan klikke tilbage til den oprindelige.

kræver også ankre i de oprindelige docs

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
