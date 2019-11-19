import socket

baseMediaPath = "/home/pi/media/"

def splitStr(h,s):
  if h.startswith(s):
    return [h[:len(s)],int(h[len(s):])]

def getLocalConfig(h=None):
  global baseMediaPath
  hn=h or socket.gethostname()

  print("hostname",hn)
  if(hn=="Tintamar"):
    baseMediaPath = "/Users/Tintamar/Google_Drive/00_spectacles/MOMOEpau/media/"
    return getConfigForParsedHn("anamorphose",1)
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
  elif n==2:
    baseConf["times"] = []

  return baseConf

if __name__=="__main__":
  print(getLocalConfig("anamorphose1"))
  
