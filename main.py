import os
import subprocess
from config import getHostName 


if __name__=="__main__":
  hn = getHostName()
  if hn=="anamorphose":
    from cloitre import doMainLoop
    doMainLoop()
