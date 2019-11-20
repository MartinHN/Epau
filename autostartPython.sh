#!/bin/bash
HOMEDIR=/home/pi


BASEDIR=$HOMEDIR

cd $BASEDIR/Epau
python3 main.py >> /tmp/python.log 2>&1 




