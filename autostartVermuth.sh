#!/bin/bash
HOMEDIR=/home/pi


BASEDIR=$HOMEDIR

cd $BASEDIR/vermuth/server
NODE_ENV=production node dist/server/src/server.js --path="${BASEDIR}/Epau/vermuth/" --session=$HOSTNAME --public="${BASEDIR}/vermuth/server/dist/server/public">> /tmp/vermuth.log 2>&1 
