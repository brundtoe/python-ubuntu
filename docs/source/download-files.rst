.. index:: !Download Files
.. _download-files:

==============
Download Files
==============
Opdateret februar 2020

Det er muligt at downloade filer med **urllib** fra Pythons standard library, med **urllib3** eller med modulet **requests**

**urllib3** og **requests** er mere programmørvenlige end **urrlib** bl.a. i forbindelse med download hvor http request bliver redirected. De to førstnævnte følger defualt en redirigering.

Download af store filer skal opdeles i blokker for at reducere memory forbruget.

Urllib
======
Urllib fra Pythons standard library kan anvendes til download af filer, hvor der er sikkerhed for, at der ikke foregår redirection.

