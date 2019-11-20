#!/bin/bash
HOMEDIR=/home/pi


BASEDIR=$HOMEDIR

cd $BASEDIR/vermuth/server
NODE_ENV=production /usr/bin/node -r tsconfig-paths/register -r ts-node/register ./src/server.ts --path="${BASEDIR}/Epau/vermuth/" --session=$HOSTNAME --public="${BASEDIR}/vermuth/server/dist/server/public">> /tmp/vermuth.log 2>&1 
