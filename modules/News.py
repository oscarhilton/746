from Call import Call
import requests
import sounds
import os
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class News(Call):
  def __init__(self):
    self.name = "News"
    self.dynamicOptions = True
    self.options = ["headlines"]

  def enterCall(self):
      if GPIO.input(19) == False:
        sounds.playNewsSounds()
        self.inCall = True
        print("You are in call with ", self.name)
        print("These are the options ", self.options)
        sounds.saySomething("Welcome to news! Here are the headlines!")
        self.headlines()

  def headlines(self):
    sources = "bbc-news"
    r = requests.get('https://newsapi.org/v2/top-headlines?sources={}&apiKey=cfb2ed55add84931be4a7e8ae66cf053'.format(sources))
    data = r.json()
    articles = data["articles"]

    while GPIO.input(19) == False:
      num = 0
      for article in articles:
        sounds.playBell()
        print(article["title"])
        sounds.saySomething("Dial {} for {}.".format(articles.index(article) + 1, article["title"]))
        num = num + 1
      if num == len(articles):
        break

    sounds.saySomething("And that concludes today's headlines!")
