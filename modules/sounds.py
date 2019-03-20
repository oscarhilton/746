#!/usr/bin/python3
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.init(channels=1)
pygame.mixer.set_num_channels(1)

class Sound:
    def  __init__(self, url):
        self.url = url
        self.sound = pygame.mixer.Sound(url)

    def play(self, loops):
        pygame.mixer.Channel(0).play(self.sound, loops=loops)

    def queue(self):
        isBusy = pygame.mixer.get_busy()
        if isBusy:
            pygame.mixer.Channel(0).queue(self.sound)
        else:
            pygame.mixer.Channel(0).play(self.sound)

offHook = Sound("sounds/offHook.wav")
ring = Sound("sounds/ringring.wav")
jazz = Sound("sounds/jazz.wav")

def playOffHook():
    offHook.play(3)

def playRing():
    ring.play(2)

def playJazz():
    jazz.queue()
