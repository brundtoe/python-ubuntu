Opgaveliste
===========

nodejs
------
Bliver ikke installeret i den nyere udgave fordi nodejs allerede er installeret på Kubuntu.

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

**requests** er nødvendig for at der kan foretages follow_redirect ved download

Ref. https://requests.readthedocs.io/en/master/user/quickstart/#redirection-and-history

Jinja2 templates
================
Jinja2 anvendes som template funktion, der producerer desktop entries til

script **source/desktopfile.py**

   - freefilesync,
   - nosqlbooster,
   - postman

Desktop items (KDE)
===================

.. note:: Når KDE anvendes som GUI så kan man

   - tilføje en fil herunder programmer til en aktivitet i en folder widget
   - trække filen ud på dekstop og vælge at oprette en genvej/link
   - på desktoppen højreklikke vælge create new og

      - basic link, som kan oprette link til fil eller mappe.
      - link to applikation, som opretter et gnome desktop entry

script xdebug_ini.py
====================

Genererer xdebug.ini til brug for konfig af XDebug afhænig af om det er et host miljø eller en guest (vbox image skabt med vagrant)

Udestående opgaver
==================

.. todo alle installationsscripts skal kunne udføres som selvstændige pgm med en

   - #!/usr/bin/env python3
   - if __name__ == __main__
   - se input  til **if** statement fra install_kubuntu

.. todo dokumentation

   - dokumentation med docstrings i de enkelte funktioner samt dok af parametrene
- alle funktioner skal afslutte med sys.exit('meddelelse')

.. todo måske

   - mysql-server konfiguration af root med pwd og en ny user (19.10 er skiftet til version 8.x)
   - laravel/homestead
   - visual studio code
   - docker konfiguration (build af images og provisionering af databaser)

anaconda jupiterlab eller spider
================================

- opdater anaconda eksempler med uddrag fra dette repository

- ryd op i mappen source/demos

.. todo Opdater PyCharm


apt-key fingerprints
====================

fingerprint for en apt-key kan tjekkes med

    key-apt fingerprint 0EBFCD88
    
viser oplysninger om docker key, kan placeres i repository.ini udføres og tjekkes

verifikation af donwlodede filer med sha256sum
==============================================

Tjek alle exceptions
====================

- find Exceptions

testcases med unittest
======================

https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

med PyCharm support

- Pytest https://docs.pytest.org/en/latest/
- UnitTest (PyUnit) - Standard library https://docs.python.org/3.7/library/unittest.html
- Django har sit eget testframework
- flask dokumentationen viser PyTest eksempler
