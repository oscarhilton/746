#!/usr/bin/python3
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.init()

def playRing():
    print("playing ring!")
    ring = pygame.mixer.Sound("ringring.wav")
    ring.play()