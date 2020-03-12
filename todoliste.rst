===========
Opgaveliste
===========

Kubuntu og Manjaro Docker afprøvning
====================================

Docker konfiguration (build af images og provisionering af databaser)

Linux process control
=====================
Kommandoden *ps* anvendes til at håndtere de kørende processer.

.. todo læs i bogen Unix og Linux systemadministraiton, 5th Edition

chroot
======
chroot er en kommando der anvendes til at afgrænse en del af filsystemet så processer fungerer i et aflukke og ikke kan tilgå proceser og filer udenfor dette.

https://en.wikipedia.org/wiki/Chroot

.. todo har så vidt jeg husker set dockerfiles der starter med chroot?

Manjaro debian packages
=======================
se mere https://wiki.archlinux.org/index.php/Creating_packages_for_other_distributions

Se bla.

- https://www.maketecheasier.com/install-deb-package-in-arch-linux/

på baggrund heraf laves en beskrivelse

.. todo hent eksempelvis freefilesync-bin eller mongodb-bin

    - lav en ny clone
    - tjek output fra installationen for at se hvilke værdier der anvendes for de ikke explicit definerede variable.
    - hvortil downloades filerne der anvendes til build


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

   - vagrant
   - laravel/homestead

Udestående ubuntu gnome
=======================
ubuntu 18.03 indeholder en gammel version af composer (1.6.3)

Testcases med unittest
======================

https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

med PyCharm support

- Pytest https://docs.pytest.org/en/latest/
- UnitTest (PyUnit) - Standard library https://docs.python.org/3.7/library/unittest.html
- Django har sit eget testframework
- flask dokumentationen viser PyTest eksempler
