# export VERMUTH_ARGS="--module /home/tinmar/Dev/abbayLight/node/build/index.js"
export VERMUTH_ARGS="--module /home/pi/abbayLight/node/build/index.js"

#echo "tsc"
#cd /home/pi/abbayLight/node/
#rm -rf ./build/ && tsc

cd /home/pi/vermuth
cd server
npm run start
