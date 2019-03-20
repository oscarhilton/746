import pyttsx

engine = pyttsx.init('espeak')

def speak(sentence):
  engine.say(sentence)
  engine.runAndWait()