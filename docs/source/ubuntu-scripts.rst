.. index:: Ubuntu Scripts
.. _ubuntu-scripts:

==============
Ubuntu Scripts
==============
Opdateret september 2020

Denne vejledning beskriver de enkelte scripts, der anvendes ved ubuntu installation


Scriptet 01_prepare_install-py
------------------------------
Scriptet foretager den grundlæggende konfiguration som betår af:

* Definition af timezone
* Oprettelse af mount points for interne diske
* /etc/sysctl.d/99-local.conf opdatres med fs.inotify.max_user_watches
* Oprettelse af

   * mappen /home/{user}/bin
   * mappen /home/ {user}/programs
   * filen .vimrc
   * images som anvendes af desktop entries koppieres til ~/bin/images

* opdatering af Linux

Scriptet 02_install_requirements.py
-----------------------------------
Scriptet installerer en række basale programmer, som defineret i config.ini. alle programmer er uden GUI.

Scriptet 03_intall_requirements.py
----------------------------------
Scriptet opretter en række software repositories, som er en forudsætning for installation af den seneste udgave af software, der normalt findes i ældre udgaver på en Ubuntu/Kubuntu/Debian installation.

* MongoDB
* VirtualBox
* Docker
* Google Chrome
* Puppet
* Node.js

Scriptet 04_install_extra.py
----------------------------
Scriptet indeholder installation af en række ekstra programmer.

.. note:: Husk afsnittet [extra.programs] skal tilpases den aktuelle maskines anvendelse.

