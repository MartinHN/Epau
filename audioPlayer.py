import pexpect
import re



class AudioPlayer(object):
  _LAUNCH_CMD = "/usr/bin/omxplayer %s %s"
  _DONE_REXP = re.compile(r"have a niceday")
  _STATUS_REXP=re.compile(r"V :\s*([\d.]+).*")
  _PAUSE_CMD='p'
  _QUIT_CMD='q'
  paused = false
  self.path=""


  def load(self,path,cb):
    self.unload()
    args =""
    cmd=self._LAUNCH_CMD%(path,args)
    self._process=pexpect.spawn(cmd)
    self.path = path
    self._position_thread = Thread(target=self._get_position)

    def _get_position(self):
      while True:
        index = self._process.expect([self._STATUS_REXP,
          pexpect.TIMEOUT,pexpect.EOF,
          self._DONE_REXP])
        if index== 1:
          continue
        elif index in (2,3):
          break
        else:
          self.position = float(self._process.match.group(1))
          sleep(0.05)


    def unload(self):
      if(self.path):
        self._process.send(self._QUIT_CMD)
        self._process.terminate(force=True)




if __name__=="__main__":
  import optparse
  parser = optparse.OptionParser()
  (opts,args) = parser.parse_args()
  fileToPlay = args 
  print(opts,args)
  player = AudioPlayer()
  player.load(fileToPlay)
  player.play()
  player.stop()
