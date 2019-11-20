#!/bin/bash
HOMEDIR=/home/pi


BASEDIR=$HOMEDIR

cd $BASEDIR/Epau
sudo pigpiod
python3 main.py >> /tmp/python.log 2>&1 




