#!/usr/bin/python3
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.init()

def playRing():
    ring = pygame.mixer.Sound("ringring.wav")
    ring.play()