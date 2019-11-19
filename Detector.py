import pigpio

pi1 = pigpio.pi()

def cbf(gpio, level, tick):
   print(gpio, level, tick)
   detector.cb(gpio,level,tick)

class Detector(object):
  def __init__(self,cb):
    self.pin = 0
    self.cb1 = pi.callback(22, pigpio.EITHER_EDGE, cbf)
  
  def setCB(c):
    self.cb = cb



detector = Detector()

