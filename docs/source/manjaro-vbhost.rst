.. index:: Virtualbox Manjaro
.. _manjaro-vbhost:

===========================
Manjaro som VirtualBox Host
===========================
Opdateret oktober 2020

Manjaro kan være host for VirtualBox

Installation af VirtualBox på Manjaro Host
==========================================
Find den aktuelle linux kerne::

    mhdw-kernel -li


Installation med linux58::

    sudo pacman -Syu virtualbox linux58-virtualbox-host-modules

Genstart maskinen

Tilføj user til vboxsf::

    sudo gpasswd -a $USER vboxsf

Genstart endnu en gang, selvom det principielt er tilstrækkeligt at logge ud og ind igen.

Virtualbox Guest additions
==========================
Tjek VirtualBox versionen::

    vboxmanage --version

.. caution:: Jf. den officielle vejledning https://wiki.manjaro.org/index.php/VirtualBox

   kan man anvende guest additions fra https://virtualbox.org, men det fejler

Via Add/Removal software

   - aktiver AUR
   - installer virtualbox-ext-oracle
   - installer virtualbox-guest.iso

Oprettelse af den virtuelle maskine
===================================
For virtuelle gæster der er baseret på Debian og Ubuntu baserede distirbutioner

   - display skal være VMSVGA

.. seealso:: For Manjaro gæster se vejledning om :ref:`manjaro-vbguest`

Opret den virtuelle maskine::

   - Den virtuelle maskine skal efter installationen af OS have et tomt IDE Optical drev, for at kunne installere guest additions.

Installer på Kubuntu::

   sudo apt install -y gcc make perl

.. caution: Det virker dog ofte uden, da det kun er build til andre kerner end den aktuelle som ikke er mulig.





