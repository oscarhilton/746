import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT) #Buzzer

def ringRing(isRinging = True):
  while isRinging:
    GPIO.output(24, True)
    sleep(1)
    GPIO.output(24, False)
    sleep(1)
    GPIO.output(24, True)
    sleep(1)
    GPIO.output(24, False)
    sleep(2)
