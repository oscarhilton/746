import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT) #Light

def startup(ready = True):
  i = 1
  while i < 20 and ready:
    try:
      GPIO.output(20, True)
      time.sleep(0.1)
      GPIO.output(20, False)
      time.sleep(0.1)
      i += 1
    except:
      break

def shutdown():
  while True:
    try:
      GPIO.output(20, True)
      time.sleep(0.1)
      GPIO.output(20, False)
      time.sleep(0.1)
    except:
      break