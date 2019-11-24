import os
import subprocess
from config import getHostName 


if __name__=="__main__":
  hn = getHostName()
  print("starting for ",hn)
  if hn.startswith("anamorphose"):
    from anamorphose import doMainLoop
    doMainLoop()
  elif hn.startswith("animo") or hn=="tintamar":
    from animo import doMainLoop
    doMainLoop()
  elif hn.startswith("zik"):
    from zik import doMainLoop
    doMainLoop()
  else:
    print("not found hostname")
    exit(1)
