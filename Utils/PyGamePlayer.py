import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

class PyGamePlayer(object):
  def __init__(self):
    pass

  def load(self,path):
    self.path = path
    print("loading",path)
    self.sound= pygame.mixer.music.load(path)
    
  def play(self):
    pygame.mixer.music.play()

  def wait(self):
    while pygame.mixer.music.get_busy() == True:
      continue

  def stop(self):
    self.sound.stop()



if __name__=="__main__":
  import optparse
  parser = optparse.OptionParser()
  (opts,args) = parser.parse_args()
  fileToPlay = args[0]
  print(opts,args)
  player = PyGamePlayer()
  player.load(fileToPlay)
  player.play()
  player.wait()
  # player.stop()