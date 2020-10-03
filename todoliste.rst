===========
Opgaveliste
===========

TODO sshkey.py

skal tjekke om mappen .ssh findes og oprette den hvis den ikke findes

TODO gennemse scripts for muligheder for optimering

model for 01_prepare_install hvor indhold flyttes til moduler

alternativ systemopdateringer foretages udenfor scripts bortset fra de ubuntu specifikke

wdmycloud og fileoperations indehodler en funktionm addLine add_line som begge tilføjer en linje til en fil

TODO alle scripts skal have module docstring

TODO flere omlægninger af disk mounts

   flyt etablering af mount points til extra_diske.py hhv. wdmycloud for at holde funktionaliteten samlet.

   ekstra diske skal kun mountes hvis host er komplett.local eller esprimo.local ej på virtuelle maskiner.

   diskene har et andet UUID på esprimo.local så en config variabel skal anvendes til at vælge den rigtige fil med mount points

   Det bør også være muligt at anvende dynamisk user for wdmycloud. pt er jackie hardkodet, det kan løses ved at anvende str.split() og så udskifte path til .smbcredentials med den dynamiske uder hentet fra config.ini

   på virtuelle maskiner skal /home/projects dog oprettes

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

Optimering af scripts
=====================
tjek scritps for mulige optimeringer

Testcases med unittest
======================

https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

med PyCharm support

- Pytest https://docs.pytest.org/en/latest/
- UnitTest (PyUnit) - Standard library https://docs.python.org/3.7/library/unittest.html
- Django har sit eget testframework
- flask dokumentationen viser PyTest eksempler
