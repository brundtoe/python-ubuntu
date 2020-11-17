.. index:: !MongoDB
.. _mongodb:

============================
MongoDB Manjaro og Archlinux
============================
Opdateret november 2020

MongoDB findes grundet licensrettighederne ikke i det officielle repository.

MongoDB skal installeres fra AUR. Der er to muligheder:

- mongodb-bin og mongodb-tools-bin
- mongodb og mongodb-tools (skal kompileres og det tager meeget lang tid)

.. note:: Alternativt anvendes MongoDB kun i docker container

Installation på Manjaro
=======================

Det letteste er at gøre det fra Pamac Manager (GUI) til installation, opdatering og fjernelse af software.

alternativt installeres fra terminalvindue::

    pamac install mongodb-bin
    pamac install mongodb-tools-bin

Der promptes for en række spørgsmål og det vælges at redigere build source (PKGBUILD filen) for at kontrollere hvorfra der downloades m.v.

De to filer indeholder Debian sw pakke som blot pakkes ud og kopieres.

Daemon startes med::

    sudo systemctl start mongodb

Installation på Archlinux
=========================
Der er ikke noget program som kan downloade og build AUR packages på archlinux. I stedet anvendes terminalvindue.

.. note:: eksemplet er fra va-devops/archer

Til brug for build af package installeres pakken base-devl::

    sudo pacman -Syu --needed base-devel git

Hent repository https://aur.archlinux.org::

  cd /home/vagrant/
  mkdir build
  git clone https://aur.archlinux.org/mongodb-bin.git
  git clone https://aur.archlinux.org/mongodb-tools-bin.git

Tjek indholdet i de downloadede pakker herunder de krævede pakker::

    cd mongodb-bin
    makepkg -si

    cd ../mongodb-tools-bin
    makepkg -si

De binære udgave, som downloader de officielle debian packages downloades da det tager en hulens tid at builde fra sourcecode.

Installationen opdateres ved at pulle fra repository og builde igen.

Start serveren::

    sudo systemctl start mongodb

.. seealso:: Vejledning om database connection i vejledning om MongoDB GUI (NoSQLBooster)