import socket

baseMediaPath = "/home/pi/media/"

def splitStr(h,s):
  if h.startswith(s):
    return [h[:len(s)],int(h[len(s):])]

def getHostName():
  hn = socket.gethostname()
  if hn.endswith(".local"):
    hn=hn[:-6]
  return hn.lower()

def getLocalConfig(h=None):
  global baseMediaPath
  hn=h or getHostName()
  print("hostname",hn)
  if(hn=="tintamar"):
    baseMediaPath = "/Users/Tintamar/Google_Drive/00_spectacles/MOMOEpau/media/"
    return getConfigForParsedHn("animo",3)
  types = ["anamorphose","animo","zik"]
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
      baseConf["times"] = [5,   7,  9,  11, 13, 15,17,19,21,23,24,25,29]
      baseConf["fadeIn"] =[1,   1,  1,   1,  1,  1, 1, 1, 1, 1,.2, 4, 5]
      baseConf["minLoopTime"] = 37
    elif n==3:
      baseConf["times"] = [0,1,2,3,4,7]
      baseConf["fadeIn"] =[0,0,0,0,0,6] 
      baseConf["minLoopTime"] = 16
  
  elif h=="animo":
    fns = ["Chouette","Coq","Crapaud"]
    baseConf = {
    "file":baseMediaPath+"%s.wav"%fns[(n-1)%len(fns)]
    }

    if n==1:#Chouette
      baseConf["times"] = [x/6 for x in range(0,7)]
      baseConf["minLoopTime"] = 1
    elif n==2:#coq
      baseConf["times"] = [0.04,.35,.6]
      baseConf["minLoopTime"] = 1
    elif n==3:#crapaud
      baseConf["times"] = [0.14,1.14,2.50,3.1 ]
      baseConf["fadeIn"] =[0.25,0.25,0.25,0.25] 
      baseConf["minLoopTime"] = 4

  elif h=="zik":
    fns = ["zik1","Coq","Crapaud"]
    baseConf = {
    "file":baseMediaPath+"%s.wav"%fns[(n-1)%len(fns)]
    }

  return baseConf

if __name__=="__main__":
  print(getLocalConfig())
  
