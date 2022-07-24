import display
import time
import audio

from machine import Pin
from neopixel import NeoPixel

# Pin 19 controls the power supply to SD card and neopixels
powerPin = Pin(19, Pin.OUT)

# Pin 5 is the LED's data line
dataPin = Pin(5, Pin.OUT)

# create a neopixel object for 5 pixels
np = NeoPixel(dataPin, 5)

# turn on power to the LEDs
powerPin.on()

# set some colors for the pixels (RGB)
np[0] = (255,0,0)
np[1] = (0,255,0)
np[2] = (0,0,255)
np[3] = (255,255,0)
np[4] = (255,0,255)

# send colors out to LEDs
np.write()


display.drawFill(display.BLACK)
display.flush()
Channel = None
Playing = False
import buttons

def stop_btn(pressed):
  global Channel
  global Playing
  if pressed:
    if Playing:
      audio.stop_channel(Channel)
      Playing = False

def start_btn(pressed):
  global Channel
  global Playing
  if pressed:
    if Playing:
      audio.stop_channel(Channel)
    Channel = audio.play('/apps/python/NotMike/Rick.mp3', volume=128)
    Playing = True


buttons.attach(buttons.BTN_A, start_btn)
buttons.attach(buttons.BTN_B, stop_btn)

COL=0
while True:
  TextColours = [display.RED, display.GREEN, display.BLUE, display.WHITE]
  LEDColours = [(128,0,0), (0,128,0), (0,0,128), (128,128,128)]
  l = ["N", "o", "t", "M", " i", "k", "e"]
  pos = 70
  for i in l:    
    COL = (COL + 1) % 4;
    display.drawText(pos, 100, i, TextColours[COL], "PermanentMarker36")
    pos += 25
    display.flush()
    np[0] = np[1] = np[2] = np[3] = np[4] = LEDColours[COL]
    np.write()
    time.sleep(0.1);
