.. index: Manjaro Display
    :pair: Manjaro; Python

.. _manjaro-kde-display:

===================
Manjaro KDE display
===================
Opdateret oktober 2020

Det er et kendt problem, at der er bøvl med at resize display størrelsen.

VMware toools
=============
vmware tools installers automatisk når manjaro installeres. Der mangler formentlig en opdatering af intiramfs  som del af installationsprocessen for, at det kan virke stabilt.

Tjek instllation
================
følgende skal være installeret

- gtk2
- gtkmm

Tjek VMware menu -> view -> autosize -> Autofit Guest

Genstart af vmtools service
===========================
VMWare tools skal køre og den skal være enabled, så den startes under systemstart.

Genstart vmtools::

   sudo systemctl restart vmtoolsd

Opdatering af vmtoolsd.service
==============================

Tilføj i **/usr/lib/systemd/system/vmtoolsd.service** linjen **After-display-manager.service**::

   [Unit]
   Description=Open Virtual Machine Tools (VMware Tools)
   ConditionVirtualization=vmware
   After=display-manager.service

https://forum.manjaro.org/t/i-found-a-bug-with-vmware-tools-and-a-solution-why-is-this-bug-still-here/127648

Regeneringen af intiramfs
=========================

Initirams loader filsystemet og kernelmodulerne. Det har hjulpet at regenerere initrams.

Via System settings findes den aktuelle linux version (her 5.6)

Regnereringen foretages med::

   sudo mkinitcpio -p linux56

Herefter genstartes maskinen

Ref. https://classicforum.manjaro.org/index.php?topic=25467.0

