#!/usr/bin/env bash
#
# kopiering af keys til non-vagrant virtual instans
#

remote_host="$1"

if [ -z "$remote_host" ]; then
  echo "hostnavn skal indtastes"
  exit 1
fi

case "$remote_host" in
  katrine.test) ;;
  michael.test) ;;
  karina.test)  ;;
  martin.test)  ;;
  *)
    printf "ssh keys kan ikke kopiers til %s\n"  "$remote_host"
    exit 1
    ;;
esac
printf "ssh key kan kopieres til %s\n" "$remote_host"

ssh-copy-id -i /home/jackie/.ssh/winston.pub jackie@"$remote_host"
scp /home/jackie/.ssh/winston katrine:/home/jackie/.ssh/id_rsa
scp /home/jackie/.ssh/winston.pub katrine:/home/jackie/.ssh/id_rsa.pub

