.. _subprocess-management:

=====================
Subprocess management
=====================

Pythons **module subprocess** gør det muligt at udføre nye processer herunder eksempelvis at anvende operativsystemets command line interfaces og kommunikere direket med input/output og error pipes og return code fra den enkelte proces.

Ref. https://docs.python.org/3.8/library/subprocess.html

Enkel anvendelse
================
At tilføje en bruger til en gruppe:

.. code-block:: python

    import shlex
    import subprocess

    cmd = shlex.split(f'usermod {options} -G {group} -a {user}')
        res = ''
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if res.returncode:
                raise Exception
        except Exception as err:
            print()
            sys.exit(res.stderr.decode('UTF-8'))
        print(res.stdout.decode('UTF-8'))

En kompleks anvendelse
======================
Eksemplet i **common/mysql_data.py** 

- Åbner en fil **../config/mysql_data**, der indeholder en række sql statements
- opretter en kommunikationskanal med **mysql -u jackie -p**
- kommunikationskanalen prompter for password
- filen anvendes som stdin
- proc.communiate() anvender filen som input, da communicate kaldes uden input parameteren
- kaldet fejler hvis en sql sætning fejler

.. code-block:: python

   from subprocess import Popen

   try:
       filename = '../config/mysql_data'
       with open(filename) as file:
           proc = Popen('mysql -u jackie -p',shell=True, stdin=file,
               stdout=PIPE, stderr=PIPE, universal_newlines=True)
           out, err = proc.communicate()
   except Exception as err:
       print(err)
       sys.exit('opdatering af mysql data fejlede')
   else:
       print('Mysql databasen er opdateret')
