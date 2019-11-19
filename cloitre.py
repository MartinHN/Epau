import os

from Light import Light
from config import *
from Detector import Detector
from time import time,sleep
from PyGamePlayer import PyGamePlayer

loopTime = 30
isLooping = False
needStartLoop = False
player = PyGamePlayer()

cfg = getLocalConfig()
if(not cfg):
  cfg = getLocalConfig("anamorphose1")

print("cfg",cfg)

player.load(cfg["file"])

def newDetection(gpio,level,tick):
  global needStartLoop
  if level and (not isLooping):
    needStartLoop=True


def startLoop():
  global isLooping
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
  l.goToSeq("base",3)
  isLooping=False



l = Light()
def doActionAtIdx(i):
  print("action", i)
  l.goToSeq(str(i),.3)


if __name__=="__main__":
  l.goToSeq("base",5)
  d = Detector(newDetection)
  
  while True:
    if(needStartLoop):
      startLoop()
    

  