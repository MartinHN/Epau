import os
import subprocess
from config import getHostName 


if __name__=="__main__":
  hn = getHostName()
  print("starting for ",hn)
  if hn.startswith("anamorphose") or hn=="tintamar":
    from anamorphose import doMainLoop
    doMainLoop()
  else:
    print("not found hostname")
    exit(1)
