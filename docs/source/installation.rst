.. index:: Ubuntu Installation
.. _installation:

======================================
Ubuntu installation med Python Scripts
======================================
Opdateret marts 2020

.. note:: Scripts er lavet på Kubuntu 19-10

I denne vejledning beskrives installation med script på en fysisk maskine eller en virtuel maskine, der skal anvendes til softwareudvikling.

.. note:: Scripts findes i repositoriet https://github.com/brundtoe/python-ubuntu

Backup
======

Forberedelser:

- ny kopi af Firefox genveje
- Backup med FreeFileSync
- Gem Jetbrains værktøjernes settings online
- Tjek installationsvejledninger

Installation af operativsystem
==============================
Den seneste udgave af Desktop Ubuntu LTS eller Kubuntu hentes på en Windows instans fra http://ubuntu.com/download/desktop og installers med Linux programmet Disks på en USB stick

.. caution::

   Ubuntu installeres på maskinens Solid State Disk. **Øvrige diske er deaktiveret**.

   Der er kun een skærm aktiv under installationen!

Software & Updates
------------------

.. important:: Skifte til Nvidia driver foretages som det første for at undgå bøvl med træg skærmdialog ved login.

- Under *software og update* søges efter additional drivers (På Kubuntu via Muon Software updates)
- Skift til Nvidia drive metapackage
- Det installerer også appen NVIDIA X Server Settings

.. note:: Nu kan skærm nummer to aktiveres

Det tjekkes via faneblad Ubuntu Software, at **multiverse** er aktiveret. Det kan også aktiveres med::

   sudo add-apt-repository multiverse && sudo apt-get update

Clone repository fra Github
===========================

Installer git med::

    sudo apt install -y git

Tilføj ssh key::

    cd ~/.ssh
    ssh-keygen -b 4096
    ssh-add

Tilføj public key til Github kontoen

Konfiguration af git user::

   git config --global user.name Jackie
   git config --global user.email brundtoe@outlook.dk

Den globale configuration for en bruger findes i **~/git/.gitconfig**

Repositoriet clones::

   mkdir ~/sourcecode
   cd sourcecode
   git clone git@github.com:brundtoe/python-ubuntu.git

Opdatering af konfigurationsfilen
=================================
Filen **config/config.ini** indeholder konfiguriatonsoplysninger, som anvendes i de enkelte scripts. Config.ini indlæses med Python modulet Configparser.

Opdater konfigurationen i forhold til den anvendte hardware og opdater evt til aktuelle versioner af softwaren. Følgende afsnit i config.ini opdateres som minimum.

* [Common] med user, host og seneste software versioner
* [extra.programs] Justeres i forhold til maskinens anvendelse

Installation med python scripts
===============================
Installationen udføres i et antal trin::

   cd ~/sourcecode/python-ubuntu/source

* 01_prepare_install.py
* 02_install_requirements
* 03_install_repositories
* 04_install_extra

.. note:: Alle scripts udføres med root access!

Scriptet 01_prepare_install-py
------------------------------
Scriptet foretager den grundlægende konfiguration som betår af:

* Definition af timezone
* Oprettelse af mount points for interne diske
* Oprettelse af mount points for wdmycloud
* Opdatering af fstab med mount points til wdmycloud
* /etc/sysctl.d/99-local.conf opdtres med fs.inotify.max_user_watches
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

.. note:: Huske afsnittet [extra.programs] skal tilpases den aktuelle maskines anvendelse

Supplerende installationer
==========================
Afhængig af maskinens avendelse kan følgende udføres **Uden root access**:

- install_php.py
- install_jetbrains.py
- install_vagrant.py
- install_packer.py
- install_postman.py
- install_freefilesync.py
- install_nosqlbooster.py
- desktopfiles.py (FreeFileSync, NoSQLBooster og Postman)

**med root efter ovenstående**

- vbox_ext_pack.py (Hvis VirtualBox er installeret
- groups.py
- chown.py (ændrer rettigheder rekursivt for directories i /home{user}/programs)





