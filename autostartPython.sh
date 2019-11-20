#!/bin/bash
HOMEDIR=/home/pi


BASEDIR=$HOMEDIR

cd $BASEDIR/Epau
set -e
sudo pigpiod
set +e
python3 main.py >> /tmp/python.log 2>&1 




