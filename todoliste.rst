===========
Opgaveliste
===========

TODO alle scripts skal have module docstring

TODO optimerings eksempel

- extra_diske.py
- wdmycloud.py
- smbcredentials.py
- add_mountpoints

udskriv og forsøg at optimere

herefter bør to funktioner

- update_fstab_wdmycloud
- update_fstab_extradiske

kunne indsættes i 01_prepare_install


TODO systemtime sættes til europe copenhagen

tjek pycharm vejl herom 

hvordan ser det ud i devops?

Kubuntu og Manjaro Docker afprøvning
====================================

TODO Docker konfiguration (build af images og provisionering af databaser)

Manjaro debian packages
=======================
se mere https://wiki.archlinux.org/index.php/Creating_packages_for_other_distributions

Se bla.

- https://www.maketecheasier.com/install-deb-package-in-arch-linux/

på baggrund heraf laves en beskrivelse

TODO hent eksempelvis freefilesync-bin eller mongodb-bin

    - lav en ny clone
    - tjek output fra installationen for at se hvilke værdier der anvendes for de ikke explicit definerede variable.
    - hvortil downloades filerne der anvendes til build

konfig af mysql server med charset og default collation
=======================================================

Se PyCharm databaser -> mysql om konfig af default charset og default collation

TODO konfig fil default charset og collation

    - Kubuntu
    - Manjaro

TODO scripting af

   - brugeroprettelse og
   - opdatering med aktuelle data (pas på i virtuelle maskiner her skal data også kopieres fra wdmycloud

Kubuntu Apache2 site definition
===============================
en apache site konfiguration med
   - opdatering af hosts
   - en site konfig til /etc/apache2/sites-available
   - enable med a2ensite <filnavn>

ref. file:///home/jackie/SphinxDoc/source/webserver/Apache.html#oprettelse-af-virtuel-host

Kubuntu nginx site konfiguration
================================
Se eksempel i mappen devops-files

Manjaro http site konfiguration
===============================
Se eksempel i mappen devops-files og evt. i docker_standard

Manjaro nginx site konfiguration
================================
Se eksempel i mappen devops-files og evt. i docker_standard

Udenstående efterfølgende på Komplett eller Esprimo
===================================================

   - laravel/homestead

Testcases med unittest
======================

https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

med PyCharm support

- Pytest https://docs.pytest.org/en/latest/
- UnitTest (PyUnit) - Standard library https://docs.python.org/3.7/library/unittest.html
- Django har sit eget testframework
- flask dokumentationen viser PyTest eksempler
