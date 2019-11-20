from pythonosc import udp_client

import time


class Light:
  def __init__(self,host=None,port=None):
    self.host = host or "127.0.0.1"
    self.port = port or 11000
    self.client = udp_client.SimpleUDPClient(self.host, self.port)
    

  def goToSeq(self,seqName,time=0):
    print("go to ",seqName, "in ",time, self.host,self.port)
    self.sendOSC('/sequencePlayer/goToStateNamed',[seqName,time])

  
  def sendOSC(self,addr,args):
    try:
      self.client.send_message(addr, args)
    except:
      print ("no client connected")


if __name__=="__main__":
  l = Light()
  i=100
  delay = 1
  while i>0:

    l.goToSeq("1",delay)
    time.sleep(delay)
    l.goToSeq("base",delay)
    time.sleep(delay)
    i-=1