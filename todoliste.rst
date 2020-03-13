===========
Opgaveliste
===========

Kubuntu og Manjaro Docker afprøvning
====================================

Docker konfiguration (build af images og provisionering af databaser)

Linux process control
=====================

ps
--
Kommandoden *ps* anvendes til at vise de kørende proceser. Det er et snapshot der vises.

====    =============================================
ps a    processer med terminalvindue for alle brugere
ps -A   alle processer
ps -T   alle processer i det aktuelle vindue
ps -x   alle processer uden tty
====    =============================================

Via alle proceser med og uden tty og vis usernavn::

    ps -aux

Eller med flere detaljer herunder parent PID (PPID)::

    ps -lax

Command navne der vises som [kommando] er Linux kernens threads.

Vis kun for et enkelt program::

    ps -ax | grep pycharm

En hurtig oversigt til brug for at finde PID og slå en process ihjel::

    ps -e | grep firefox

Kommandoen **pgrep** er en kombination af ovenstående anvendelse af ps og grep::

    pgrep firefox

top og htop
-----------
top og htop viser de proceser, der har det største ressourceforbrug.

De anvender hele terminalvinduet og opdateres en gang hvert andet sekund.

Output er opdelt i to dele. Headeren som viser sumarisk status og body, som viser en linje for hver proces. Det viset indhold svarer til **ps -aux**

top header er udelukkende tegnbaseret, medens htop header viser en grafik af systembelastningen.

top er installeret på alle distirbutioner, medens htop skal installeres på Ubuntu.

top visning af felter kan konfigureres ved at taste **f** eller **F**. Flere muligehder for konfiguration fremgår af https://www.computerhope.com/unix/top.htm

htop viser for neden en menulinje med valgmuligheder herunder konfiguration og help.

Det er i htop muligt med cursoren at vælge en linje og standse (kill) en process.

Se mere om htop http://hisham.hm/htop/

Signals
=======
Signals er process-level interupt requests som sendes til en proces fra en anden proces, typisk fra parent eller kernen/systemd.

De mest anvendte signaler er::

========
3   QUIT    svarer til TERM og producerer et core dump
9   KILL    Det ultimatives signal for at standse en process
15  TERM    En anmodning om at afslutte og rydde op.
18  CONT    Fortsæt processen.
19  STOP    Stands processen indtil CONT modtages

Der anvendes ofte en notationen med prefix SIG eksempelvis SIGKILL

Vis alle signaler::

    kill -l

Send kill signal
----------------

En proces standses ved at anvende dens PID eller JOB nummer ::

    sudo kill -n 9 PID
    sudo kill -s SIGKILL PID

jobs vises med kommandoen jobs

En process kan også standses med dens procesnavn::

    sudo killall httpd


foreground og background processer

- https://www.howtogeek.com/440848/how-to-run-and-control-background-processes-on-linux/




chroot
======
chroot er en kommando der anvendes til at afgrænse en del af filsystemet så processer fungerer i et aflukke og ikke kan tilgå proceser og filer udenfor dette.

https://en.wikipedia.org/wiki/Chroot

.. todo har så vidt jeg husker set dockerfiles der starter med chroot?

Manjaro debian packages
=======================
se mere https://wiki.archlinux.org/index.php/Creating_packages_for_other_distributions

Se bla.

- https://www.maketecheasier.com/install-deb-package-in-arch-linux/

på baggrund heraf laves en beskrivelse

.. todo hent eksempelvis freefilesync-bin eller mongodb-bin

    - lav en ny clone
    - tjek output fra installationen for at se hvilke værdier der anvendes for de ikke explicit definerede variable.
    - hvortil downloades filerne der anvendes til build


Kubuntu Apache2 site definition
===============================
en apache site konfiguration med
   - opdatering af hosts
   - en site konfig til /etc/apache2/sites-available
   - enable med a2ensite <filnavn>

ref. file:///home/jackie/SphinxDoc/source/webserver/Apache.html#oprettelse-af-virtuel-host

Kubuntu nginx site konfiguration
================================
Se eksempel i mappen devops-files

Manjaro http site konfiguration
===============================
Se eksempel i mappen devops-files og evt. i docker_standard

Manjaro nginx site konfiguration
================================
Se eksempel i mappen devops-files og evt. i docker_standard

Udenstående efterfølgende på Komplett eller Esprimo
===================================================

   - vagrant
   - laravel/homestead

Udestående ubuntu gnome
=======================
ubuntu 18.03 indeholder en gammel version af composer (1.6.3)

Testcases med unittest
======================

https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

med PyCharm support

- Pytest https://docs.pytest.org/en/latest/
- UnitTest (PyUnit) - Standard library https://docs.python.org/3.7/library/unittest.html
- Django har sit eget testframework
- flask dokumentationen viser PyTest eksempler
