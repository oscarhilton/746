#!/usr/bin/python3
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.init()

def playOffHook():
    pygame.mixer.music.load("sounds/offHook.wav")
    pygame.mixer.music.play(-1)
    
def playRing():
    print("playing ring!")
    pygame.mixer.music.load("sounds/ringring.wav")
    pygame.mixer.music.play(2)

def playJazz():
    pygame.mixer.music.load("sounds/jazz.wav")
    pygame.mixer.music.play()

def isBusy():
    return pygame.mixer.music.get_busy()

def quit():
    pygame.quit()