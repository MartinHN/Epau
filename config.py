import socket

baseMediaPath = "/home/pi/media/"

def splitStr(h,s):
  if h.startswith(s):
    return [h[:len(s)],int(h[len(s):])]

def getHostName():
  hn = socket.gethostname()
  if hn.endswith(".local"):
    hn=hn[:-6]
  return hn

def getLocalConfig(h=None):
  global baseMediaPath
  hn=h or getHostName()
  print("hostname",hn)
  if(hn=="tintamar"):
    baseMediaPath = "/Users/Tintamar/Google_Drive/00_spectacles/MOMOEpau/media/"
    return getConfigForParsedHn("anamorphose",3)
  types = ["anamorphose"]
  for t in types:
    spl = splitStr(hn,t)
    if spl:
      return getConfigForParsedHn(spl[0],spl[1])

def getConfigForParsedHn(h,n): 
  if h=="anamorphose":
    baseConf = {
    "file":baseMediaPath+"Epau Cloitre Point de vue 0%i.wav"%n
    }
  if n==1:
    baseConf["times"] = [2,2.77,3.5,4.25,5]
    baseConf["minLoopTime"] = 30
  elif n==2:
    baseConf["times"] = [4,   6,  8,  10, 12, 15,17,19,21,23,24,25,29]
    baseConf["fadeIn"] =[2,   2,  2,   2,  2,  1, 1, 1, 1, 1, 1, 4, 5]
    baseConf["minLoopTime"] = 37
  elif n==3:
    baseConf["times"] = [0,1,2,3,4,7]
    baseConf["fadeIn"] =[0,0,0,0,0,6] 
    baseConf["minLoopTime"] = 16

  return baseConf

if __name__=="__main__":
  print(getLocalConfig())
  
