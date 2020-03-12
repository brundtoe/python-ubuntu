.. index:: !systemd
.. _systemd:

=======
systemd
=======
.. seealso:: Bogen Unix and Linux System administration 5th edition.

Systemd er en system og service manager som administrerer et Linux system. Den kører som proces med PID =1.

Systemd initieres som proces med PID = 0, når Linux kernen er loaded og har afsluttet initialiseringsprocessen.

systemd har flere funktioner med dens mål er at sikre at systemet til enhver tid kører med det rette mix af services og daemons**.

system fungerer som en dirigent og har kun meget lidt kendskab til disse opgaver. Den eksekverer en række kommandoer og scripts, som er defineret til udførelse i en given kontekst.

På Ubuntu systemerne findes reminiscenser herfra i mapperne /etc/rc.0 - /etc/r.07 hvor nummeret identificere et given **run level**. Disse reminiscenser findes for at kunne håndtere services og daemons, som ikke er porteret til systemd.

På Ubuntu findes de scripts, der anvendes til at starte og standse services i:

    - /etc/init (konfigurationsscript for user installerede services)
    - /etc/init.d (scripts som starter og standse services)

Manjaro (Arch Linux) anvender ikke konfigrurationsfiler i /etc/init eller scripts i /etc/init.d. Scripts findes i /usr/bin

En service betegnes i **systemd** som en unit og findes normalt i:

    - /urs/lib/systemd/system eller
    - /lib/systemd/system

På Manjaro og Ubuntu 19.10 er **/lib** et link til **/usr/lib**

Units kan indeholde beskrivelser af afhængigheder til andre units.

Unit beskrivelserne i **/usr/lib/systemd/system** må ikke ændres, da de bliver overskrevet ved systemopdateringer.

Hvis der er bhove for at ændre en standard unit beskrivelser så oprettes en et fragment af en unit fil, som alen indeholder ændringerne efter denne model (eksempel nginx)::

    sudo systemctl edit nginx-service

Det åbner system editoren (nano eller vim) og de ændrede parametre eksempelvis en custom nginx.conf fil::

    [Service]
    ExecStart=
    ExecStart=/usr/sbin/nginx -c /usr/local/www/nginx.conf

Den første **ExecStart=** er ndøvendig for at nulstille den oprindelige værdi.  filen gemmes automatisk med navnet::

    /etc/systemd/system/nginx.service.d/override.conf

Path **/etc/systemd/system/nginx.service.d** er obligatorisk for ningx.service medens filnavnet override.conf er best practice. Kravet er blot at det skal være en \*.conf fil.

Det er ikke muligt at overrule [Install] sectionen i en unit file.

Opret filen /etc/systemd/system/ningx.service.d/override

administration af systemd
=========================
Systemd administreres med kommandoen **systemctl**, som har en række subkommandoer.

Vise alle de installerede units::

    sudo systemctl list-unit-files

Vis alle kørende processer::

    sudo systemctl list-units

Herudover anvendes typisk sub commands:
    - enable
    - disable
    - start, stop, restart, status

Når en service er enabled så findes et link i::

    /etc/systemd/system/multi-user.target.wants/mysql.service

Linket peger på unit definitionen i /lib/system.d/system. Når service disables så fjernes dette link

Visning af service loggen
=========================
Vis de seneste entries i loggen::

    systemctl -xe

Vi de seneste entries for mysql::

    systemctl -e -u mysql

