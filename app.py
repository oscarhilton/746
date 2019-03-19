#!/usr/bin/python3
import RPi.GPIO as GPIO  
import math, sys, os
import subprocess
import socket
import sounds

from modules.Spotify import Spotify

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

c = 0
last = 1
phoneNumber = ""
availableNumbers = {
    "123": "spotify",
    "321": "slack",
    "672": "amswerphone"
}
inCall = False
service = {
    running: False,
    number: "",
    name: ""
}

spotify = Spotify()

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

    if number in availableNumbers and !service.running:
        print("Yep!")
        service.name = availableNumbers.get(number)
        service.number = number
        print(service)

    else:
        print("Nope")

    if service.running:
        try:
            if inCall:
                globals()[service.name].saySomething()
                globals()[service.name].enterNumber(number)
            else: 
                globals()[service.name].enterCall()
                inCall = True
    
        except KeyError:
            print("There's no service here.. strange")
            return

GPIO.add_event_detect(18, GPIO.BOTH)

while True:
    try:
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
    except KeyboardInterrupt:
        break
