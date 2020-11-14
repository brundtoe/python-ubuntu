#!/usr/bin/env bash

echo $(whoami)

if [ $(whoami) != "root" ]; then
        echo "Script must be run as user: root"
        exit -1
fi


