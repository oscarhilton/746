import pygame
pygame.mixer.init()

def playRing():
    s = pygame.mixer.Sound("ringring.wav")
    s.play()