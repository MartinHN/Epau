import pigpio
from functools import partial
from time import sleep

rpi = pigpio.pi()

def cbf(gpio, level, tick):
   print(gpio, level, tick)
   

class Detector(object):
  def __init__(self,cb):
    pin = 4
    print('listening on pin ',pin)
    rpi.set_mode(pin, pigpio.INPUT)
    self.cb1 = rpi.callback(pin, pigpio.EITHER_EDGE, self.edgeCB)
    self.pin = pin
    self.cb = cb or cbf
  

  def setCB(self,c):
    self.cb = c
  def edgeCB(self,gpio,level,tick):
    print('edge')
    if (self.cb):
      self.cb(gpio,level,tick);



if __name__=="__main__":
  from PyGamePlayer import PyGamePlayer
  player = PyGamePlayer()
  file = "/home/pi/media/Epau Cloitre Point de vue 03.wav"
  player.load(file)
  player.play()
  #player.wait()
  def playSound(g,l,t):
    if(l):
      player.play()
      #player.wait()
  d = Detector(playSound)
  
  while True:
    sleep(1)



