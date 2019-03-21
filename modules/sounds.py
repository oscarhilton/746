#!/usr/bin/python3
import pygame
import io
from pygame import mixer

pygame.init()
pygame.mixer.init(channels=1)
pygame.mixer.set_num_channels(2)

class Polly:
    OUTPUT_FORMAT = "mp3"

    def __init__(self, voiceId):
        self.polly = boto3.client('polly')
        self.VOICE_ID = voiceId

    def say(self, text):
        response = polly.synthesize_speech(Text=text, TextType="text", OutputFormat=OUTPUT_FORMAT, VoiceId=self.VOICE_ID)

       with io.BytesIO() as f: # use a memory stream
            f.write(pollyResponse['AudioStream'].read()) #read audiostream from polly
            f.seek(0)
            pygame.mixer.music.load(f)
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
            pygame.event.set_allowed(pygame.USEREVENT)
            pygame.mixer.music.play()
            pygame.event.wait() # play() is asynchronous. This wait forces the speaking to be finished before closing
            
        while pygame.mixer.music.get_busy() == True:
            pass


class Sound:
    def  __init__(self, url, channel=0, volume=1):
        self.SOUND = pygame.mixer.Sound(url)
        self.CHANNEL = channel

        self.sound.set_volume(volume)

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
jazz = Sound("sounds/jazz.wav", 0, 1)
answered = Sound("sounds/answered.wav", 0, 1)
news = Sound("sounds/news.wav", 0, 0.1)

def saySomething(text):
    return Polly(text)

def playOffHook():
    offHook.play(-1)

def playRing():
    ring.play(1)

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