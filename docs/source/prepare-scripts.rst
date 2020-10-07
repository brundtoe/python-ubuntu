
.. _prepare-scripts:

==================================
Klargøring til script installation
==================================
Opdateret oktober 2020

Forudsætninger: 

- operativsystem er installeret

Opdatering af settings
======================

Font i terminal og kate::

   Noto Sans Mono** alternativ **DejaVu Sans Mono** font size 11 pt

GNOME/GTK Applications style
============================
Der anvendes Manjaro med KDE og det kan være nødvendigt at ændre applications style for GNOME/GTK. 

Det berører SmartGit og FreeFile Sync.

I **System Settings -> Application Style -> configure GNOME/GTK Application style** ændres for GTK2 og 3 til Theme **Adwaita**.

Ref. https://www.syntevo.com/blog/?tag=gtk

Installation af git
===================
**Kubuntu** Installer git og vim med::

    sudo apt install -y git vim

**Manjaro** installation af vim::

    sudo pacman -S vim

Konfiguration af git user::

   git config --global user.name Jackie
   git config --global user.email brundtoe@outlook.dk
   git config --global core.editor vim

Opret ssh key::

    cd ~/.ssh

Tilføj på **Kubuntu**::

    ssh-keygen -b 4096
    ssh-add

Tilføj på **Manjaro**::

    eval $(ssh-agent)
    ssh-add ~/.ssh/id_rsa

Tilføj public key til GitHub og Bitbucket konti.

Visual Studio Code
===================

**Kubuntu** Installation af Visual Studio code::

   sudo snap install --classic code

**Manjaro** installation af Visual Studio Code::

    pacman -S Code

- Installer Python extension
- Installer TODO extension
- Kopier settings fra Hosten ~/.config/Code/User/settings.json

Clone repository fra Github (uden USB stick)
============================================
Repositoriet clones på **virtuelle maskiner**::

   mkdir ~/sourcecode
   cd sourcecode
   git clone git@github.com:brundtoe/python-ubuntu.git

Clone data repositoriet
=======================
::

    cd /home/jackie
    git clone git@github.com:brundtoe/dumps

Installation af Python moduler
==============================
Installation på **Kubuntu**::

   sudo apt install -y python3-pip python3-venv python3-setuptools

Installation på **Manjaro**::

    sudo pacman -S --noconfirm python-pip python-setuptools

Python indeholder venv og virtualenv

Klargøring Af det virtuelle environment
=======================================

.. code-block:: bash

   cd python-ubuntu
   python3 -m venv venv
   source venv/bin/activate
   pip3 install -r requirements-local.txt
   python3 setup.py develop

.. important:: Installation skal foretages med det virtuelle  environment, og python-ubuntu skal være installeret i development mode.

.. caution:: kompilering af Shpinx doc forberedes

   Skift til terminalvindue med det globale environment og udfør::

      cd python-ubuntu
      sudo pip3 install -r requirements-global.txt

Opdatering af konfigurationsfilen
=================================
Filen **config/config.ini** indeholder konfigurationsoplysninger, som anvendes i de enkelte scripts. Config.ini indlæses med Python modulet Configparser.

Opdater konfigurationen i forhold til den anvendte hardware og opdater evt til aktuelle versioner af softwaren. Følgende afsnit i config.ini opdateres som minimum.

* [Common] med user, host og seneste software versioner
* gtk2 er krævet af FreefileSync

På Kubuntu kontrolleres desuden::

* [extra.programs] Justeres i forhold til maskinens anvendelse

På Manjaro kontrolleres desuden::

  - pakker i programs.sh
    - node.js er normalt seneste lst version. Find navnet på https://nodejs.org

.. caution:: Husk at opdatere **config/.env_devlop** med password til **wdmycloud**

Restore data (fysisk maskine)
=============================
- Data fra backup af Home/jackie restores
   - Documents
   - dumps (fra GitHub repository jf. ovenstående)
   - Pictures
   - .thunderbird
   - Firefox favoritter
   - log på Postman og importer evt fra dumps/Postman

Øvrige data findes på de øvrige diske og skal ikke restores

.. seealso:: Udfør evt. opgaver jf. Vejledning om :ref:`ekstra-diske`

   Fortsæt til installation med script

   - :ref:`Kubuntu <kubuntu-scripts>`
   - :ref:`Manjaro <manjaro-scripts>`