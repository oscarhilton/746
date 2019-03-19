#!/usr/bin/python3
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.init()
    
def playRing():
    print("playing ring!")
    pygame.mixer.music.load("ringring.wav")
    pygame.mixer.music.play(2)

def quit():
    pygame.quit()