import pyautogui as pag
from PIL import ImageGrab
from time import sleep
import numpy as np

pag.FAILSAFE = True

def getFish():
    pag.keyDown('e')
    sleep(.4)
    pag.keyUp('e')

def getImg():
    img = ImageGrab.grab(bbox = (1008, 725, 1028, 735))
    img = img.convert('1')
    thresh = 200
    fn = lambda x : 255 if x > thresh else 0
    r = img.convert('L').point(fn, mode='1')
    data = np.asarray(r, dtype="int32")
    print(data.sum())

    return data.sum()

print("Starting In:")
for time in range(5):
    print(5 - time)
    sleep(1)

getImg()

prior = 0
while True:
    baseImg = getImg()
    sleep(.01)
    if baseImg > prior+5:
        getFish()
        print("fish")
        prior = baseImg
    elif baseImg < prior-5:
        getFish()
        print("fish")
        prior = baseImg
    else:
        prior = baseImg
