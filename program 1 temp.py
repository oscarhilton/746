#!/usr/bin/python3
import RPi.GPIO as GPIO  
import math, sys, os
import subprocess
import socket
import sounds

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

    service = availableNumbers.get(number)
    try:
        sounds.playRing()
        globals()[service](inCall, number)
        inCall = True
    except KeyError:
        return
    
def spotify(inCall, number):
    if inCall:
        print("Entered number ", number)
    else:
        print("Loading up spotify!")
    
def slack(inCall, number):
    if inCall:
        print("Entered number ", number)
    else:
        print("Loading up slack!")

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

                    if number == 10:
                        inCall = False
                        print("Call ended")

                    c= 0                 
                    
                    
                last = GPIO.input(18)
    except KeyboardInterrupt:
        break
