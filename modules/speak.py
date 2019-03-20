import pyttsx

engine = pyttsx.init()

def speak(sentence):
  engine.say(sentence)
  engine.runAndWait()