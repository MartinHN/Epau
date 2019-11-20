#!/bin/bash
HOMEDIR=/home/pi


BASEDIR=$HOMEDIR

cd $BASEDIR/vermuth/server
sudo NODE_ENV=production /usr/bin/node dist/server/src/server.js --path="${BASEDIR}/Epau/vermuth/" --session=$HOSTNAME >> /tmp/vermuth.log 2>&1 &

cd $BASEDIR/Epau
sudo ./run.sh >> /tmp/python.log 2>&1 &




