.. _ekstra-diske:

=========================
Ekstra diske og wdmycloud
=========================
Opdateret oktober 2020

WdMycloud tilsluttes på fysiske og virtuelle maskiner

De ekstra diske på Komplett og Esprimo tilsluttes kun på respektive fysiske maskiner.

De eksterne diske på Komplett
=============================
De eksterne diske på Komplett har følgende identifikation, som kun ændres hvis en disk reformateres.

- 1 TB SSD mountes på /home/projects
   - serienummer S3Z9NY0M409052E
   - UUID dde1bf8b-3552-4709-a6d7-5f3605d966a3

- 2 TB HDD mountes på home/data
   - serienummer  Z4ZC9EBT
   - UUID 3865c960-e586-4b04-8745-fb1ccabaf412

- 2 TB HDD mountes på /home/backup
   - serienummer Z4Z8X6FA
   - UUID b6af222b-5148-4d63-b8f2-9acc1591207f

Tjek filen **config/extradiske** som indeholder registreringen, der anvendes af installationen.

Ekstra diske på Esprimo
=======================
- 1 TB HDD mountes på /home/projects

   - serienummer STH6L7MQ0256KS
   - UUID a8768fc6-4ef3-4310-b27c-fd83a39416fb

1 TB HDD mountes på /home/data

-  serienummer STH6L7MQ01TAYS
-  UUID d31e8166-403c-41a7-973c-eda1490799aa

Tilslut øvrige harddiske (fysisk maskine)
=========================================
Mount points og opdatering af fstab foretages i scriptet 01_prepare_install  -> moduler/install_prepare

.. important:: Manuel installation kræver anvendelse af af **Gnome Disks** 
   Programmet findes i Discover under system settings (gnome-disk-utility)

Installations kan foretages/opdateres med::

      cd python-demo/moduler
      sudo ./extra-diske.py

   Scriptet opretter mount points og opdateret /etc/fstab

Konfigurationsfilen: **config/extradiske** indeholder de ekstra diske på Komplett og Esprimo. Scriptet tjekker for om disken findes på den aktuelle maskine inden den foresøger at opdatere /etc/fstab.

Tilslut wdmycloud
==================
Mount points og smbcredentials oprettes som en del af 01_prepare_install.py -> moduler/install_prepare

Seperat installation::

   cd python-demo/moduler
   sudo ./wdmycloud.py
