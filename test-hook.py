#!/usr/bin/python3
import RPi.GPIO as GPIO
# import subprocess
# import socket
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(19) == False:
            print("Phone Up")
            time.sleep(0.5)
        else:
            print("Phone down")
            time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()

# while True:
#     try:
#         if GPIO.input(19) == GPIO.HIGH:
#             print("PHONE OFF HOOK")
#         else:
#             print("PHONE DOWN")
#     except KeyboardInterrupt:
#         GPIO.cleanup()
#         break
