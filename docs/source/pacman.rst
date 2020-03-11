.. index: !Pacman

.. _pacman:

========================================
Pacman installation af software packages
========================================
Opdateret marts 2020

Installation Pacman
===================

Et programs dependencies findes i appen, der anvendes til program administration og på archlinux.org/packages

**Hent og udfør opdateringer**::

    pacman -Syu

.. important:: Systemet skal opdateres før enhver installation af sw packages!

**Installation af en package**::

    pacman -S <packagename>

**Installation af uden bekræftelse**::

    pacman -S --noconfirm <packagename>

**vis detaljeret info om en package**::

    pacman Si <packagename>

Hvis pacman Si returnerer 1 så findes pakken ikke

**Vis alle de installerede packages**::

    pacman -Qs [packagename]

Hvis en pakke ikke er installeret returnerer pacman -Qs statuskode 1

Da pacman gemmer alle de gamle udgaver af downloadede psackages og det er en rullende distribution, så vokse pacman cache.

**Oprydning med**::

    paccache --remove

Installation fra AUR
====================
AUR packages er brugergenererede BUILDS.

pamac CLI anvendes ved installation af AUR packages

Eksempel med mongodb
====================
Der anvendes kommandoen::

    pamac install mongodb-bin

Der skal interaktivt svares på en antal spørgsmål.

.. important:: Svar ja til om build filen skal redigeres.

    Her kontrolleres scriptet for hvad downlodes og hvad foretages under installationen

Indholdet i mongodb.deb
-----------------------
mongodb-bin downloader en debian installationsfil ekstraherer indholdet med GNU **tar** archive manager.

Pamac tjekker for om forudsætningerne er installet og installere rom nødvendigt.

Herefter foretages installationen ved at kopiere de enkelte dele på plads.

.. note::

    Det er formentlig sådan dpkg i princippet fungerer.

    Det er ikke alle debian packages, hvor denne model fungerer på Arch Linux/Manjaro

