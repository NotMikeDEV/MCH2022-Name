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

Brightness = 16
def home_btn(pressed):
  global Brightness
  if pressed:
    if Brightness == 0:
      Brightness = 1
    elif Brightness >= 128:
      Brightness = 255
    else:
      Brightness = Brightness << 1

def menu_btn(pressed):
  global Brightness
  if pressed:
    Brightness = Brightness >> 1

buttons.attach(buttons.BTN_HOME, home_btn)
buttons.attach(buttons.BTN_MENU, menu_btn)

display.drawText(220, 140, ".co.uk", display.GREEN, "PermanentMarker22")

COL=0
while True:
  TextColours = [display.RED, display.GREEN, display.BLUE, display.WHITE]
  LEDColours = [(Brightness,0,0), (0,Brightness,0), (0,0,Brightness), (Brightness,Brightness,Brightness)]
  l = ["N", "o", "t", "M", " i", "k", "e"]
  pos = 25
  for i in l:    
    COL = (COL + 1) % 4;
    display.drawText(pos, 90, i, TextColours[COL], "permanentmarker22", 2 ,2)
    pos += 40
    display.flush()
    np[0] = np[1] = np[2] = np[3] = np[4] = LEDColours[COL]
    np.write()
    time.sleep(0.1);
