#!/usr/bin/python3
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.init(channels=1)
pygame.mixer.set_num_channels(2)

class Sound:
    def  __init__(self, url, channel=0):
        self.url = url
        self.sound = pygame.mixer.Sound(url)
        self.channel = channel

    def play(self, loops):
        pygame.mixer.Channel(self.channel).play(self.sound, loops=loops)

    def queue(self):
        isBusy = pygame.mixer.get_busy()
        if isBusy:
            pygame.mixer.Channel(self.channel).queue(self.sound)
        else:
            pygame.mixer.Channel(self.channel).play(self.sound)

offHook = Sound("sounds/offHook.wav", 0)
ring = Sound("sounds/ringring.wav", 0)
jazz = Sound("sounds/jazz.wav", 0)
answered = Sound("sounds/answered.wav", 0)

def playOffHook():
    offHook.play(-1)

def playRing():
    ring.play(1)

def playAnswered():
    answered.queue()

def playJazz():
    jazz.queue()

def playWeatherSounds():
    ring.play(2)
    answered.queue()
    jazz.queue()
