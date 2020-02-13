#!/usr/bin/env python

# GNU like SED command

from shutil   import move
from tempfile import NamedTemporaryFile

with NamedTemporaryFile(mode="w", encoding="utf-8", delete=False) as tmp_sources:
    with open("../../infile/php.ini") as sources_file:
        for line in sources_file:
            if line.startswith(";date.timezone"):
                tmp_sources.write(line[1:])
            else:
                tmp_sources.write(line)

move(tmp_sources.name, sources_file.name)