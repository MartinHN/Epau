import os
import random
from Utils.Light import Light
from config import *

from time import time,sleep
from Utils.PyGamePlayer import PyGamePlayer


isLooping = False
needStartLoop = False
player = PyGamePlayer()

cfg = getLocalConfig()
if(not cfg):
  raise NameError("no config found")
  

print("cfg",cfg)
restTime = 3
loopTime = cfg["minLoopTime"]+restTime
player.load(cfg["file"])


def startLoop():
  global isLooping
  global needStartLoop
  needStartLoop=False

  l.goToSeq("base",1)
  isLooping=True
  startTime = time()
  player.play()
  cTime = 0
  nextAIdx = 0
  randomState=0
  if("random" in cfg):
    randomState = cfg["random"]
  if not "times" in cfg:
    interval = .1
    resolution = int(cfg["minLoopTime"]/interval)
    timePoints = [x/cfg["minLoopTime"] for x in range(0,resolution)]
    print(timePoints)
  else:
    timePoints = cfg["times"]
  nextATime = timePoints[nextAIdx]

  doActionAtIdx(-1)
  while cTime<loopTime:
    cTime = time() - startTime
    if(cTime>=nextATime):
      if randomState>0:
        doActionAtIdx(1+int(random.random()*randomState))
      else:
        doActionAtIdx(nextAIdx+1)
      nextAIdx+=1
      if nextAIdx<len(timePoints):
        nextATime = timePoints[nextAIdx]
      else:
        nextATime = loopTime
    
    slTime = nextATime - cTime
    print('sleeping for',slTime)
    if(slTime>0):
      sleep(slTime)
  l.goToSeq("base",restTime)
  sleep(restTime)
  isLooping=False



l = Light()
def doActionAtIdx(i):
  print("action", i)
  fadeIn = 0
  if "fadeIn" in cfg:
    if i-1>=0 and i-1<len(cfg["fadeIn"]):
      fadeIn = cfg["fadeIn"][i-1]
  elif "globalFade" in cfg:
    fadeIn = cfg["globalFade"]
  l.goToSeq(str(i),fadeIn)


def doMainLoop():
  global needStartLoop
  l.goToSeq("base",5)
  while True:
    if(needStartLoop):
      startLoop()

    sleep(3) 
    needStartLoop = random.random()>.5

      
if __name__=="__main__":
  doMainLoop()
    

  