#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
BASEDIR=$DIR/..

cd $BASEDIR/vermuth/server
NODE_ENV=production node dist/server/src/server.js --path="${BASEDIR}/Epau/vermuth/" --session=$HOSTNAME &

cd $BASEDIR/Epau
./run.sh &



