import time
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Animation:
    def __init__(self):
        self.frames = []
        self.fps = 12

    def addFrame(self, content):
        self.frames.append(content)

    def setFps(self, num):
        self.fps = num

    def start(self):
        for frame in self.frames:
            clear_screen()
            print(frame)
            time.sleep(1 / self.fps)
