from pythonosc import udp_client

import time


class Light:
  def __init__(self,host=None):
    host = host or "localhost"
    self.client = udp_client.SimpleUDPClient(host, 11000)
    

  def goToSeq(self,seqName,time=0):
    self.sendOSC('/sequencePlayer/goToStateNamed',[seqName,time])

  
  def sendOSC(self,addr,args):
    try:
      self.client.send_message(addr, args)
    except:
      print ("no client connected")


if __name__=="__main__":
  l = Light()
  i=100
  delay = .1
  while i>0:
    l.goToSeq("fds",delay)
    time.sleep(delay)
    l.goToSeq("kk",delay)
    time.sleep(delay)
    i-=1