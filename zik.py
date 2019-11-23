import os
import random

from config import *

from time import time,sleep
from Utils.PyGamePlayer import PyGamePlayer



cfg = getLocalConfig()
if(not cfg):
  raise NameError("no config found")
  

print("cfg",cfg)
restTime = 1
player = PyGamePlayer()
player.load(cfg["file"])


def doMainLoop():
  while True:
    player.play()
    player.wait()
    sleep(restTime)
      
if __name__=="__main__":
  doMainLoop()
    

  