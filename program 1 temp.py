#!/usr/bin/python3
import RPi.GPIO as GPIO  
import math, sys, os
import subprocess
import socket

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

c = 0
last = 1
phoneNumber = ""
availableNumbers = {
    "123": "spotify",
    "321": "slack"
}
inCall = False

def count(pin):
    global c 
    c = c + 1

def addToNumber(num):
    global phoneNumber
    phoneNumber = phoneNumber + str(num)

def callPhoneNumber(number):
    global availableNumbers
    global inCall
    n = availableNumbers.get(number)
    try:
        globals()[n](inCall, number)
        
        if inCall:
            phoneNumber = ""

        inCall = True
    except KeyError:
        return
    
def spotify(inCall, number):
    if inCall:
        print("Entered number ", number)
    else:
        print("Loading up spotify!")
    
def slack(inCall, number):
    print("Loading up slack! ", number)

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
		                       
                    print ("You dial", number, phoneNumber)

                    callPhoneNumber(phoneNumber)

                    c= 0                 
                    
                    
                last = GPIO.input(18)
    except KeyboardInterrupt:
        break
