Opgaveliste
===========

nodejs
------
Bliver ikke installret i den nyere udgave fordi nodejs allerede er installeret på Kubuntu.

- kan løses ved som afslutning på installationen at udføre en apt update && apt upgrade scriptet **apt_update.py**

automatisering af de manuelle processer
=======================================

- **VBoxManage** er det CLI som anvendes til administraiton af en VirtualBox installation. Den har samme versionsummer som VirtualBox, som findes med::

   **VBoxManage --version | awk -Fr '{print $1}'

.. caution:: Ovenstående fejler hvis der anvendes dobbelt gnyffer "{print $1}"

Denne model for at finde et versionsnummer er følsom overfor udviklerens ændirnger af et program og kan ikke generaliseres men skal for hvert program tjekkes i terminalen før der kan skrives et program.

Scriptet **demos/is_installed.py** viser hvordan det kan gøres.

.. caution:: kommandoen **apt** viser en warning om, at den ikke har et stabilt interface, når den anvendes i script. Forsøg har vist, at awk ikke fungerer med output fra **apt**

   Husk i øvrigt at awk behandler hver linje i output, Derfor bør grep anvendes til at finde den relevante linje, inden et flerlinje putput pipes gennem awk.

Python udgaven af find VirtualBox versionen via VBoxManage::

   cmd = 'VBoxManage --version'
   res = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
   version = re.search('\d{1,2}\.\d{1,2}\.\d{1,2}',res.stdout.decode('utf-8'))
   print(version.group(0))

.. note:: awk kan ikke anvende syntaksen med \\d men skal i stedet anvnede [0-9].

Efter installation af VirtualBox Extension Package findes Guest additions i **/usr/share/virtualbox/VBoxGuestAdditions.iso**

- Det er kun i mappen demos at modulet **requests** er anvendt. Derfor kan installationen udføres, når repo er clonet til maskinen, der skal installeres og konfigureres

**FreeFileSync** kræver en resuest som kan følge et redirect eksempelvis::

   curl -O -L https://freefilesync.org/download/FreeFileSync_10.20_Linux.tar.gz

Det er den letteste model, Python dok af standard library urllib er vanskelig til
gængelig for at udlede hvordan en follow-redirect udføres

Tredjeparts package **requests** følger default redirect

Ref. https://requests.readthedocs.io/en/master/user/quickstart/#redirection-and-history

- vejledninger -> linuxinstall -> installationsscript de **efterfølgende manuelle opgaver**

.. todo alle downloads skal foregå til /tmp
.. todo kan install_postmann og freefilsync og packer refaktoreres med en fælles kerne
.. todo install_jetbrains og freefilesync og packer skal ændre owner til {user} og mode til 775
.. todo flyt jetbrains-toolbox og freefilesync og postman til /home/{user}/programs
.. todo refaktorerring så alle der downloader og pakker en targz eller zip fil ud er ens - pas på angivelse af pakke algoritmen **gztar** eller **zip**
.. todo der skal med jinja2 eller tilsvarende laves en template med desktopfiles for freefilesyn og nosqlbooster samt postman
.. todo puppet_repo_install og install_smartgit skal anvende scriptet for smartgit og scriptet skal downloade til /tmp
.. todo refakotrering, så alle der downloader og installerer en .deb fil er ens (finde slettest ud fra config.ini
.. todo alle downloads bør anvende requests, så det sikres at evt. ændriner som medfører redirects ikke medfører fejl.

   - mysql-server konfiguration af root med pwd og en ny user (19.10 er skiftet til version 8.x)
   - laravel/homestead
   - visual studio code
   - docker konfiguration (build af images og provisionering af databaser)

anaconda jupiterlab eller spider
================================

- opdater anaconda eksempler med uddrag fra dette repository

- ryd op i mappen source/demos

Opdater PyCharm
===============

apt-key fingerprints
====================

fingerprint for en apt-key kan tjekkes med

    key-apt fingerprint 0EBFCD88
    
viser oplysninger om docker key, kan placeres i repository.ini udføres og tjekkes

verifikation af donwlodede filer med sha256sum
==============================================

Eksekvering af scripts fra CLI
==============================

Scripts skal hvor relevant kunne aktivers fra command line

Tjek alle exceptions
====================

- find Exceptions
- lav custom exceptions

testcases med unittest
======================

https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

med PyCharm support

- Pytest https://docs.pytest.org/en/latest/
- UnitTest (PyUnit) - Standard library https://docs.python.org/3.7/library/unittest.html
- Django har sit eget testframework
- flask dokumentationen viser PyTest eksempler
