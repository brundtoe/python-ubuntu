#!/usr/bin/env bash
PASS=vagrant
USER=vagrant
echo -ne "$PASS\n$PASS\n" | smbpasswd -a -s $USER
