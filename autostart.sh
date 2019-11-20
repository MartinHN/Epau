#!/bin/bash
HOMEDIR=/home/pi
exec &> "${HOMEDIR}/epaulog.txt"

BASEDIR=$HOMEDIR

cd $BASEDIR/vermuth/server
sudo NODE_ENV=production node dist/server/src/server.js --path="${BASEDIR}/Epau/vermuth/" --session=$HOSTNAME &

cd $BASEDIR/Epau
sudo ./run.sh &



