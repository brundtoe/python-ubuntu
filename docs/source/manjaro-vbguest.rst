.. index:: Virtualbox Manjaro
.. _manjaro-vbguest:

===========================
Manjaro som Virtualbox Gæst
===========================
Opdateret juni 2020

Manjaro kan installeres som guest på en Virtualbox Host.

.. seealso:: Manjaro som host fremgår af vejledning om :ref:`manjaro-vbhost`

.. note:: Display skal være VBoxSVGA for at kunne resize display under installation

.. important:: Hostens VirtualBox skal være samme version som guest aditions i Manjaro repository

- Anvend Manjaro minimal KDE iso fil
- Vælg Linux type Archlinux 64 bit
- general copy bidirectional
- system 4 CPU

- display: 16 MB, VBoxSVGA (jf. manjaro wiki)

- Marker IDE som virtual optical disk, som live CD. Der promptes for iso fil når maskinen startes.
- USB 3.0
- I stedet for at genstarte standses maskinen og iso filen fjernes

Ref. https://wiki.manjaro.org/index.php/VirtualBox

På Manjaro anvendes den traditionelle vbox guest additions package ikke i stedet.

Find den akutelle kerne::

   mhwd-kernel -li

Viser der aktuelt aktive kerne, som skal anvendes til installation af guest modulerne::

   sudo pacman -Syu linux58-virtualbox-guest-modules virtualbox-guest-utils

Herefter skal vbox service enables::

   sudo modprobe vboxguest vboxvideo vboxsf
   sudo systemctl enable --now vboxservice.service
   sudo gpasswd -a $USER vboxsf

stands og start ej genstart

Opdatering af geust additions
=============================
Det er muligt at anvende standard guest additions på sædvanlig vis. Dete foretages hvis der ikke er frigivet en manjaro/archlinux udgave, der svarer til den  installerede kernel.

Det kræver installation af **dkms, perl og linux-headers**. Se standard vejledningen om virtualbox.
