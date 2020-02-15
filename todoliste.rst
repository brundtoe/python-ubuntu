# Opgaveliste

ændring af print ved exception, 

except Exception as err
    print("does not exist", file=sys.stderr) 
    print("Exception: {err}", file=sys.stderr) 
    sys.exit(1)

## install php

Installationen skaber mapperne /etc/php/7.3/cli cgi der hver indeholder php.ini, der skal opdateres 

.. todo kan opdatere en php.ini fil afventer, at der eksekveres et eksempel, hvor php er installeret

.. todo juster opdatering af install_php.update_php_ini() så den tager en tuple med path til php.ini eksempelvis cli og cgi med date.time og intl.error

**installationen af php-xdebug** opretter en /etc/php/7.3/mods_available/xdebug.ini

**xdebug.ini** indeholder blot aktivering af **zend_extension=xdebug.so**. Dvs. at øvrige parametre er default. Der er automatisk skabt link herfra til cgi, cli og fpm ./conf.d/320-xdebug.ini.

Se mine **xdebug vejledninger**

.. todo hvilke af mine egne parametre er reelt default værdierne

.. todo config.ini i dette projekt er til vagrant og docker instanser, hvad er standard for alm maskiner.

.. todo kan nodejs installeres ved fra scriptet at hente

   - key
   - source_string

   derefter kan opdatering foregå som for mongodb m.fl.

## automatisering af de manuelle processer

- forsøg at lave nendestående uden anvendelse af modulet **request** idet det så er muligt at undvære dette modul hvorefter det ikke er nødvendigt at foretage forberedende installation på et image men **install_kubuntu.py** kan eksekveres umiddelbart.

- vejledninger -> linuxinstall -> installationsscript de **efterfølgende manuelle opgaver**

- tjek resten af vejledninger -> linuxinstall for yderligere opgaver, der skal automatiseres

- tjek også projekt devops puppet scripts herunder også yaml filerne og filerne med diverse config filer

- **virtualbox**, der må være en CLI cmd som installerer en guest addition

- evt anvendelse af jinja2 templates

## anaconda jupiterlab eller spider

- opdater anaconda eksempler med uddrag fra dette repository

- ryd op i mappen source/demos

## Opdater PyCharm

## apt-key fingerprints

fingerprint for en apt-key kan tjekkes med

    key-apt fingerprint 0EBFCD88
    
viser oplysninger om docker key, kan placeres i repository.ini udføres og tjekkes

## verifikation af donwlodede filer med sha256sum

##  Eksekvering af scripts fra CLI

Scripts skal hvor relevant kunne aktivers fra command line

## Tjek alle exceptions

- find Exceptions
- lav custom exceptions

## testcases med unittest

https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

med PyCharm support
- Pytest https://docs.pytest.org/en/latest/
- UnitTest (PyUnit) - Standard library https://docs.python.org/3.7/library/unittest.html
- Django har sit eget testframework
- flask dokumentationen viser PyTest eksempler
