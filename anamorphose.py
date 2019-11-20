import os

from Utils.Light import Light
from config import *
from Utils.Detector import Detector
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

def newDetection(gpio,level,tick):
  global needStartLoop
  if level and (not isLooping):
    needStartLoop=True


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
  nextATime = cfg["times"][nextAIdx]

  doActionAtIdx(-1)
  while cTime<loopTime:
    cTime = time() - startTime
    if(cTime>=nextATime):
      doActionAtIdx(nextAIdx+1)
      nextAIdx+=1
      if nextAIdx<len(cfg["times"]):
        nextATime = cfg["times"][nextAIdx]
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
  fadeIn = .3
  if "fadeIn" in cfg:
    if i-1>=0 and i-1<len(cfg["fadeIn"]):
      fadeIn = cfg["fadeIn"][i-1]
  l.goToSeq(str(i),fadeIn)


def doMainLoop():
  l.goToSeq("base",5)
  if(getHostName()=="tintamar"):
    startLoop()
    exit(0)
  d = Detector(newDetection)
  
  while True:
    if(needStartLoop):
      startLoop()
      
if __name__=="__main__":
  doMainLoop()
    

  