.. index:: Virtualbox Manjaro
.. _virtualbox-manjaro:

===========================
Virtualbox som Manjaro Host
===========================
Opdateret juni 2020

Manjaro kan installeres som guest på en Virtualbox Host.

.. note:: Det er bøvlet at installere på VirtualBox. Det ikke er muligt at skalere skærmen før vbox guest additions er installeret

.. important:: Hostens VirtualBox skal være samme version som guest aditions i Manjaro repository

- Anvend Manjaro minimal KDE iso fil
- Vælg Linux type Archlinux 64 bit
- display: 128 MB, VMSVGA, UDEN 3D Acceleration
- attach iso som IDE som virtual optical disk, husk at markere live CD
- USB 3.0
- Vælg dansk systemsprog
- I stedet for at genstarte standses maskinen og iso filen fjernes

Ref. https://wiki.manjaro.org/index.php?title=Virtualbox

på Manjaro anvendes den traditionelle vbox guest aditions package ikke i stedet ::

   sudo pacman -S linux54-virtualbox-guest-modules
   sudo pacman -S virtualbox-guest-utils

   sudo systemctl enable vboxservice.service
   sudo gpasswd -a $USER vboxsf
   stands og start ej genstart

Hvis der er ikke kan scaleres når vmsvga er anvendt:

- fjern vmware video med **sudo mhwd -r pci video-vmware**
- stands den virtuelle maskine og skift i settings til vboxsvga så funkter det

https://forum.manjaro.org/t/manjaro-in-virtualbox-cannot-change-display-resolution/118120

Manjaro og Linux kernels
