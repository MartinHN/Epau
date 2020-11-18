
from Utils.PyGamePlayer import PyGamePlayer
from glob import glob
import os
from os import getcwd, chdir
types = ('*.wav', '*.mp3')
audioFolders = ["/home/pi/media/", "/boot/medias",
                "/home/tinmar/Documents/Sounds/pl"]


def listAudioFiles(dir):
    if not os.path.exists(dir):
        return []
    saved = getcwd()
    chdir(dir)
    files_grabbed = []
    for ext in types:
        files_grabbed.extend(glob(ext))

    chdir(saved)
    return files_grabbed


class AutoAudioPlayer(object):
    def __init__(self):
        self.player = PyGamePlayer()
        for p in audioFolders:
            if os.path.exists(p):
                print("listing audios in", p)
                self.audioFiles = [p+"/"+x for x in listAudioFiles(p)]
                print(self.audioFiles)
                if(not self.audioFiles):
                    NameError("no audio files found in ", p)
                self.startFileAt(0)
                break

    def startFileAt(self, idx):
        idx = idx % len(self.audioFiles)
        self.curIdx = idx
        self.player.load(self.audioFiles[self.curIdx])
        self.player.play()

    def loop(self):
        self.player.wait()
        self.startFileAt(self.curIdx+1)


def doMainLoop():
    a = AutoAudioPlayer()
    while True:
        a.loop()


if __name__ == "__main__":
    doMainLoop()
