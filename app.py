#!/usr/bin/python3
import RPi.GPIO as GPIO
import math, sys, os
import subprocess
import socket
from modules import sounds
from modules import lights

from modules.Phone import Phone
from modules.Spotify import Spotify
from modules.Weather import Weather
from modules.News import News
from weather import Unit

# Startup clean and start lights
lights.startup()
sounds.removeAllSounds()

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup
availableNumbers = {
    "123": "spotify",
    "321": "slack",
    "111": "news",
    "222": "weather",
    "672": "amswerphone",
    "888": "shutdown"
}
c = 0
last = 1
phoneNumber = ""
inCall = False
def restart():
    global c = 0
    global last = 1
    global phoneNumber = ""
    global inCall = False

# Instanciate Services =======
service = Phone()
spotify = Spotify()
weather = Weather()
news = News()

# Shutdown
def shutdown():
    lights.shutdown()
    os.system('sudo shutdown now')

def count(pin):
    global c
    c = c + 1

def addToNumber(num):
    global phoneNumber
    if num > 0:
        phoneNumber = phoneNumber + str(num)

def callPhoneNumber(number):
    global availableNumbers
    global inCall
    global phoneNumber
    global service

    if number in availableNumbers and not service.running:
        serviceName = availableNumbers.get(number)

        if serviceName != "shutdown":
            service.setName(serviceName)
            service.setNumber(number)
            service.run()
            phoneNumber = ""
        else:
            shutdown()

    if service.running:
        try:
            if inCall:
                globals()[service.name].enterNumber(number)
            else:
                globals()[service.name].enterCall()
                inCall = True

        except KeyError:
            print("There's no service here.. strange")
            service.reset()
            return

GPIO.add_event_detect(18, GPIO.BOTH)

while True:
    try:
        while GPIO.input(19) == False:
            lights.lightOn()
            if not inCall:
                sounds.playOffHook()
            if GPIO.event_detected(18):
                current = GPIO.input(18)
                if(last != current):
                    if(current == 0):
                        GPIO.add_event_detect(23, GPIO.BOTH, callback=count, bouncetime=10)
                    else:
                        GPIO.remove_event_detect(23)
                        number = int((c-1)/2)
                        addToNumber(number)

                        print ("You dialed", number, phoneNumber)

                        callPhoneNumber(phoneNumber)

                        if inCall:
                            phoneNumber = ""

                        if number == 10 or len(phoneNumber) > 9:
                            inCall = False
                            phoneNumber = ""
                            print("Call ended")

                        c= 0

                    last = GPIO.input(18)
        if inCall:
            if service.running:
                globals()[service.name].hangup()
            inCall = False
        lights.lightOff()
        restart()
        sounds.stopAll()
        service.reset()
        sounds.removeAllSounds()
    except KeyboardInterrupt:
        break
