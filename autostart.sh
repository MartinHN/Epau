#!/bin/bash
exec &> "${HOME}/epaulog.txt"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
BASEDIR=$DIR/..

cd $BASEDIR/vermuth/server
sudo NODE_ENV=production node dist/server/src/server.js --path="${BASEDIR}/Epau/vermuth/" --session=$HOSTNAME &

cd $BASEDIR/Epau
sudo ./run.sh &



