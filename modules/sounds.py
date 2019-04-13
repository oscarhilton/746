#!/usr/bin/python3
import pygame
import io
from pygame import mixer
import boto3
import datetime
import os
import time

pygame.init()
pygame.mixer.init(channels=1)
pygame.mixer.set_num_channels(2)

class Polly:
    def __init__(self, voiceId):
        self.polly = boto3.client('polly')
        self.VOICE_ID = voiceId

    def say(self, text):
        response = self.polly.synthesize_speech(LanguageCode="en-GB", TextType="ssml", Text="<speak>{}<break time='500ms'/></speak>".format(text), OutputFormat="mp3", VoiceId=self.VOICE_ID)
        data_stream = response.get("AudioStream")

        filename = "sounds/temp/{}.mp3".format(datetime.datetime.now())
        f = file(filename, "wb")

        CHUNK_SIZE = 1024

        while True:
            data = data_stream.read(CHUNK_SIZE)
            f.write(data)
            if not data:
               break

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        os.remove("sounds/temp/{}".format(filename))


class Sound:
    def  __init__(self, url, channel=0, volume=1):
        self.SOUND = pygame.mixer.Sound(url)
        self.CHANNEL = channel

        self.SOUND.set_volume(volume)

    def play(self, loops):
        pygame.mixer.Channel(self.CHANNEL).play(self.SOUND, loops=loops)

    def queue(self):
        isBusy = pygame.mixer.get_busy()
        if isBusy:
            pygame.mixer.Channel(self.CHANNEL).queue(self.SOUND)
        else:
            pygame.mixer.Channel(self.CHANNEL).play(self.SOUND)

offHook = Sound("sounds/offHook.wav", 0, 0.05)
ring = Sound("sounds/ringring.wav", 0, 0.15)
jazz = Sound("sounds/jazz.wav", 0, 0.5)
answered = Sound("sounds/answered.wav", 0, 1)
news = Sound("sounds/news.wav", 0, 0.1)
bell = Sound("sounds/bell.wav", 0, 0.6)

def removeAllSounds():
    try:
        return os.remove("sounds/temp/*")
    except OSError as error:
        print("Error: ", error)
        continue

def saySomething(text):
    return Polly("Brian").say(text)

def playOffHook():
    offHook.play(-1)

def playRing():
    stopAll()
    ring.play(1)
    time.sleep(2)

def playAnswered():
    answered.queue()

def playJazz():
    jazz.queue()

def playWeatherSounds():
    ring.play(1)
    answered.queue()
    jazz.queue()

def playNewsSounds():
    ring.play(1)
    answered.queue()
    news.queue()

def playBell():
    bell.queue()

def stopAll():
    pygame.mixer.stop()
    pygame.mixer.music.stop()
