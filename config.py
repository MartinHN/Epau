import socket
import os
import re

baseMediaPath = "/home/pi/media/"

def splitStr(h,s):
  if h.startswith(s):
    return [h[:len(s)],h[len(s):]]

def getHostName():
  hn = socket.gethostname()
  if hn.endswith(".local"):
    hn=hn[:-6]
  return hn.lower()

def getInsensitiveMediaFile(p):
  plow =p.lower()
  for filename in os.listdir(baseMediaPath):
    if filename.lower()==plow:
      return os.path.join(baseMediaPath,filename)

def flexComp(a,b):
  return str(a).lower()==str(b).lower()

def getLocalConfig(h=None):
  global baseMediaPath
  hn=h or getHostName()
  print("hostname",hn)
  if(hn=="tintamar" or hn=="imac-de-olivier.home"):
    baseMediaPath = "/Users/Tintamar/Google_Drive/00_spectacles/MOMOEpau/media/"
    hn="zikTst".lower()
  types = ["anamorphose","animo","zik"]
  for t in types:
    spl = splitStr(hn,t)
    if spl:
      return getConfigForParsedHn(spl[0],spl[1])#int(spl[1]

def getConfigForParsedHn(h,n): 
  if h=="anamorphose":
    baseConf = {
    "file":getInsensitiveMediaFile("Epau Cloitre Point de vue %s.wav"%n)
    }
    if n=="a":
      baseConf["times"] = [2,2.77,3.5,4.25,5]
      baseConf["minLoopTime"] = 30
    elif n=="b":
      baseConf["times"] = [5,   7,  9,  11, 13, 15,17,19,21,23,24,25,29]
      baseConf["fadeIn"] =[1,   1,  1,   1,  1,  1, 1, 1, 1, 1,.2, 4, 5]
      baseConf["minLoopTime"] = 37
    elif n=="c":
      baseConf["times"] = [0,1,2,3,4,7]
      baseConf["fadeIn"] =[0,0,0,0,0,6] 
      baseConf["minLoopTime"] = 16
  
  elif h=="animo":
    #fns = ["Chouette","Coq","Crapaud","Grenouille","PetitOiseau"]
    baseConf = {
    "file":getInsensitiveMediaFile("%s.wav"%n)
    }

    if n=="chouette":#Chouette
      baseConf["times"] = [x/6 for x in range(0,7)]
      baseConf["globalFade"] = .2
      baseConf["minLoopTime"] = 1
    elif n=="coq":#coq
      baseConf["times"] = [0.04,.35, .6,.9]
      baseConf["fadeIn"] =[0.4 ,0.4,0.4, 1] 
      baseConf["minLoopTime"] = 1
    elif n=="crapaud":#crapaud
      baseConf["times"] = [0.06,1.,2.45,3. ]
      baseConf["fadeIn"] =[0.33,0.27,0.24,0.28] 
      baseConf["minLoopTime"] = 4
    elif n=="grenouille":
      baseConf["times"] = [0.01,.75,2. ]
      #baseConf["fadeIn"] =[0.4,0.4,0.4] 
      baseConf["minLoopTime"] = 3
    elif n=="petitoiseau": #random
      baseConf["minLoopTime"] = 4
      baseConf["times"] = [0.5,.75,.9,1,1.7,2.1,2.45, 2.6,3.2,3.8,4,4.44]
      baseConf["random"] = 6

  elif h=="zik":
    if n=="cloitre":
      baseConf = {"file":getInsensitiveMediaFile("Epau Cloitre Point de vue General.wav")}
    else:
      baseConf = {"file":getInsensitiveMediaFile("Allee %s.wav"%n)}

  return baseConf

if __name__=="__main__":
  print(getLocalConfig())
  
