import pyscreenshot as ImageGrab
import time
import sys
import time
from PIL import Image

# example: python3 image.py 320 180 1900 1080

def grab_screen(region=None):
    last_time = time.time()
    screen = None
    filename = None
    if region:
            left,top,x2,y2 = region
            width = x2 - left + 1
            height = y2 - top + 1
    screen = ImageGrab.grab(bbox=(left, top, width, height))
    filename = 'screencapture-{}.png'.format(last_time)
    last_time = time.time()
    screen.save(filename)

# region=(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
region=(320, 180, 1900, 1050)
grab_screen(region)
