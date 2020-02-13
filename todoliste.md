# Opgaveliste


ændring af print ved exception, 

except Exception as err
    print("does not exist", file=sys.stderr) 
    print("Exception: {err}", file=sys.stderr) 
    sys.exit(1)

## install php

script 05-install_php.sh

kan downloade og verificere composer

todo: kan opdatere en php.ini fil afventer, at der eksekveres et eksempel, hvor php er installeret

todo juster opdatering af install_php.update_php_ini() så den tager en tuple med path til php.ini eksempelvis cli og cgi med date.time og intl.error

## anaconda jupiterlab eller spider

- opdater anaconda eksempler med uddrag fra dette repository

- ryd op i mappen source/demos

## Opdater PyCharm

## automatisering af de manuelle processer fra

- vejledninger -> linuxinstall -> installationsscript de **efterfølgende manuelle opgaver**

- tjek resten af vejledninger -> linuxinstall for yderligere opgaver, der skal automatiseres

- tjek også projekt devops puppet scripts herunder også yaml filerne og filerne med diverse config filer

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

